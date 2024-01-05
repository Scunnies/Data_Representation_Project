import mysql.connector
import dbconfig as cfg

class ProductDAO:
    connection = None
    cursor = None

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = 'products_db'
        self.initialize_database_connection()

    def initialize_database_connection(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
        if self.cursor:
            self.cursor.close()

    def create(self, values):
        print(f"creating a new product in the database with values: {values}")
        self.initialize_database_connection()
        sql = "insert into products (name, price, description) values (%s,%s,%s)"
        self.cursor.execute(sql, values)
        self.connection.commit()
        newid = self.cursor.lastrowid
        self.close_connection()
        return newid

    def getAll(self):
        print("getting all products from the database")
        self.initialize_database_connection()
        sql = "select * from products"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(f"results: {results}")
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))

        self.close_connection()
        print(f"return array: {returnArray}")
        return returnArray

    def findByID(self, id):
        print(f"finding product by ID: {id}")
        self.initialize_database_connection()
        sql = "select * from products where id = %s"
        values = (id,)

        self.cursor.execute(sql, values)
        result = self.cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.close_connection()
        return returnvalue

    def update(self, values):
        print(f"updating product in the database with values: {values}")
        self.initialize_database_connection()
        sql = "update products set name= %s, price=%s, description=%s  where id = %s"
        self.cursor.execute(sql, values)
        self.connection.commit()
        self.close_connection()

    def delete(self, id):
        print(f"deleting product from the database with ID: {id}")
        self.initialize_database_connection()
        sql = "delete from products where id = %s"
        values = (id,)

        self.cursor.execute(sql, values)

        self.connection.commit()  # Commit the changes to the database
        self.close_connection()
        print("delete done")


    def convertToDictionary(self, result):
        colnames = ['id', 'name', 'price', 'description']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

    def __del__(self):
        self.close_connection()

# Create an instance of the ProductDAO class
productDAO = ProductDAO()
