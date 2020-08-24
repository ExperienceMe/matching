import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from data.consts import menti_match, CREDENTIALS_FILE, SS_ID, GAPI_SERVICES, MENTI_SHEET, MATCH_SHEET, MENTOR_SHEET
from collections import defaultdict
from time import sleep


def make_dict_by_row_data(data):
    """Из списка списков делает словарь. Ожидает, что в data[0] лежат заголовки – ключи для словаря"""

    headers, row_records = data[0], data[1:]

    res = {}
    for row_record in row_records:
        obj = dict(zip(headers, row_record))
        res[obj['id']] = obj

    return res


while True:
    # Авторизируемся и получаем объект для доступа к щитам – service
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, GAPI_SERVICES)
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # грузим всех менти
    row_menties = service.spreadsheets().values().get(
        spreadsheetId=SS_ID,
        range=MENTI_SHEET,
        # данные придут в виде списка списков, [[], [], ..., []], где каждый элемент – СТРОКА (ROWS) таблицы
        majorDimension='ROWS',
    ).execute()['values']
    menties = make_dict_by_row_data(row_menties)

    # грузим всех менторов
    row_mentors = service.spreadsheets().values().get(
        spreadsheetId=SS_ID,
        range=MENTOR_SHEET,
        majorDimension='ROWS',
    ).execute()['values']
    mentors = make_dict_by_row_data(row_mentors)

    # определяем новых менти
    with open('data/_stored_menties.txt') as menties_file:
        stored_menties = menties_file.read().splitlines()
    new_menti_ids = list(set(menties.keys()) - set(stored_menties))

    # res =
    # {
    #     'M01': { // mentiId
    #         // mentorId1
    #         '32': {
    #             // codes1
    #             'sphera1_code': '1_3_4',
    #             ...
    #         },
    #
    #         // mentorId2
    #         '45': { ... }, // codes2
    #     },
    #     ...
    # }
    res = defaultdict(dict)
    for new_menti_id in new_menti_ids:
        for mentor in mentors.values():
            matched_codes = {}
            for mentor_header, mentor_code in mentor.items():
                for menti_code in menties[new_menti_id].values():
                    if menti_code in menti_match and mentor_code in menti_match[menti_code]:
                        matched_codes[mentor_header] = mentor_code

            if len(matched_codes) > 1 or matched_codes.get('sphera1_code'):
                res[new_menti_id][mentor['id']] = matched_codes

        r = [new_menti_id, *sorted(
                res[new_menti_id],
                # тем, у кого сошлись sphera1_code выставляем ахриненно высокий приоритет
                key=lambda mentor_id: bool(res[new_menti_id][mentor_id].get('sphera1_code', '')) * 100 + len(res[new_menti_id][mentor_id]),
                reverse=True
            )]

        service.spreadsheets().values().append(
            spreadsheetId=SS_ID,
            range=MATCH_SHEET,
            valueInputOption='USER_ENTERED',
            body={
                'majorDimension': 'ROWS',
                'values': [r],
            },
        ).execute()

        with open('data/_stored_menties.txt', 'a') as menties_file:
            menties_file.write(f'{new_menti_id}\n')

        print('Обработан новый менти:', new_menti_id)

    sleep(60 * 30)
