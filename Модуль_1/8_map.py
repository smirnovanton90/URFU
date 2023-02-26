#ФУНКЦИЯ MAP
names = ['Ivan', 'Nikita', 'Simon', 'Margarita', 'Vasilisa', 'Kim']

# Создаём пустой список, куда будем заносить результаты
lens_list = []
# Создаём цикл по элементам списка names
for name in names:
    # Вычисляем длину текущего слова
    length = len(name)
    # Добавляем вычисленную длину слова в список
    lens_list.append(length)
 
print(lens_list)
# [4, 6, 5, 9, 8, 3]

# Объявляем функцию для вычисления длины
def get_length(word):
    return len(word)
# Применяем функцию get_length к каждому элементу списка
lens = map(get_length, names)
# Проверим, что переменная lens — это объект типа map:
# Для этого воспользуемся функцией isinstance
print(isinstance(lens, map))
# Будет напечатано:
# True

lens_list = list(map(lambda x: len(x), names))
print(lens_list)

#ЗАДАНИЕ 8.1
docs = [
    '//doc/5041434?query=data%20science',
    '//doc/5041567?query=data%20science',
    '//doc/4283670?query=data%20science',
    '//doc/3712659?query=data%20science',
    '//doc/4997267?query=data%20science',
    '//doc/4372673?query=data%20science',
    '//doc/3779060?query=data%20science',
    '//doc/3495410?query=data%20science',
    '//doc/4308832?query=data%20science',
    '//doc/4079881?query=data%20science'
]
links = list(map(lambda x: "https://www.kommersant.ru" + x, docs))
print (links)

#ФУНКЦИЯ FILTER

#ЗАДАНИЕ 8.2
family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]
def family(*args):
    return list(filter(lambda x: x in family_list, args))

print(family('newborn registration', 'parking permit', 'maternity capital', 'tax benefit', 'medical policy'))

#ЗАДАНИЕ 8.3
reg = [('Ivanov', 'Sergej', 24, 9, 1995),
      ('Smith', 'John', 13, 2, 2003),
      ('Petrova', 'Maria', 13, 3, 2003)]
new_reg_1 = filter(lambda x: x[4] >= 2000, reg)
new_reg = list(map(lambda x: (x[0] + " " + x[1][:1] + ".",x[2],x[3],x[4]), new_reg_1))
print(new_reg)

#ФУНКЦИЯ ZIP

#ЗАДАНИЕ 8.4
def group_gen(n=3):
    while True:
        for i in range(1, n+1):
            yield i
            
users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']

def print_groups(users):
    for user, group in zip(users, group_gen(3)):
        print(user + " in group " + str(group))
        
print_groups(users)