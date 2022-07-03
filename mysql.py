
# enter your server IP address/domain name
HOST = "blind.local" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "blind"
# this is the user you create
USER = "1_blind"
# user password
PASSWORD = "blind"
# connect to MySQL server
# Module Imports
import mariadb
import sys

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
def delete(name):
 
# Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=3306,
            database=DATABASE
            )
        cursor = conn.cursor()
        sql_insert_blob_query = """ DELETE FROM face WHERE
                            name=%s"""

        DEL = (name,)
        result = cursor.execute(sql_insert_blob_query, DEL)
        conn.commit()
     
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return 1
        
    finally:
        return 0
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
        return 0

def upload(name,filename):
    photo = filename
    print(photo,name)
# Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=3306,
            database=DATABASE
            )
        cursor = conn.cursor()
        sql_insert_blob_query = """ INSERT INTO face
                            (name, image) VALUES (%s,%s)"""

        empPicture = convertToBinaryData(photo)
        # Convert data into tuple format
        insert_blob_tuple = (name, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        conn.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return 1

    finally:
        
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
        return 0

