#ЗАДАНИЕ 6.1 (НА САМОПРОВЕРКУ)
def get_length(a):
    return len(a)

new_list = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
new_list.sort(key=get_length)
print(new_list)


#Сортировка по нескольким признакам
new_list2 = ['bbb', 'ababa','aaa', 'aaaaa',  'cc']
new_list2.sort(key = lambda word: (len(word), word))
print(new_list2)


#ЗАДАНИЕ 6.3
hyp = lambda a, b: (a**2 + b**2)**(1/2)
print(hyp(3,4))
print(hyp(1,9))


#ЗАДАНИЕ 6.4
def sort_sides (l_in):
    l_in.sort(key = lambda b: (b[0]**2 + b[1]**2)**(1/2))
    return l_in
    
print(sort_sides([(3,4), (1,2), (10,10)]))
