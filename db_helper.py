import mysql.connector as sql

# connection = sql.connect(
#                 host = 'localhost',
#                 port = '3306',
#                 user = 'user1',
#                 password = 'password',
#                 database = 'learn_website'
#             )

class DBHELPER:
    def __init__(self):
        self.con = sql.connect(
                host = 'localhost',
                port = '3306',
                user = 'user1',
                password = 'password',
                database = 'SE_ACTIVITY'
                )
        # create table if it doesnt exits   
        query = 'CREATE TABLE IF NOT EXISTS Library(userid INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(200),email VARCHAR(200),phone VARCHAR(12),book_name VARCHAR(200))' 
        curr = self.con.cursor()
        curr.execute(query)
        print("Created")

    # inserting in db
    def insert_user(self,username,email,phone,book_name):
        query = "INSERT INTO Library(username,email,phone,book_name) VALUES('{}','{}',{},'{}')".format(username,email,phone,book_name)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('user saved to db')

    def fetch_all(self):
        query = "SELECT * FROM Library"
        cur = self.con.cursor()
        cur.execute(query)
        dataset = cur.fetchall()
        return dataset
        # print('here are your datasets\n\n')
        # for row in dataset:
        #     print('ID: ',row[0])
        #     print('NAME: ',row[1])
        #     print('EMAIL: ',row[2])
        #     print("PHONE NO: ",row[3])
        #     print("book_name: " row[4])
        #     print('\n\n')

    def delete_user(self,userid):
        query = 'DELETE FROM Library WHERE userid = {}'.format(userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Userid {} deleted !".format(userid))

    def update_user(self,userid,new_name,new_email,new_phone,book_name):
        query = 'UPDATE Library SET username="{}",email="{}",phone="{}",book_name="{}" WHERE userid={}'.format(new_name,new_email,new_phone,book_name,userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Userid {} updated !".format(userid))
