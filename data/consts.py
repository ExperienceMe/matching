from os.path import join as concat_path
from os import getcwd

CUR_DIR = getcwd()
CREDENTIALS_FILE = concat_path(CUR_DIR, 'data/credentials.json')  # файл сгенеренный в момент создания ключа
BOT_TOKEN = '1355312750:AAG-jktTI9YNjAzl_7vHqDXe3SObjAY0xEY'
CREDENTIALS_FILE = 'data/credentials.json'  # файл сгенеренный в момент создания ключа
SS_ID = '1YGw5uZap6VLPnFOpN64TrjGOuj0PCDgkpTcYfZ7AG6c'  # spreadsheet id (можно взять из URL)
GAPI_SERVICES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

MENTI_SHEET = 'menti_source'
MENTOR_SHEET = 'mentor_source'
MATCH_SHEET = 'match_result'

menti_match = {
    '1_1_1': ['2_1_6', '2_8_3', '2_1_1', '2_8_4'],
    '1_1_2': ['2_1_5', '2_8_7'],
    '1_1_3': ['2_1_6', '2_8_3', '2_1_1', '2_8_4', '2_1_5', '2_8_7'],
    '1_2_1': ['2_1_5', '2_8_7'],
    '1_2_2': ['2_8_1'],
    '1_2_3': ['2_4_14', '2_8_2', '2_6_1', '2_2_13'],
    '1_2_4': ['2_1_6', '2_8_3', '2_1_1', '2_8_4', '2_1_2'],
    '1_2_5': ['2_1_1', '2_8_4', '2_1_2', '2_1_3'],
    '1_2_6': ['2_1_3', '2_8_5', '2_1_2'],
    '1_2_7': ['2_1_4', '2_8_6'],
    '1_3_1': ['2_2_1', '2_4_1', '2_4_2', '2_2_2'],
    '1_3_2': ['2_2_2', '2_4_2', '2_4_1', '2_2_1'],
    '1_3_3': ['2_2_3', '2_4_3'],
    '1_3_4': ['2_2_4', '2_4_4'],
    '1_3_5': ['2_2_5', '2_4_5'],
    '1_3_6': ['2_2_6', '2_4_6', '2_1_3', '2_8_5'],
    '1_3_7': ['2_2_7', '2_4_7'],
    '1_3_8': ['2_2_8', '2_4_8'],
    '1_3_9': ['2_2_9', '2_4_9'],
    '1_3_10': ['2_2_10', '2_4_10'],
    '1_3_11': ['2_2_11', '2_4_11'],
    '1_3_12': ['2_2_12', '2_4_12'],
    '1_3_13': ['2_2_13', '2_4_13', '2_6_1', '2_8_2'],
    '1_3_14': ['2_2_14', '2_4_14'],
    '1_3_15': ['2_2_15', '2_4_15'],
    '1_3_16': ['2_2_16', '2_4_16'],
    '1_4_1': ['2_1_5', '2_8_7'],
    '1_4_2': ['2_8_1'],
    '1_4_3': ['2_6_1', '2_8_2'],
    '1_4_4': ['2_1_6', '2_8_3', '2_1_1', '2_8_4', '2_1_2'],
    '1_4_5': ['2_8_4', '2_1_2', '2_1_3', '2_1_1'],
    '1_4_6': ['2_8_5', '2_1_2', '2_1_3'],
    '1_4_7': ['2_8_6', '2_1_4'],
}

statuses = {
    '1_1_1': 'Учусь в ВУЗе',
    '1_1_2': 'Учусь в школе',
    '1_1_3': 'Учусь в колледже',
    '1_1_4': 'Стажируюсь/стажировался',
    '1_1_5': 'Свой бизнес',
    '1_1_6': 'Работаю',
}

requests = {
    '1_2_1': 'Выбрать ВУЗ и поступить',
    '1_2_2': 'Разобраться в новой сфере',
    '1_2_3': 'Переехать в другой город/страну',
    '1_2_4': 'Попасть на стажировку',
    '1_2_5': 'Получить работу',
    '1_2_6': 'Запустить свой бизнес',
    '1_2_7': 'Перейти на фриланс',
}

spheres = {
    '1_3_1': 'Финансы и банки',
    '1_3_2': 'Инвестиции',
    '1_3_3': 'Бизнес в IT (ProductM/ProjectM)',
    '1_3_4': 'Программирование',
    '1_3_5': 'Консалтинг',
    '1_3_6': 'Стартапы',
    '1_3_7': 'Маркетинг&PR',
    '1_3_8': 'SMM',
    '1_3_9': 'Дизайн',
    '1_3_10': 'Творчество',
    '1_3_11': 'Естественные науки',
    '1_3_12': 'Продажи',
    '1_3_13': 'Путешествия',
    '1_3_14': 'HR',
    '1_3_15': 'Юриспруденция',
    '1_3_16': 'Data Science',
}
