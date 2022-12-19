import csv
from datetime import datetime
from math import ceil


# days = ['понедельник', 'вторник', 'среда',
#         'четверг', 'пятница', 'суббота', 'воскресенье']


def analyze(city):
    def check(city_to_check):
        return city == 'all' or city.lower() == city_to_check.lower()

    file = open('cinema_successful_orders.csv',
                'rt', encoding='utf-8')
    reader = csv.DictReader(file, delimiter=';')

    weeks_after = dict()
    weeks_before = dict()
    min_day = datetime(2020, 1, 1, 0, 0, 0).date()

    for line in reader:
        cinema_city = line['cinema_city']
        if not check(cinema_city):
            continue
        date_string = line['session_date']
        date = datetime.strptime(date_string, '%Y-%m-%d').date()
        timepoint = (date - min_day).days
        week_number = timepoint // 7 + 1
        if week_number < 11:
            if week_number not in weeks_before:
                weeks_before[week_number] = {'workdays': 0, 'weekend': 0}
            weekday = date.weekday()
            if weekday > 4:
                weeks_before[week_number]['weekend'] += 1
            else:
                weeks_before[week_number]['workdays'] += 1
        elif week_number >= 27:
            if week_number not in weeks_after:
                weeks_after[week_number] = {'workdays': 0, 'weekend': 0}
            weekday = date.weekday()
            if weekday > 4:
                weeks_after[week_number]['weekend'] += 1
            else:
                weeks_after[week_number]['workdays'] += 1

    file.close()

    # print(weeks_before, weeks_during, weeks_after)
    return weeks_before,  weeks_after


def save(weeks_before, weeks_after):
    # before
    output_before = open(
        './data_home/before.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_before, fieldnames=(
        '', 'week', 'percent',), delimiter=',')
    writer.writeheader()
    items = list(weeks_before.items())
    items.sort(key=lambda x: x[0])
    for week_number, data in items:
        s = data['workdays'] + data['weekend']
        percent = round(data['weekend'] / data['workdays'] * 250)
        writer.writerow(
            {"": week_number, 'week': week_number, 'percent': percent})
    output_before.close()

    # after
    output_after = open(
        './data_home/after.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_after, fieldnames=(
        '', 'week', 'percent',), delimiter=',')
    writer.writeheader()
    items = list(weeks_after.items())
    items.sort(key=lambda x: x[0])
    for week_number, data in items:
        s = data['workdays'] + data['weekend']
        percent = round(data['weekend'] / data['workdays'] * 250)
        writer.writerow(
            {"": week_number, 'week': week_number, 'percent': percent})
    output_after.close()


def generate_files(city: str):
    save(*analyze(city))


if __name__ == '__main__':
    print('Введите город (all для всех городов)')
    city = input().lower()
    generate_files(city)
