import csv
from datetime import datetime
from math import ceil

# GENRES = ['triller', 'military', 'action', 'biographical', 'fairy_tale', 'science', 'fantasy', 'historical', 'drama', 'animation', 'cartoon', 'documentary', 'adventure',
#           'fiction', 'childish', 'horror', 'humor', 'western', 'noir', 'detective', 'biography', 'criminal', 'tragicomedy', 'biopic', 'mystic', 'family', 'comedy', 'arthouse']


def analyze():
    def increase(d: dict, key: str):
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    file = open('cinema_successful_orders.csv',
                'rt', encoding='utf-8')
    reader = csv.DictReader(file, delimiter=';')

    before_films = dict()
    during_films = dict()
    after_films = dict()

    min_day = (100500, 0, 0)
    max_day = (-100500, 0, 0)

    for line in reader:
        movie_name = line['movie_name']
        date_string = line['session_date']
        date = datetime.strptime(date_string, '%Y-%m-%d')
        month = date.month
        day = date.day
        year = date.year
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
            increase(before_films, movie_name)
        elif type == 'during':
            increase(during_films, movie_name)
        elif type == 'after':
            increase(after_films, movie_name)
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
    # weeks_before = ceil(days_before / 7)
    # weeks_during = ceil(days_during / 7)
    # weeks_after = ceil(days_after / 7)

    # print(first_day)
    # print(start_day)
    # print(end_day)
    # print(last_day)

    c = 5

    top_films_before = sorted(before_films.items(),
                              key=lambda x: x[1], reverse=True)[:c]
    top_films_during = sorted(during_films.items(),
                              key=lambda x: x[1], reverse=True)[:c]
    top_films_after = sorted(
        after_films.items(), key=lambda x: x[1], reverse=True)[:c]
    t = 40
    print(len(list(filter(lambda x: x[1] > t, before_films.items()))))
    print(len(list(filter(lambda x: x[1] > t, during_films.items()))))
    print(len(list(filter(lambda x: x[1] > t, after_films.items()))))

    # print(weeks_before, weeks_during, weeks_after)
    return top_films_before, top_films_during, top_films_after


def save(top_films_before, top_films_during, top_films_after):
    # before
    output_before = open(
        './data_home/before.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_before, fieldnames=(
        '', 'movie', 'count',), delimiter=',')
    writer.writeheader()
    for i, (movie, count) in enumerate(top_films_before):
        writer.writerow({"": i, 'movie': movie, 'count': count})
    output_before.close()

    # during
    output_during = open(
        './data_home/during.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_during, fieldnames=(
        '', 'movie', 'count',), delimiter=',')
    writer.writeheader()
    for i, (movie, count) in enumerate(top_films_during):
        writer.writerow(
            {"": i, 'movie': movie, 'count': count})
    output_during.close()

    # after
    output_after = open('./data_home/after.csv',
                        mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output_after, fieldnames=(
        '', 'movie', 'count'), delimiter=',')
    writer.writeheader()
    for i, (movie, count) in enumerate(top_films_after):
        writer.writerow(
            {"": i, 'movie': movie, 'count': count})
    output_after.close()


def generate_files():
    # save(*analyze())
    analyze()


if __name__ == '__main__':
    generate_files()
