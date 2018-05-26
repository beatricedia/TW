CREATE TABLE USERS
( ID number not null primary key,
  USER_NAME  VARCHAR2(64) not null ,
  FIRST_NAME VARCHAR2(64) not null,
  LAST_NAME VARCHAR2(64) not null,
  PASSWARD VARCHAR2(64) not null,
  COUNTRY  VARCHAR2(64) not null,
  CITY VARCHAR2(64) not null
);

/
CREATE TABLE LOCATION
( ID_DEST NUMBER not null	primary key,
  ID_USER NUMBER not null,
  ORIGIN_LOCATION VARCHAR2(64) not null,
  DESTINATION_LOCATION VARCHAR2(64) not null,
  START_MIG DATE not null,
  END_MIG DATE not null,
);
--da update de fiecare data la origin si destination
/

CREATE TABLE LOCATION_LIST
( ID_USER NUMBER not null primary key,
   LOC  VARCHAR2(64) not null,
   ZILE number
);
/
CREATE TABLE LOC_STATISTIC
( ID_DEST NUMBER not null	primary key,
  TRANZIT VARCHAR2(64) not null,
  CLIMA VARCHAR2(64) not null,
  COND_DEMOGF VARCHAR2(64) not null
);
/
CREATE UNIQUE INDEX USERS_USERNAME_UINDEX
	on USERS (USERNAME)
/  

/*
  CREATE OR REPLACE TRIGGER not_destructiv
  BEFORE DROP ON SCHEMA
BEGIN
     
      RAISE_APPLICATION_ERROR (
      num => -20000,
      msg => 'Tabelul nu poate fi alterat');
      COMMIT;
END;   
*/
--drop trigger not_destructiv;

