import mysql.connector
from mysql.connector import errorcode
# mysql.connector.connect(host='localhost',database='mysql',user='root',password='')

print('Hello!')

# http://webpy.org/docs/0.3/tutorial


# --mysql connection
# name wdp
# pass kajhzbn7vceW

DB_NAME = 'todo'

TABLES = {}
TABLES['todo'] = (
    "CREATE TABLE `todo` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `title` varchar(14) NOT NULL,"
    "  `created` date NOT NULL,"
    "  `done` BOOLEAN DEFAULT 0,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='wdp', database='todo', password='kajhzbn7vceW')
print('cnx', cnx)
cursor = cnx.cursor()
print('cursor', cursor)





# def create_database(cursor):
#     try:
#         cursor.execute(
#             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#         print('DB created')
#     except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)
#
# try:
#     cnx.database = DB_NAME
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_BAD_DB_ERROR:
#         create_database(cursor)
#         cnx.database = DB_NAME
#     else:
#         print(err)
#         exit(1)
#
# for name, ddl in TABLES.iteritems():
#     try:
#         print("Creating table {}: ".format(name), end='')
#         cursor.execute(ddl)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     else:
#         print("OK")


# create_database(cursor)

cursor.close()
cnx.close()

