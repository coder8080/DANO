import csv
from datetime import datetime
from math import ceil


def analyze(city):
    def check(city_to_check):
        return city == 'all' or city.lower() == city_to_check.lower()

    file = open('cinema_successful_orders.csv',
                'rt', encoding='utf-8')
    reader = csv.DictReader(file, delimiter=';')
    min_day = datetime(2020, 1, 1, 0, 0, 0).date()

    source = []

    for i, line in enumerate(reader):
        cinema_city = line['cinema_city']
        if not check(cinema_city):
            continue
        price = int(line['ticket_price_in_cu'].split(',')[0])
        if price > 100500:
            print(price)
            continue
        if price < 0:
            print('aaaaaaa')
        date_string = line['session_date']
        date = datetime.strptime(date_string, '%Y-%m-%d').date()
        timepoint = (date - min_day).days
        source.append((timepoint, price))

    weeks = dict()
    source.sort(key=lambda x: x[0])
    result = []

    def add(d: dict, key: any, el: any):
        if key in d:
            d[key].add(el)
        else:
            d[key] = set([el])

    for timepoint, price in source:
        week_number = timepoint // 7
        add(weeks, week_number, price)

    for i in range(len(weeks)):
        if i not in weeks:
            continue
        prices = sorted(weeks[i])
        price = prices[len(prices) // 2]
        result.append((i * 7, price))

    output = open(
        './data_home/result.csv', mode='wt', encoding='utf-8')
    writer = csv.DictWriter(output, fieldnames=(
        '', 'timepoint', 'price',), delimiter=',')
    writer.writeheader()
    writer.writerow({'': i, 'timepoint': timepoint,
                     'price': int(price)})

    for i, (timepoint, price) in enumerate(result):
        writer.writerow({'': i, 'timepoint': timepoint, 'price': price})

    file.close()
    output.close()


if __name__ == '__main__':
    print('Введите город (all для всех городов)')
    city = input()
    analyze(city)

    # current_timepoint = None
    # current_prices = []
    # result = []
    # for i in range(len(source)):
    #     timepoint, price = source[i]
    #     if current_timepoint is None:
    #         current_timepoint = timepoint
    #         current_prices = [price]
    #     elif current_timepoint != timepoint:
    #         pr = current_prices[len(current_prices) // 2]
    #         if pr < 0:
    #             print(timepoint, pr)
    #         result.append(
    #             (current_timepoint, pr))
    #         current_prices = [price]
    #         current_timepoint = timepoint
    #     elif current_timepoint == timepoint:
    #         current_prices.append(price)
