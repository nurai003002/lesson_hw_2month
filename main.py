# import sqlite3

# def create_connection(db_name):
#     connection = sqlite3.connect(db_name)
#     return connection
# create_connection("schedule.db")


# def create_table(conn, sql):
#     cursor = conn.cursor()
#     cursor.execute(sql)


# def create_lessons(conn, lesson: tuple):
#     sql = """ INSERT INTO lesssons
#     (lesson_title, time, opinion)
#     VALUES (?,?,?);
# """
#     cursor = conn.cursor
#     cursor.execute(sql, lesson)
#     conn.commit()

# sql_create_table = """
# CREATE TABLE IF NOT EXISIS lessons(
# id INTEDER PRIMARY KEY AUTOINCREMENT,
# lesson_title TEXT NOT FAULT,
# time DOUBLE (4, 2) NOT NULL DEFAULT 0.0
# opinion TEXT DEFAULT NULL
# )
# """
# connection = create_connection("schedule.db")
# if connection:
#     print("Conect")
#     create_table(connection, sql_create_table)
#     create_lessons(connection, ("Английский", 11.30, "Интересный"))



