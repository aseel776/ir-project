import mysql.connector
from mysql.connector import Error

def load_docs(indices, dataset_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="ir_docs",
            user="aseel",
            password="1234"
        )

        if conn.is_connected():
            cur = conn.cursor(dictionary=True)
                        
            format_strings = ','.join(['%s'] * len(indices))
            query = f"SELECT * FROM dataset{dataset_id} WHERE id IN ({format_strings})"
            
            cur.execute(query, tuple(indices))
                        
            docs = cur.fetchall()
            return docs

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None
    
    finally:
        if (conn.is_connected()):
            cur.close()
            conn.close()