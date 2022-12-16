import csv
from datetime import datetime
from math import ceil

# GENRES = ['triller', 'military', 'action', 'biographical', 'fairy_tale', 'science', 'fantasy', 'historical', 'drama', 'animation', 'cartoon', 'documentary', 'adventure',
#           'fiction', 'childish', 'horror', 'humor', 'western', 'noir', 'detective', 'biography', 'criminal', 'tragicomedy', 'biopic', 'mystic', 'family', 'comedy', 'arthouse']


def analyze(city):
    def check(city_to_check):
        return city == 'all' or city.lower() == city_to_check.lower()

    file = open('cinema_successful_orders.csv',
                'rt', encoding='utf-8')
    reader = csv.DictReader(file, delimiter=';')

    before_orders = [0] * 7
    during_orders = [0] * 7
    after_orders = [0] * 7

    min_day = (100500, 0, 0)
    max_day = (-100500, 0, 0)

    for line in reader:
        cinema_city = line['cinema_city']
        if not check(cinema_city):
            continue
        date_string = line['session_date']
        date = datetime.strptime(date_string, '%Y-%m-%d')
        month = date.month
        day = date.day
        year = date.year
        weekday = date.weekday()
        type = 'none'

        cort = (year, month, day)
        if cort < min_day:
            min_day = cort
        if cort > max_day:
            max_day = cort

        if year != 2020:
            if year < 2020:
                type = 'before'
            elif year > 2020:
                type = 'after'
        else:
            if month > 3 and month < 6:
                type = 'during'
            elif month == 3:
                if day >= 10:
                    type = 'during'
                else:
                    type = 'before'
            elif month == 6:
                if day > 23:
                    type = 'after'
                else:
                    type = 'during'
            elif month < 3:
                type = 'before'
            elif month > 6:
                type = 'after'
        if type == 'before':
            before_orders[weekday] += 1
        elif type == 'during':
            during_orders[weekday] += 1
        elif type == 'after':
            after_orders[weekday] += 1
        else:
            print('unknown type', month, day, year)
            raise ValueError('unknown type')
    file.close()

    first_day = datetime(*min_day, 0, 0, 0).date()
    start_day = datetime(2020, 3, 10, 0, 0, 0).date()
    last_day = datetime(*max_day, 0, 0, 0).date()
    end_day = datetime(2020, 6, 23, 0, 0, 0).date()
    days_before = (start_day - first_day).days
    days_during = (end_day - start_day).days
    days_after = (last_day - end_day).days
    weeks_before = ceil(days_before / 7)
    weeks_during = ceil(days_during / 7)
    weeks_after = ceil(days_after / 7)

    # print(weeks_before, weeks_during, weeks_after)
    return before_orders, during_orders, after_orders, weeks_before, weeks_during, weeks_after


def save(before_orders, during_orders, after_orders, weeks_before, weeks_during, weeks_after):
    # before
    output_before = open(
        './data_home/before.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_before, fieldnames=(
        '', 'weekday', 'count',), delimiter=',')
    writer.writeheader()
    for i, count in enumerate(before_orders):
        writer.writerow(
            {"": i, 'weekday': i, 'count': ceil(count / weeks_before)})
    output_before.close()

    # during
    output_during = open(
        './data_home/during.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_during, fieldnames=(
        '', 'weekday', 'count',), delimiter=',')
    writer.writeheader()
    for i, count in enumerate(during_orders):
        writer.writerow(
            {"": i, 'weekday': i, 'count': ceil(count / weeks_during)})
    output_during.close()

    # after
    output_after = open('./data_home/after.csv',
                        mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_after, fieldnames=(
        '', 'weekday', 'count'), delimiter=',')
    writer.writeheader()
    for i, count in enumerate(after_orders):
        writer.writerow(
            {"": i, 'weekday': i, 'count': ceil(count / weeks_after)})
    output_after.close()


def generate_files(city):
    result = analyze(city)
    save(*result)


if __name__ == '__main__':
    print('Введите город (all для всех городов)')
    city = input()
    generate_files(city)
