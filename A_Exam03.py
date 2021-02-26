import sqlite3

def Create_Table():
    conn = sqlite3.connect("fruit.db")
    cur = conn.cursor()
    conn.execute("create table fruit_table (Id , Name  , Price )")
    cur.close()
    conn.close()

if __name__ == "__main__":
  Create_Table();

def Insert_M():
    connector = sqlite3.connect("fruit.db")
    sql = "insert into fruit_table values('1','사과','2000')"
    connector.execute(sql)
    sql = "insert into fruit_table values('2','배','1000')"
    connector.execute(sql)
    sql = "insert into fruit_table values('3','바나나','4000')"
    connector.execute(sql)
    connector.commit()
    connector.close()
    print('Insert_M()_sss')

def Select_M():
    connector = sqlite3.connect("fruit.db")
    cursor = connector.cursor()
    cursor.execute("select * from fruit_table")
    rows = cursor.fetchall()

    for row in rows:
        print("%s 는 %s원 입니다." %(row[1],row[2]))

    cursor.close()
    connector.close()

if __name__ == "__main__":
    Insert_M()
    Select_M()