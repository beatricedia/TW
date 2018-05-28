import cx_Oracle
import os
import json


def getLocationFromDB(database_file, user_name):
    conn = cx_Oracle.connect('student/STUDENT@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    person_id = "SELECT ID FROM USERS WHERE USER_NAME='" + user_name + "';"
    cursor.execute(person_id)
    results = cursor.fetchone()
    cursor.close()
    cursor2 = conn.cursor()
    cursor2.execute(
        "SELECT 'makes a migration from '||ORG_LOCATION||' to '|| DEST_LOCATION FROM  LOCATION where ID_USER='" + results[0] + "';")
    results2 = cursor2.fetchone()
    cursor2.close()
    connection.close()
    return results2[0][0]

    # gandeste-te ca trebuie sa apara "userul x a plecat de la origin_loc la dest_loc"
    # verifica mai intai de SQL injection si XSS
