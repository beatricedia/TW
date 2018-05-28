import cx_Oracle
import json
import os


def addUser(usname, fname, lname, passw, country, city):
    # def addRegisteerInfo(database_file,new_user):
    conn = cx_Oracle.connect(
        'student/STUDENT@localhost:1521', encoding="UTF-8")
    cursor = conn.cursor()
    print(cursor)
    querystring = '''SELECT max(ID) FROM USERS'''
    cursor.execute(querystring)
    usID = cursor.fetchone()[0]
    if usID != None:
        usID = usID + 1
    else:
        usID = 1
    # cursor.close()
    # conn.close()
    # return usID

    # querystring = '''INSERT INTO USERS (ID,USER_NAME,FIRST_NAME,LAST_NAME,PASSWORD,COUNTRY,CITY) VALUES ( ?, ?, ?, ?, ?, ?, ?)'''.format( usID, usname, fname, lname, passw, country, city)
    # querystring = '''INSERT INTO USERS VALUES(usID,usname,fname,lname,passw,country,city)'''
    querystring = '''INSERT INTO USERS(ID,USER_NAME,FIRST_NAME,LAST_NAME,PASSWORD,COUNTRY,CITY) VALUES({ID},'{USER_NAME}','{FIRST_NAME}','{LAST_NAME}','{PASSWORD}','{COUNTRY}','{CITY}')'''.format(
        ID=usID, USER_NAME=usname, FIRST_NAME=fname, LAST_NAME=lname, PASSWORD=passw, COUNTRY=country, CITY=city)
    # querystring = "INSERT INTO USERS(ID,USER_NAME,FIRST_NAME,LAST_NAME,PASSWORD,COUNTRY,CITY) VALUES(usID,usname,fname,lname,passw,country,city)"
    cursor.execute(querystring)
    cursor.close()
    conn.commit()
    conn.close()


def addLocation(database_file, usname, orgLoc, destLoc, startMig, endMig):
    conn = cx_Oracle.connect(
        'student/STUDENT@localhost:1521', encoding="UTF-8")
    cursor = conn.cursor()
    print(cursor)
    querystring = '''SELECT max(ID_DEST) FROM LOCATION'''
    cursor.execute(querystring)
    locID = cursor.fetchone()[0]
    if locID != None:
        locID = locID + 1
    else:
        locID = 1

    cursor.execute("SELECT ID FROM USERS WHERE USER_NAME='" + usname + "';")
    usID = cursor.fetchone()

    querystring = '''INSERT INTO LOCATION VALUES({ID_DEST},{ID_USER},'{ORG_LOCATION}','{DEST_LOCATION}',to_Date('{START_MIG}','dd.mm.yyyy'),to_Date('{END_MIG}','dd.mm.yyyy'))'''.format(
        ID_DEST=locID, ID_USER=usID, ORG_LOCATION=orgLoc, DEST_LOCATION=destLoc, START_MIG=startMig, END_MIG=endMig)
    cursor.execute(querystring)

    cursor.close()
    conn.commit()
    # conn.close()


def addLocationList(database_file, usname):
    conn = cx_Oracle.connect(
         'student/STUDENT@localhost:1521', encoding="UTF-8")
    cursor = conn.cursor()
    print(cursor)
    cursor.execute("SELECT ID FROM USERS WHERE USER_NAME='" + usname + "';")
    usID = cursor.fetchone()
    
    cursor.execute("SELECT DEST_LOCATION FROM LOCATION WHERE ID_USER='" + usID + "' ORDER BY ID_DEST DESC;")
    destination = cursor.fetchone()


    cursor.execute("SELECT floor((END_MIG-START_MIG)/365)  FROM LOCATION WHERE ID_USER='" + usID + "' ORDER BY ID_DEST DESC;")
    days= cursor.fetchone()

    querystring = '''INSERT INTO LOCATION VALUES({ID_USER},'{LOC}','{ZILE}')'''.format(ID_USER=usID,LOC=destination,ZILE=days)
    cursor.execute( querystring)  

    cursor.close()
    conn.commit()
    conn.close()
   # trebuie sa iei toate inputurile si sa le inserzi in toate tabelele aferente 
   #


addUser('Alina333','Alina','Mihaiescu','Alina123','Romania','Galati')
