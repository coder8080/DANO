import csv

file = open('cinema_successful_orders.csv', 'rt', encoding='utf-8')
reader = csv.DictReader(file, delimiter=';')
result = dict()
for line in reader:
    if line['genre_is_triller'] != '1,0':
        continue
    name = line['movie_name']
    if name in result:
        result[name] += 1
    else:
        result[name] = 1

best = sorted(result.items(), key=lambda x: x[1], reverse=True)[:5]
print(best, sep='\n')
