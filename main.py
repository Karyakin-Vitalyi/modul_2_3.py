# Домашняя работа "Стиль кода часть II. Цикл While"
# Записываем исходный список в переменную my_list
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Начинаем цикл while
index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break  # Прерываем цикл, если встретилось отрицательное число
    elif my_list[index] == 0:
        index += 1
        continue  # Пропускаем ноль и переходим к следующему элементу
    else:
        print(my_list[index])  # Выводим положительное число
        index += 1

print("Цикл завершен")