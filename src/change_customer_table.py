from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import pymysql
import identity2 as iden2

class change_customer_table(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('修改顾客信息')
        self.master.geometry('426x417')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        global img0
        self.style.configure('Label4.TLabel',anchor='center', justify='center')
        photo = Image.open("E:/新桌面/ttttt/pic4.jpg")
        photo = photo.resize((426,417))
        img0 = ImageTk.PhotoImage(photo)
        self.Label10 = Label(self.top, image=img0, style='Label10.TLabel')
        self.Label10.pack()

        self.style.configure('Label1.TLabel',relief=SUNKEN, anchor='w', font=('楷体',15))
        self.Label1 = Label(self.top, text='修改信息', style='Label1.TLabel')
        self.Label1.place(relx=0.019, rely=0.019, relwidth=0.197, relheight=0.07)

        self.style.configure('Label2.TLabel',anchor='w', font=('楷体',14))
        self.Label2 = Label(self.top, text='学号：', style='Label2.TLabel')
        self.Label2.place(relx=0.131, rely=0.269, relwidth=0.141, relheight=0.065)

        self.style.configure('Label3.TLabel',anchor='w', font=('楷体',14))
        self.Label3 = Label(self.top, text='姓名：', style='Label3.TLabel')
        self.Label3.place(relx=0.131, rely=0.384, relwidth=0.141, relheight=0.065)

        self.style.configure('Label4.TLabel',anchor='w', font=('楷体',14))
        self.Label4 = Label(self.top, text='性别：', style='Label4.TLabel')
        self.Label4.place(relx=0.131, rely=0.499, relwidth=0.141, relheight=0.065)

        self.style.configure('Label5.TLabel',anchor='w', font=('楷体',14))
        self.Label5 = Label(self.top, text='电话：', style='Label5.TLabel')
        self.Label5.place(relx=0.131, rely=0.614, relwidth=0.141, relheight=0.065)

        self.style.configure('Label6.TLabel',anchor='w', font=('楷体',14))
        self.Label6 = Label(self.top, text='操作：', style='Label6.TLabel')
        self.Label6.place(relx=0.131, rely=0.153, relwidth=0.153, relheight=0.06)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.319, rely=0.269, relwidth=0.453, relheight=0.06)

        self.Combo1List = ['增加','删除','更新']
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.319, rely=0.153, relwidth=0.453, relheight=0.048)
        self.Combo1.set(self.Combo1List[0])

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='Text2', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.319, rely=0.384, relwidth=0.453, relheight=0.06)

        self.Text3Var = StringVar(value='Text3')
        self.Text3 = Entry(self.top, text='Text3', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.319, rely=0.499, relwidth=0.453, relheight=0.062)

        self.Text4Var = StringVar(value='Text4')
        self.Text4 = Entry(self.top, text='Text4', textvariable=self.Text4Var, font=('宋体',9))
        self.Text4.place(relx=0.319, rely=0.614, relwidth=0.453, relheight=0.06)

        self.style.configure('Command1.TButton',font=('楷体',14))
        self.Command1 = Button(self.top, text='确认', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.376, rely=0.787, relwidth=0.209, relheight=0.098)
        
    def Command1_Cmd(self, event=None):
        self.change_customer_in_db()
		
    def change_customer_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        sql1 = "call customer_insert(%d,'%s','%s','%s');" % (
            int(self.Text1.get()),self.Text2.get(),self.Text3.get(),self.Text4.get())
        sql2 = "call customer_delete(%d,'%s','%s','%s');" % (
            int(self.Text1.get()),self.Text2.get(),self.Text3.get(),self.Text4.get())
        sql3 = "call customer_update(%d,'%s','%s','%s');" % (
            int(self.Text1.get()),self.Text2.get(),self.Text3.get(),self.Text4.get())
        if self.Combo1.get() ==  '增加':
            try:
                cursor.execute(sql1)
                db.commit()
                messagebox.showinfo('完成', '已成功增加顾客信息!')
            except pymysql.err.OperationalError as err:
                print("发生异常", err)
                messagebox.showinfo('异常', err)
                db.rollback()
        elif self.Combo1.get() == '删除':
            try:
                cursor.execute(sql2)
                db.commit()
                messagebox.showinfo('完成', '已成功删除顾客信息!')
            except pymysql.err.OperationalError as err:
                print("发生异常", err)
                messagebox.showinfo('异常', err)
                db.rollback()
        elif self.Combo1.get() == '更新':
            try:
                cursor.execute(sql3)
                db.commit()
                messagebox.showinfo('完成', '已成功更新顾客信息!')
            except pymysql.err.OperationalError as err:
                print("发生异常", err)
                messagebox.showinfo('异常', err)
                db.rollback()
        db.close()
        self.top.destroy()
        iden2.identity2().__init__()
