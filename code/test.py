import createTable

if __name__ == "__main__":
    mysql = createTable.MysqlTable()
    mysql.create_table('t.csv')
    print(mysql.get_info("SELECT * FROM HasLanguages"))
    mysql.disconnect()
