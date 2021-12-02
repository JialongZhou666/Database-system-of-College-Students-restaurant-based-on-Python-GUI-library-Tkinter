from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

class select_customer_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('餐厅管理人员界面')
        self.master.geometry('889x509')
        self.createWidgets()
		
    def createWidgets(self):
        self.top = Tk()
        self.top.title('顾客信息表')

        self.style = Style()
        
        self.tree = Treeview(self.top)
        self.tree["columns"] = ("学号", "姓名", "性别", "电话")
        self.tree.column("学号", width=100)
        self.tree.column("姓名", width=100)
        self.tree.column("性别", width=100)
        self.tree.column("电话", width=100)
        self.tree.heading("学号", text="学号")
        self.tree.heading("姓名", text="姓名")
        self.tree.heading("性别", text="性别")
        self.tree.heading("电话", text="电话")
        
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
        cursor.execute("select * from customer")
        data = cursor.fetchall()
        cnt=1
        for row in data:
            sno = row[0]
            sname = row[1]
            ssex = row[2]
            stel = row[3]
            self.tree.insert("", cnt, text="line{}".format(cnt), values=(sno, sname, ssex, stel))
            cnt=cnt+1

        db.close()
