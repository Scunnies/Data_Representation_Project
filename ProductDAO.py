# ProductDAO.py

import mysql.connector
import dbconfig as cfg

class ProductDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = 'products_db'

    def initialize_database_connection(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()

    def getcursor(self):
        if not self.connection or not self.connection.is_connected():
            self.initialize_database_connection()
        return self.cursor

    def closeAll(self):
        if self.connection.is_connected():
            self.connection.close()
        if self.cursor:
            self.cursor.close()

    def create(self, values):
        print(f"Creating a new product in the database with values: {values}")
        cursor = self.getcursor()
        sql = "insert into products (name, price, description) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        print("Getting all products from the database")
        cursor = self.getcursor()
        sql = "select * from products"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"Results: {results}")
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.closeAll()
        print(f"Return Array: {returnArray}")
        return returnArray


        self.closeAll()
        return returnArray

    def findByID(self, id):
        print(f"Finding product by ID: {id}")
        cursor = self.getcursor()
        sql = "select * from products where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        print(f"Updating product in the database with values: {values}")
        cursor = self.getcursor()
        sql = "update products set name= %s, price=%s, description=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        print(f"Deleting product from the database with ID: {id}")
        cursor = self.getcursor()
        sql = "delete from products where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        print("Delete done")

    def convertToDictionary(self, result):
        colnames = ['id', 'name', 'price', 'description']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

productDAO = ProductDAO()
