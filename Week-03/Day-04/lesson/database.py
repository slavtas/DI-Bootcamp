# import pg8000   
# connection = pg8000.connect(database = 'countries',
#                               user = 'my_env_',
#                               password = 'admin',
#                               host= 'localhost',
#                               port = '5432')
# cursor = connection.cursor()
# cursor.execute('DROP TABLE if EXISTS random_countries')
# create_table_query = f'''CREATE TABLE random_countries(
#                         country_id SERIAL PRIMARY KEY,
#                         name VARCHAR(100) NOT NULL,
#                         capital VARCHAR(100) NOT NULL,
#                         flag_code VARCHAR(100),
#                         population INTEGER
#                         )'''
# cursor.execute(create_table_query)
# connection.commit()

import pg8000

try:
    conn = pg8000.connect(
        dbname="your_db",
        user="your_user",
        password="your_password",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print("Error:", e)

