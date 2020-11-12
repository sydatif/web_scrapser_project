
# RDS info - Running on AWS
# DB instance identifier:csv-to-rds
# username: admin
# password : webscarping 
# Endpint :csv-to-rds.cmvifwvlg9wu.ca-central-1.rds.amazonaws.com
# Port : 3306


import pymysql # run 'pip install PyMySQL' command to install MySQL module 
import db_credentials # In this file we can save database credentials. it exists in local directory


#db = pymysql.connect('csv-to-rds.cmvifwvlg9wu.ca-central-1.rds.amazonaws.com', 'admin','webscarping')
db = pymysql.connect(db_credentials.database, db_credentials.username, db_credentials.password, autocommit=True, local_infile=True)


cursor = db.cursor() # A database cursor is an object that enables traversal over the rows of a result set.
                     # It allows you to process individual row returned by a query.


def show_rds_version():
    cursor.execute("select version()")
    data = cursor.fetchone()
    print(data [0])


def show_database():
    sql = '''show databases;'''
    cursor.execute(sql)
    for databases in cursor:
        print(databases[0])

def create_database(): 
    sql = '''CREATE DATABASE IF NOT EXISTS scarp_project;'''
    cursor.execute(sql)
    cursor.connection.commit()

def select_database():
    sql = ''' USE scarp_project;'''
    cursor.execute(sql)
    

def create_table():
    sql = ''' CREATE TABLE IF NOT EXISTS post_data (username VARCHAR(20) PRIMARY KEY, address VARCHAR(35), friend_count INT, post_date VARCHAR(10), review_count INT, post_text TEXT);'''
    cursor.execute(sql)
    

def show_tables():
    sql ='''show TABLES;'''     
    cursor.execute(sql)
    for table in cursor:
        print(table[0])

def check_inline_status():
    sql = '''SHOW VARIABLES LIKE 'local_infile';'''
    cursor.execute(sql)
    data = cursor.fetchone()
    print(data)


def upload_csv_file():
    sql = '''LOAD DATA LOCAL INFILE '/home/satif/becloudready/python/scraper_project/post.csv' 
    INTO TABLE post_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;'''
    cursor.execute(sql)     
    print(sql)

def show_table_data():
    sql = ''' SELECT * FROM post_data;'''
    cursor.execute(sql)
    for row in cursor:
        print(row)

if __name__ == "__main__":

    show_rds_version()
    show_database()
    create_database()
    show_database()
    select_database()
    create_table()
    show_tables()
    check_inline_status()
    upload_csv_file()
    show_table_data()