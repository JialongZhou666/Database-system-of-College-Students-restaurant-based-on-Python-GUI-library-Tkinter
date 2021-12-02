from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

class select_sell_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('餐厅管理人员界面')
        self.master.geometry('889x509')
        self.createWidgets()
		
    def createWidgets(self):
        self.top = Tk()
        self.top.title("售卖信息表")

        self.style = Style()
        
        self.tree = Treeview(self.top)
        self.tree["columns"] = ("菜号", "菜名", "卖出数量")
        self.tree.column("菜号", width=100)
        self.tree.column("菜名", width=100)
        self.tree.column("卖出数量", width=100)
        self.tree.heading("菜号", text="菜号")
        self.tree.heading("菜名", text="菜名")
        self.tree.heading("卖出数量", text="卖出数量")
        
        self.select_sell_table_in_db()
        
        self.tree.pack()
        self.top.mainloop()
        
    def select_sell_table_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        cursor.execute("select food.fno,fname,sell_num from food,sell where food.fno=sell.fno")
        data = cursor.fetchall()
        cnt=1
        for row in data:
            fno = row[0]
            fname = row[1]
            sell_num = row[2]
            self.tree.insert("", cnt, text="line{}".format(cnt), values=(fno, fname, sell_num))
            cnt=cnt+1

        db.close()
