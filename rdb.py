import sqlite3

class Rdatabase:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS order2(
            date text,
            total text,
            billno text,
            costofdrink text,
            costoffood text,
            menu text
            )
            """
        self.cur.execute(sql)
        self.con.commit()

    def save(self,date,total,billno,costofdrink,costoffood,menu):
        self.cur.execute("insert into order2 values (?,?,?,?,?,?)",
                         (date,total,billno,costofdrink,costoffood,menu))
        self.con.commit()

    def displayall(self):
        self.cur.execute("SELECT * from order2")
        rows = self.cur.fetchall()
        # print(rows)
        return rows
