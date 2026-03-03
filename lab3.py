input_data = input("Введіть елементи списку через пробіл: ")
my_list = input_data.split()

print("Початковий список:", my_list)
target_value = input("Введіть значення елемента, який потрібно видалити: ")
if target_value in my_list:
    while target_value in my_list:
        my_list.remove(target_value)
    message = f"Елемент '{target_value}' успішно видалено."
else:
    message = f"Елемент '{target_value}' не знайдено у списку."

print(message)
print("Оновлений список:", my_list)