from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql

class select_food_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('餐厅管理人员界面')
        self.master.geometry('889x509')
        self.createWidgets()
		
    def createWidgets(self):
        self.top = Tk()

        self.style = Style()
        self.top.title('菜品信息表')
        
        self.tree = Treeview(self.top)
        self.tree["columns"] = ("菜号", "菜名", "主要原料1", "主要原料2", "甜或咸", "辣或不辣", "高或低热量")
        self.tree.column("菜号", width=100)
        self.tree.column("菜名", width=100)
        self.tree.column("主要原料1", width=100)
        self.tree.column("主要原料2", width=100)
        self.tree.column("甜或咸", width=100)
        self.tree.column("辣或不辣", width=100)
        self.tree.column("高或低热量", width=100)
        self.tree.heading("菜号", text="菜号")
        self.tree.heading("菜名", text="菜名")
        self.tree.heading("主要原料1", text="主要原料1")
        self.tree.heading("主要原料2", text="主要原料2")
        self.tree.heading("甜或咸", text="甜或咸")
        self.tree.heading("辣或不辣", text="辣或不辣")
        self.tree.heading("高或低热量", text="高或低热量")
        
        self.select_food_table_in_db()
        
        self.tree.pack()
        self.top.mainloop()
        
    def select_food_table_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        cursor.execute("select * from food")
        data = cursor.fetchall()
        cnt=1
        for row in data:
            fno = row[0]
            fname = row[1]
            main_material1 = row[2]
            main_material2 = row[3]
            sweet = row[4]
            hot = row[5]
            hi_calorie = row[6]
            self.tree.insert("", cnt, text="line{}".format(cnt), values=(fno, fname, main_material1, main_material2, sweet, hot, hi_calorie))
            cnt=cnt+1

        db.close() 
