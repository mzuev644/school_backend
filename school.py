
import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(dbname='school', user='postgres', password='ukr997u', host='localhost', port='5432')

# Создание курсора
cursor = conn.cursor()


# Функция для выбора таблицы
def select_table():
    while True:
        print("Выберите имя таблицы:")
        print("1. Ученики")
        print("2. Учителя")
        print("3. Оценки")
        print("4. Расписание")
        print("5. Классы")
        print("6. Предметы")
        print("7. Классные руководители")
        print("8. Предметы учителей")
        print("9. Назад")
        table = input("Введите номер таблицы: ")

        if table == '1':
            return 'student'
        elif table == '2':
            return 'teacher'
        elif table == '3':
            return 'grade'
        elif table == '4':
            return 'schedule'
        elif table == '5':
            return 'class'
        elif table == '6':
            return 'subject'
        elif table == '7':
            return 'class_leader'
        elif table == '8':
            return 'subject_list'
        elif table == '9':
            return select_table()
        else:
            print("Неверный ввод. Попробуйте еще раз.")


# Функция для изменения записи
def update(table):
    try:
        column = input("Введите название столбца с PK, который хотите изменить: ")
        record_id = int(input("Введите ID записи, которую хотите изменить: "))
        column_name = input("Введите имя столбца, который хотите изменить: ")
        new_value = input("Введите новое значение: ")
        query = f"UPDATE public.{table} SET {column_name} = '{new_value}' WHERE {column} = {record_id}"
        cursor.execute(query)
        conn.commit()
        print("Запись успешно изменена!")
    except:
        print("Неверный ввод. Попробуйте еще раз.")
    # Здесь можно добавить код для изменения записи в базе данных


# Функция для удаления записи
def delete(table):
    column = input("Введите название столбца с PK, который хотите удалить: ")
    record_id = int(input("Введите ID записи, которую хотите удалить: "))
    query = f"DELETE FROM public.{table} WHERE {column} = {record_id}"
    cursor.execute(query)
    conn.commit()
    print("Запись успешно удалена!")


# Функция для вывода таблицы
def read(table):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM public.{table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# Функция для добавления записи
def create(table):
    try:
        columns = input("Введите названия столбцов через запятую: ")
        values = input("Введите значения через запятую: ")
        query = f"INSERT INTO public.{table} ({columns}) VALUES ({values})"
        cursor.execute(query)
        conn.commit()
        print("Запись успешно добавлена!")
    except:
        print("Неверный ввод. Попробуйте еще раз.")
    pass


# Основной цикл программы
while True:
    table_name = select_table()
    while True:
        print("Выберите действие:")
        print("1 - изменить запись")
        print("2 - удалить запись")
        print("3 - вывести таблицу")
        print("4 - добавить запись")
        print("5 - вернуться к выбору таблицы")
        action = input("Введите номер: ")
        if action == '1':
            update(table_name)
        elif action == '2':
            delete(table_name)
        elif action == '3':
            read(table_name)
        elif action == '4':
            create(table_name)
        elif action == '5':
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")
    return_to_table = input("Вернуться к выбору таблицы? (да/нет): ")
    if return_to_table.lower() != 'да':
        break

# Закрытие соединения с базой данных
conn.close()
