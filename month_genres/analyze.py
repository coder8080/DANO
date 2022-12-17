import csv
from datetime import datetime
from math import ceil

GENRES = ['triller', 'military', 'action', 'biographical', 'fairy_tale', 'science', 'fantasy', 'historical', 'drama', 'animation', 'cartoon', 'documentary', 'adventure',
          'fiction', 'childish', 'horror', 'humor', 'western', 'noir', 'detective', 'biography', 'criminal', 'tragicomedy', 'biopic', 'mystic', 'family', 'comedy', 'arthouse']

before = dict()
during = dict()
after = dict()


def get_genre_by_line(line):
    for genre_name in GENRES:
        if line[f'genre_is_{genre_name}'] == '1,0':
            return genre_name
    else:
        pass
        # print('жанр не найден')


def analyze():

    file = open('cinema_successful_orders.csv',
                'rt', encoding='utf-8')
    reader = csv.DictReader(file, delimiter=';')

    before_orders = dict()
    during_orders = dict()
    after_orders = dict()

    for line in reader:
        genre = get_genre_by_line(line)
        if not genre:
            continue

        date_string = line['session_date']
        date = datetime.strptime(date_string, '%Y-%m-%d')
        month = date.month
        day = date.day
        year = date.year
        weekday = date.weekday()
        type = 'none'

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
            if genre in before_orders:
                before_orders[genre] += 1
            else:
                before_orders[genre] = 1
        elif type == 'during':
            if genre in during_orders:
                during_orders[genre] += 1
            else:
                during_orders[genre] = 1
        elif type == 'after':
            if genre in after_orders:
                after_orders[genre] += 1
            else:
                after_orders[genre] = 1
        else:
            print('unknown type', month, day, year)
            raise ValueError('unknown type')
    file.close()
    return before_orders, during_orders, after_orders


def save(before_orders, during_orders, after_orders):
    # before
    output_before = open(
        './data_home/before.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_before, fieldnames=(
        '', 'genre', 'count',), delimiter=',')
    writer.writeheader()
    s = sum(map(lambda x: x[1], before_orders.items()))
    best = sorted(before_orders.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (genre, count) in enumerate(best):
        writer.writerow(
            {"": i, 'genre': genre, 'count': ceil(count / s * 100)})
    output_before.close()

    # during
    output_during = open(
        './data_home/during.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_during, fieldnames=(
        '', 'genre', 'count',), delimiter=',')
    writer.writeheader()
    s = sum(map(lambda x: x[1], during_orders.items()))
    best = sorted(during_orders.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (genre, count) in enumerate(best):
        writer.writerow(
            {"": i, 'genre': genre, 'count': ceil(count / s * 100)})
    output_during.close()

    # after
    output_after = open('./data_home/after.csv',
                        mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_after, fieldnames=(
        '', 'genre', 'count'), delimiter=',')
    writer.writeheader()
    s = sum(map(lambda x: x[1], after_orders.items()))
    best = sorted(after_orders.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (genre, count) in enumerate(best):
        writer.writerow(
            {"": i, 'genre': genre, 'count': ceil(count / s * 100)})
    output_after.close()


def generate_files():
    save(*analyze())


if __name__ == '__main__':
    generate_files()
