populations = {'Нью-Йорк': 8398748, 'Лос-Анджелес': 3990456, 'Чикаго': 2705994,
                        'Хьюстон': 2325502, 'Феникс': 1660272,'Филадельфия': 1584138}
largest = {}
for k, v in populations.items():
    if v > 2000000: largest[k] = v
print(largest)
print()
largest = {k : v for k, v in populations.items() if v > 2000000}
print(largest)