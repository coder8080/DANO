import csv

file = open('cinema_successful_orders.csv',
            'rt', encoding='utf-8')
reader = csv.DictReader(file, delimiter=';')

films = dict()


def increase(d: dict, name: str):
    if name in d:
        d[name] += 1
    else:
        d[name] = 1


for line in reader:
    name = line['movie_name']
    increase(films, name)

result = sorted(films.items(), key=lambda x: x[1])[:10]

c = 0

for l in result:
    if l[1] > 1:
        break
    else:
        c += 1
print(*result, sep='\n')
print(c)
