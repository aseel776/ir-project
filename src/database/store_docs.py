import mysql.connector
from mysql.connector import Error

def store_docs_in_dataset1(docs):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="ir_docs",
            user="aseel",
            password="1234",
        )

        if conn.is_connected():
            cur = conn.cursor()
            
            count = 0
            for doc in docs:
                cur.execute(
                    "INSERT INTO dataset1 (id, doc_id, title, text) VALUES (%s, %s, %s, %s)", 
                    (count, doc['id'], doc['title'], doc['text'])
                )
                count = count + 1
            
            conn.commit()
            cur.close()
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if (conn.is_connected()):
            conn.close()

def store_docs_in_dataset2(docs):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="ir_docs",
            user="aseel",
            password="1234"
        )

        if conn.is_connected():
            cur = conn.cursor()
            
            count = 0
            for doc in docs:
                cur.execute(
                    "INSERT INTO dataset2 (id, doc_id, text) VALUES (%s, %s, %s)", 
                    (count, doc['id'], doc['text'])
                )
                count = count + 1
            
            conn.commit()
            cur.close()
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if (conn.is_connected()):
            conn.close()
