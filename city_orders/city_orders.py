file = open('city_orders/city_orders.txt', 'rt', encoding='utf-8')
output = open('city_orders/result.txt', 'wt', encoding='utf-8')

result = []

for line in file.readlines():
    *city, count = line.split()
    city = ' '.join(city)
    count = int(count)
    result.append((city, count))

result.sort(key=lambda x: x[1], reverse=True)
print(*map(lambda x: x[0], result[:5]), sep='\n', file=output)
