from datetime import datetime
import re


months= ['','січня','лютого','березня','квітня','травня','червня','липня',
'серпня','вересня','жовтня','листопада','грудня',]

numbers = ["", "Перше", "Друге", "Третє", "Четверте", "П´яте", "Шосте", "Сьоме", "Восьме", 
"Дев´яте", "Десяте","Одинадцяте","Дванадцяте", "Тринадцяте", "Чотирнадцяте", "П´ятнадцяте", 
"Шістнадцяте", "Сімнадцяте", "Вісімнадцяте", "Дев´ятнадцяте", "Двадцяте", "Двадцять перше ",
"Двадцять друге", "Двадцять третє","Двадцять четверте","Двадцять п´яте","Двадцять шосте", 
"Двадцять сьоме", "Двадцять восьме", "Двадцять дев´яте", "Тридцяте", "Тридцять перше",
"Тридцять перше", "Тридцять Друге", "Тридцять Третє", "Тридцять Четверте", "Тридцять П´яте",
 "Тридцять шосте", "Тридцять сьоме", "Тридцять Восьме", "Тридцять Дев´яте",]


patterns =[r'\d{2}-\d{2}-\d{4}',
            r'\d{2}.\d{2}.\d{4}',
            r'\d{2}.\d{2}.\d{2}',
            r'\d{2} \d{2} \d{4}',
            r'\d{2} \d{2} \d{2}']


def change_ending(number):
    if number[-1] == 'е':
        return number[:-1] + 'ого'
    return number[:-1] + 'ього'

def replace_day(day_number, date_in_text):
    day = numbers[int(day_number)]
    if date_in_text:
        day = change_ending(day).lower()
    return day

def replace_month(month_number):
    return months[int(month_number)]

def replace_year(year_number):
    _year = numbers[int(year_number[-2:])].lower()
    return 'дві тисячі ' + change_ending(_year) + ' року'



def parse_dates(txt):
    date_line = re.findall(r'|'.join(patterns), txt)
    date_line_check = re.findall(r'[\W\w]?|'.join(patterns), txt)

    for dt, dt_check in zip(date_line, date_line_check):
        date_in_text = True
        if dt == dt_check or dt_check[-1] == '\n':
            date_in_text = False

        splitted_date = dt.replace('.', ' ').replace('-', ' ').split()
        day = replace_day(splitted_date[0], date_in_text)
        month = replace_month(splitted_date[1])
        year = replace_year(splitted_date[2])
        new_date = ' '.join([day, month, year])
        txt =  txt.replace(dt, new_date)
    return txt
