limit = 100

# Створюємо словники для добутків та сум
products = {}
sums = {}

# Знаходимо усі можливі добутки та суми
for x in range(2, limit):
    for y in range(x + 1, limit):
        prod = x * y
        summ = x + y
        
        if prod not in products:
            products[prod] = [(x, y)]
        else:
            products[prod].append((x, y))
        
        if summ not in sums:
            sums[summ] = [(x, y)]
        else:
            sums[summ].append((x, y))

# Фільтруємо добутки, які зустрічаються лише один раз
non_unique_products = {k: v for k, v in products.items() if len(v) > 1}

# Суми, де S міг би сказати Я був впевнений, що ти їх не вгадаєш
non_unique_sums = []
for sum in sums.values():
    is_all_non_unique = True
    if len(sum) < 2:
        continue
    for pair in sum:
        n = non_unique_products.keys()
        if pair[0] * pair[1] not in n:
            is_all_non_unique = False
    if is_all_non_unique:
        non_unique_sums.append(sum[0][0]+sum[0][1])

#Добутки, де P міг би сказати «Тоді, я їх знаю.»
possible_products = []
for product in non_unique_products.values():
    count = 0
    possible_answer = (0,0)
    for pair in product:
        if pair[0] + pair[1] in non_unique_sums:
            count +=1
            possible_answer = (pair[0], pair[1])
    if count == 1:
        possible_products.append(possible_answer[0] * possible_answer[1])

#Сума, де S може сказати «Якщо ти можеш їх вгадати, то і я їх знаю.»
result = []
for sum in [sums[key] for key in non_unique_sums]:
    count = 0
    possible_answer = (0,0)
    for pair in sum:
        if pair[0] * pair[1] in possible_products:
            count += 1
            possible_answer = (pair[0], pair[1])
    if count == 1:
        result.append((possible_answer[0], possible_answer[1]))

print(result)