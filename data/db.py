import sqlite3


def convert_to_binary_data(filename):
    """Преобразование данных в двоичный код"""
    with open(filename, "rb") as file:
        blob_data = file.read()
    return blob_data


def insert_blob(id, practice_file, theory_file, answer_file, URL):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO data_theory
                                  (id, practice_file, theory_file, answer_file, URL) VALUES (?, ?, ?, ?, ?)"""

        data_tuple = (id, practice_file, theory_file, answer_file, URL)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def write_to_file(data, filename):
    """Преобразование двоичных данных в нужный формат"""
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

# read_blob_data(1)
# read_blob_data(2)

# insert_blob(1, r"D:\MatematikBot\db\practice\Uslovia_prototipov_1.pdf", r"D:\MatematikBot\db\theory\tutorial1.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_1.pdf", r"https://www.youtube.com/watch?v=axMFeOWP6x8")
# insert_blob(2, "------------------------None------------------------", r"D:\MatematikBot\db\theory\tutorial2.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_2.pdf", r"https://www.youtube.com/watch?v=AwfzAV-EKHI&t=1584s")
# insert_blob(3, r"D:\MatematikBot\db\practice\Uslovia_prototipov_3.pdf", r"D:\MatematikBot\db\theory\tutorial3.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_3.pdf", r"https://www.youtube.com/watch?v=FN_uKR1snA8&t=322s")
# insert_blob(4, r"D:\MatematikBot\db\practice\Uslovia_prototipov_4.pdf", r"D:\MatematikBot\db\theory\tutorial4.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_4.pdf", r"https://www.youtube.com/watch?v=0aGIDlgzHCU")
#
# insert_blob(5, r"D:\MatematikBot\db\practice\Uslovia_prototipov_5.pdf", r"D:\MatematikBot\db\theory\tutorial5.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_5.pdf", r"https://www.youtube.com/watch?v=0aGIDlgzHCU")
# insert_blob(6, r"D:\MatematikBot\db\practice\Uslovia_prototipov_6.pdf", r"D:\MatematikBot\db\theory\tutorial6.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_6.pdf", r"https://www.youtube.com/watch?v=o9BKCYEKrb8")
# insert_blob(7, r"D:\MatematikBot\db\practice\Uslovia_prototipov_7.pdf", r"D:\MatematikBot\db\theory\tutorial7.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_7.pdf", r"https://www.youtube.com/watch?v=taaneALeK4o")
# insert_blob(8, r"D:\MatematikBot\db\practice\Uslovia_prototipov_8.pdf", r"D:\MatematikBot\db\theory\tutorial8.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_8.pdf", r"https://www.youtube.com/watch?v=tIWOcXSm2rU")
#
# insert_blob(9, r"D:\MatematikBot\db\practice\Uslovia_prototipov_9.pdf", r"D:\MatematikBot\db\theory\tutorial9.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_9.pdf", r"https://www.youtube.com/watch?v=206GuftFyU0")
# insert_blob(10, r"D:\MatematikBot\db\practice\Uslovia_prototipov_10.pdf", r"D:\MatematikBot\db\theory\tutorial10.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_10.pdf", r"https://www.youtube.com/watch?v=oRWQtlPOyww")
# insert_blob(11, r"D:\MatematikBot\db\practice\Uslovia_prototipov_11.pdf", r"D:\MatematikBot\db\theory\tutorial11.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_11.pdf", r"https://www.youtube.com/watch?v=F-i-BWY3fwo")
# insert_blob(12, r"D:\MatematikBot\db\practice\Uslovia_prototipov_12.pdf", r"D:\MatematikBot\db\theory\tutorial12.pdf",
#             r"D:\MatematikBot\db\answer\Otvety_prototipov_12.pdf", r"https://www.youtube.com/watch?v=tIWOcXSm2rU")
