import cx_Oracle
import os
import json


def getFname(database_file, user_name):
    conn = cx_Oracle.connect('student/STUDENT@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    cursor.execute("SELECT FIRST_NAME FROM  USERS where USER_NAME='" + user_name + "';")
    results = cursor.fetchone()
    cursor.close()
    return results[0]


def getLname(database_file, user_name):
    conn = cx_Oracle.connect('student/STUDENT@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    cursor.execute(
        "SELECT LAST_NAME FROM  USERS where USER_NAME='" + user_name + "';")
    results = cursor.fetchone()
    cursor.close()
    return results[0]


def getContry(database_file, user_name):
    conn = cx_Oracle.connect('student/STUDENT@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    cursor.execute(
        "SELECT COUNTRY FROM  USERS where USER_NAME='" + user_name + "';")
    results = cursor.fetchone()
    cursor.close()
    return results[0]


def getCity(database_file, user_name):
    conn = cx_Oracle.connect('student/STUDENT@localhost:1521')
    cursor = conn.cursor()
    print(cursor)
    cursor.execute(
        "SELECT CITY FROM  USERS where USER_NAME='" + user_name + "';")
    results = cursor.fetchone()
    cursor.close()
    return results[0]

# verifica mai intai de SQL injection si XSS
