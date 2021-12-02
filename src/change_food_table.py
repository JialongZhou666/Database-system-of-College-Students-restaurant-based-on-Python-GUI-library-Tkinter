from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import pymysql
import identity2 as iden2

class change_food_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('修改菜品信息')
        self.master.geometry('463x425')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        global img0
        self.style.configure('Label4.TLabel',anchor='center', justify='center')
        photo = Image.open("E:/新桌面/ttttt/pic3.jpg")
        photo = photo.resize((463,425))
        img0 = ImageTk.PhotoImage(photo)
        self.Label10 = Label(self.top, image=img0, style='Label10.TLabel')
        self.Label10.pack()
        
        self.style.configure('Command1.TButton',font=('楷体',14))
        self.Command1 = Button(self.top, text='确认', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.415, rely=0.889, relwidth=0.158, relheight=0.063)

        self.Text7Var = StringVar(value='Text7')
        self.Text7 = Entry(self.top, text='Text7', textvariable=self.Text7Var, font=('宋体',9))
        self.Text7.place(relx=0.432, rely=0.766, relwidth=0.4, relheight=0.048)

        self.Text6Var = StringVar(value='Text6')
        self.Text6 = Entry(self.top, text='Text6', textvariable=self.Text6Var, font=('宋体',9))
        self.Text6.place(relx=0.432, rely=0.674, relwidth=0.4, relheight=0.048)

        self.Text5Var = StringVar(value='Text5')
        self.Text5 = Entry(self.top, text='Text5', textvariable=self.Text5Var, font=('宋体',9))
        self.Text5.place(relx=0.432, rely=0.582, relwidth=0.4, relheight=0.048)

        self.Text4Var = StringVar(value='Text4')
        self.Text4 = Entry(self.top, text='Text4', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.432, rely=0.49, relwidth=0.4, relheight=0.048)

        self.Text3Var = StringVar(value='Text3')
        self.Text3 = Entry(self.top, text='Text3', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.432, rely=0.398, relwidth=0.4, relheight=0.048)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='Text2', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.432, rely=0.307, relwidth=0.4, relheight=0.048)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.432, rely=0.215, relwidth=0.4, relheight=0.048)

        self.Combo1List = ['增加','删除','更新']
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.432, rely=0.123, relwidth=0.4, relheight=0.038)
        self.Combo1.set(self.Combo1List[0])

        self.style.configure('Label9.TLabel',anchor='w', font=('楷体',14))
        self.Label9 = Label(self.top, text='高或低热量：', style='Label9.TLabel')
        self.Label9.place(relx=0.104, rely=0.766, relwidth=0.259, relheight=0.052)

        self.style.configure('Label8.TLabel',anchor='w', font=('楷体',14))
        self.Label8 = Label(self.top, text='辣或不辣：', style='Label8.TLabel')
        self.Label8.place(relx=0.138, rely=0.674, relwidth=0.216, relheight=0.052)

        self.style.configure('Label7.TLabel',anchor='w', font=('楷体',14))
        self.Label7 = Label(self.top, text='甜或咸：', style='Label7.TLabel')
        self.Label7.place(relx=0.19, rely=0.582, relwidth=0.173, relheight=0.052)

        self.style.configure('Label6.TLabel',anchor='w', font=('楷体',14))
        self.Label6 = Label(self.top, text='主要原料2：', style='Label6.TLabel')
        self.Label6.place(relx=0.121, rely=0.49, relwidth=0.238, relheight=0.052)

        self.style.configure('Label5.TLabel',anchor='w', font=('楷体',14))
        self.Label5 = Label(self.top, text='主要原料1：', style='Label5.TLabel')
        self.Label5.place(relx=0.121, rely=0.398, relwidth=0.238, relheight=0.052)

        self.style.configure('Label4.TLabel',anchor='w', font=('楷体',14))
        self.Label4 = Label(self.top, text='操作：', style='Label4.TLabel')
        self.Label4.place(relx=0.225, rely=0.123, relwidth=0.13, relheight=0.052)

        self.style.configure('Label3.TLabel',anchor='w', font=('楷体',14))
        self.Label3 = Label(self.top, text='菜名：', style='Label3.TLabel')
        self.Label3.place(relx=0.225, rely=0.307, relwidth=0.13, relheight=0.052)

        self.style.configure('Label2.TLabel',anchor='w', font=('楷体',14))
        self.Label2 = Label(self.top, text='菜号：', style='Label2.TLabel')
        self.Label2.place(relx=0.225, rely=0.215, relwidth=0.13, relheight=0.052)

        self.style.configure('Label1.TLabel',relief=SUNKEN, anchor='center', font=('楷体',16))
        self.Label1 = Label(self.top, text='修改信息', style='Label1.TLabel')
        self.Label1.place(relx=0.017, rely=0.015, relwidth=0.199, relheight=0.079)
        
    def Command1_Cmd(self, event=None):
        self.change_food_in_db()
		
    def change_food_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        sql1 = "call food_insert(%d,'%s','%s','%s','%s','%s','%s');" % (
            int(self.Text1.get()),self.Text2.get(),self.Text3.get(),self.Text4.get(),self.Text5.get(),self.Text6.get(),self.Text7.get())
        sql2 = "call food_delete(%d,'%s','%s','%s','%s','%s','%s');" % (
            int(self.Text1.get()),self.Text2.get(),self.Text3.get(),self.Text4.get(),self.Text5.get(),self.Text6.get(),self.Text7.get())
        sql3 = "call food_update(%d,'%s','%s','%s','%s','%s','%s');" % (
            int(self.Text1.get()),self.Text2.get(),self.Text3.get(),self.Text4.get(),self.Text5.get(),self.Text6.get(),self.Text7.get())
        if self.Combo1.get() ==  '增加':
            try:
                cursor.execute(sql1)
                db.commit()
                messagebox.showinfo('完成', '已成功增加菜品信息!')
            except pymysql.err.OperationalError as err:
                print("发生异常", err)
                messagebox.showinfo('异常', err)
                db.rollback()
        elif self.Combo1.get() == '删除':
            try:
                cursor.execute(sql2)
                db.commit()
                messagebox.showinfo('完成', '已成功删除菜品信息!')
            except pymysql.err.OperationalError as err:
                print("发生异常", err)
                messagebox.showinfo('异常', err)
                db.rollback()
        elif self.Combo1.get() == '更新':
            try:
                cursor.execute(sql3)
                db.commit()
                messagebox.showinfo('完成', '已成功更新菜品信息!')
            except pymysql.err.OperationalError as err:
                print("发生异常", err)
                messagebox.showinfo('异常', err)
                db.rollback()
        db.close()
        self.top.destroy()
        iden2.identity2().__init__()
