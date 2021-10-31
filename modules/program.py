import main.py as m
import task1.py as task1

# Конфигурируем программу добавляя задачи в список
# В каждой задаче настраиваем ввод, вывод, исполняющую функцию и тип ожидаемых данных от пользователя
# Последовательноть выволнения задач будет в соответствии со списком tasks 
# Если необходимо, то список можно сортировать, так как номера задач весьма условны
# Сортировка внутри кортежа (одной задачи), недопустима!

tasks = list()
tasks.append(({"def":task1.Func}))
'''tasks.append(({"in":"Введите список, например: [1,2,4,6,3] : ", "out":"Результат = {0}", "def":ForTask2, "type": str}))
tasks.append(({"in":"Введите номер месяца: ", "out":"Время года = {0}", "def":ForTask3, "type": int}))
tasks.append(({"in":"Введите несколько слов: ", "def":ForTask4, "type": str}))
tasks.append(({"in":"Введите натуральное число (новый элемент рейтинга): ", "out":"Результат = {0}", "def":ForTask5, "type": int}))
task_6=(
    ({"out":"Добавление товара в программу..."}),
    ({"in":"Введите название: ", "def":ForTask6_1, "type": str}),
    ({"in":"Введите цену: ", "def":ForTask6_2, "type": {int,float}}),
    ({"in":"Введите количество: ", "def":ForTask6_3, "type": {int,float}}),
    ({"in":"Введите eдицину измерения: ", "out":"Товар добавлен: {0}", "def":ForTask6_4, "type": str}),
    ({"in":"Введите 'yes' или 'y', чтобы продолжить добавление товаров, а для аналитики нажмите Enter: ", "def":ForTask6_5, "type": str}))
tasks.append(task_6)'''

# Основной цикл
while True:
    # Основная функция
    m.main(tasks)
    value = input("Введите 'yes' или 'y', чтобы повторить программу, а для выхода нажмите Enter: ")
    if value != 'y' and value != 'yes':
        break

print("Завершение программы")
