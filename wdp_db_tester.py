from mysql.connector import MySQLConnection, Error
from db_config import read_db_config


def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
            print('DBG conn:', type(conn), conn)
            # print('DBG dir(conn):', dir(conn))
            print('DBG server info:', conn.get_server_info())
            print('DBG server version:', conn.get_server_version())
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')


def insert_data(text):              # note kwargs...
    ''' Insert data into database
    :param filename: name of the configuration file
    :param section: section of database configuration
    
    :return: a dictionary of database parameters
    
    # preapare query format
    # query is like:
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
    # and it's args
    args = (title, isbn)
    
    # connect ...
    conn = MySQLConnection(**db_config)
    # create cursor
    cursor = conn.cursor()
    # execute
    cursor.execute(query, args)
    # commit
    conn.commit()
    # close cursor and connection
    cursor.close()
    conn.close()
    

    
    '''
    query = ("INSERT INTO todozero" \
            "(todozero_text, todozero_num) " \
            "VALUES (%s, 0)")
    args = (text,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)  # possible cursor.executemany(query, text)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()



def main():
    # set initial values for table for webdotpy project
    test_proj_data = ['web.py',
                      'SQLAlchemy',
                      'Celery',
                      'RabbitMQ']
    for item in test_proj_data:
        insert_data(item)

if __name__ == '__main__':
    main()

