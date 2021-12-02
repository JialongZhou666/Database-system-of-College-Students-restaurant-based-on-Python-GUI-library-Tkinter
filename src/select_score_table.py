from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

class select_score_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('餐厅管理人员界面')
        self.master.geometry('889x509')
        self.createWidgets()
		
    def createWidgets(self):
        self.top = Tk()
        self.top.title("打分信息表")

        self.style = Style()
        
        self.tree = Treeview(self.top)
        self.tree["columns"] = ("菜号", "菜名", "分数")
        self.tree.column("菜号", width=100)
        self.tree.column("菜名", width=100)
        self.tree.column("分数", width=100)
        self.tree.heading("菜号", text="菜号")
        self.tree.heading("菜名", text="菜名")
        self.tree.heading("分数", text="分数")
        
        self.select_score_table_in_db()
        
        self.tree.pack()
        self.top.mainloop()
        
    def select_score_table_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        cursor.execute("select food.fno,fname,score from food,score_table where food.fno=score_table.fno")
        data = cursor.fetchall()
        cnt=1
        for row in data:
            fno = row[0]
            fname = row[1]
            score = row[2]
            self.tree.insert("", cnt, text="line{}".format(cnt), values=(fno, fname, score))
            cnt=cnt+1

        db.close()
