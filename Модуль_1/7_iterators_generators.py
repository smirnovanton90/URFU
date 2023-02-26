#ИТЕРАТОРЫ

new_list = [12, 14, 16]
print(new_list)

iter_list = iter(new_list) 
print(iter_list)
print(next(iter_list))
print(next(iter_list))


users = ['admin', 'user']
iter_users = iter(users)
while True:
    # Создаём блок обработки исключений
    try:
        # Выводим следующий объект из итератора
        print(next(iter_users))
   # Отлавливаем исключение StopIteration
    except StopIteration:
        # Когда возникает исключение, выводим фразу на экран
        print("User list is over!")
        # Завершаем цикл
        break


for user in iter_users:
    # Выводим текущий элемент на экран
    print(user)

#ГЕНЕРАТОРЫ

# Объявляем функцию для расчёта суммы вклада
def deposit(money, interest):
    # Процент по вкладу преобразуем во множитель:
    # делим процент на 100 и прибавляем 1
    interest = interest/100 + 1
    # Создаём бесконечный цикл
    while True:
        # Сумма вклада через год — это
        # текущая сумма, умноженная на коэффициент
        # и округлённая до двух знаков после запятой
        money = round(interest * money, 2)
        # Выдаём полученную сумму вклада
        yield money
        
bank = deposit(1000, 5)

print(next(bank)) # Запускаем генератор bank в первый раз
print(next(bank)) # Запускаем генератор bank во второй раз
print(next(bank)) # Запускаем генератор bank в третий раз


#ЗАДАНИЕ 7.7
def inf_iter(l):
    l_iter = iter(l)
    while True:
        try:
            yield next(l_iter)
        except StopIteration as e:
            l_iter = iter(l)
            yield next(l_iter)

l = [101, 102, 103]
gen = inf_iter(l)
for _ in range(10):
    print(next(gen))
    
#ЗАДАНИЕ 7.8
def group_gen(n):
    r = range(n + 1)[1:]
    n_iter = iter(r)
    while True:
        try:
            yield next(n_iter)
        except StopIteration as e:
            n_iter = iter(r)
            yield next(n_iter)
            
            
groups = group_gen(3)
for _ in range(10):
    print(next(groups))
