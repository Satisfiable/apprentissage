import sqlite3

class Database():

    def connect_database(self):

        try:
            self.connection = sqlite3.connect("Century.db")
            self.cursor = self.connection.cursor()

            table_query = "CREATE TABLE IF NOT EXISTS Archive (Date TEXT PRIMARY KEY)"
            self.cursor.execute(table_query)
            self.connection.commit()
            print("Veri tabanına bağlanıldı!")
        except Exception as e:
            print("[Hata] Veri tabanına bağlanılamadı. Hata kodu: " + str(e))

    def disconnect_database(self):

        self.connection.close()

    def insert_statement(self, statement_name):

        column_query = "ALTER TABLE student ADD COLUMN {} BLOB".format(statement_name)
        self.cursor.execute(column_query)

    def convertToBinaryData(self, filename):
   
        with open(filename, 'rb') as file:
            blobData = file.read()

        return blobData

    def writeTofile(self, data, filename):
        
        with open(filename, 'wb') as file:
            file.write(data)

