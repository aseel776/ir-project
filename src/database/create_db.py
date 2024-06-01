import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        database="ir_docs",
        user="aseel",
        password="1234",
    )

    if conn.is_connected():
        cur = conn.cursor()

        cur.execute('DROP TABLE dataset1')
        cur.execute('DROP TABLE dataset2')

        # Create table dataset1
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS dataset1 (
                id INT PRIMARY KEY,
                doc_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                text TEXT NOT NULL
            )
            '''
        )

        # Create table dataset2
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS dataset2 (
                id INT PRIMARY KEY,
                doc_id INTEGER NOT NULL,
                text TEXT NOT NULL
            )
            '''
        )

        conn.commit()

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (conn.is_connected()):
        cur.close()
        conn.close()
