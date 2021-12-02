from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

class select_usr_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('餐厅管理人员界面')
        self.master.geometry('889x509')
        self.createWidgets()
		
    def createWidgets(self):
        self.top = Tk()
        self.top.title("用户信息表")

        self.style = Style()
        
        self.tree = Treeview(self.top)
        self.tree["columns"] = ("用户名", "密码", "职位")
        self.tree.column("用户名", width=100)
        self.tree.column("密码", width=100)
        self.tree.column("职位", width=100)
        self.tree.heading("用户名", text="用户名")
        self.tree.heading("密码", text="密码")
        self.tree.heading("职位", text="职位")
        
        self.select_usr_table_in_db()
        
        self.tree.pack()
        self.top.mainloop()
        
    def select_usr_table_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        cursor.execute("select * from usr")
        data = cursor.fetchall()
        cnt=1
        for row in data:
            username = row[0]
            pw = row[1]
            job = row[2]
            self.tree.insert("", cnt, text="line{}".format(cnt), values=(username, pw, job))
            cnt=cnt+1

        db.close()
