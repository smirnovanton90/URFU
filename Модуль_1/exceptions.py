try:
    a = int(input("Enter a number (Введите число): "))
    print("You entered ", a, " (Вы ввели ", a, ")")
except ValueError as e:
    print("You entered a wrong number (Вы ввели неправильное число)")
else:
    print("You entered a right number (Вы ввели правильное число")
finally:
    print("Exit (Выход из программы)")
