# task1
# god = input("Введите год: ")
# if god.isdigit():
#     god = int(god)
    
#     f_year = god % 4
#     if f_year == 0:
#         print('Год является високосным')
#     else:
#         print('Год не является високосным')

# else:
#     print("Введите пожалуйста год")


# task2
# a = input("Ввдите число: ")
# given_number = a

# if given_number.isdigit():
#     given_number = int(given_number)
    
#     if given_number % 3 == 0 and given_number % 5 == 0:
#         print("HahaHoo")
#     elif given_number % 3 == 0:
#         print("Haha")
#     elif given_number % 5 == 0:
#         print("Hoo")
#     elif given_number % 3 != 0 and given_number % 5 != 0:
#         print("Aaaaa")

# else:
#     print("Введите число пж")


# task3
# f = input("первое число: ")
# s = input("второе число: ")
# if f.isdigit() and s.isdigit():
#     f = int(f)
#     s = int(s)
    
#     plus = f + s
#     if plus > 5:
#         print("Сумма чисел больше 5")
#     elif plus < 5:
#         print("Сумма чисел меньше 5")

# else:
#     print("введи число")



# task5                                     
# num = input("Введите число: ")

# if num.isdigit():                         # с isdigit почему то не работают отрицательные числа
#     num = int(num)
#     if num >= 1:
#         print("1")
#     elif num == 0:
#         print("0")
#     elif num < 0:
#         print("-1")
# else:
#     print("Введите число пж.")

# а без него все работает, только надо вводить числа, пример снизу

# num = int(input("Введите число: "))
# if num >= 1:
#     print("1")
# elif num == 0:
#     print("0")
# elif num < 0:
#     print("-1")




# task6
# slovo = input("введите слово: ")
# bukva = input("введите букву: ")
# if slovo.count(bukva) == 1:
#     print(f"индекс подстроки {slovo.find(bukva)}.")
# elif slovo.count(bukva) >= 2:
#     print(f"индекс первого вхождения {slovo.find(bukva)}, индекс последнего вхождения {slovo.rfind(bukva)}")


# task7
# a = input("введите атора: ").title()
# books = {"Джек Лондон": "Зов природы", "Стивен Кинг": "Темная башня", "Никколо Макиавелли": "Государь"}

# if a in books:
#     print(f"Название книги: {books[a]}")
# elif a not in books:
#     print("назовите книгу: ")
#     naz = input().capitalize()
#     books[a] = naz
#     print(books)
