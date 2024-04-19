import sqlite3


def convert_to_binary_data(filename):
    """Преобразование данных в двоичный код"""
    with open(filename, "rb") as file:
        blob_data = file.read()
    return blob_data


def insert_blob(id, name, photo):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO data_theory
                                  (id, name, photo) VALUES (?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        # Преобразование данных в формат кортежа
        data_tuple = (id, name, emp_photo)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблиу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    try:
        with open(filename, 'wb') as file:
            file.write(data)
        print("Данные из blob сохранены в: ", filename, "\n")

    except Exception as ex:
        print(f"ERROR {ex}")


def read_blob_data(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from data_theory"""
        cursor.execute(sql_fetch_blob_query)
        record = cursor.fetchall()
        for row in record:
            print("Id =", row[0], "Name =", row[1])
            name = row[1]
            photo = row[2]
            print("Сохранение изображения сотрудника на диске \n")

            photo_path = f"{name}.jpg"
            write_to_file(photo, photo_path)

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


read_blob_data(1)
read_blob_data(2)

# insert_blob(1, "koala", "Koala.jpg")
# insert_blob(2, "house", "Lighthouse.jpg")
