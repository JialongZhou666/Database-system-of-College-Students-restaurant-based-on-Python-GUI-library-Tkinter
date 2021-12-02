from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import identity2 as iden2
import pymysql

class identity1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('身份验证界面')
        self.master.geometry('409x300')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        global img0
        self.style.configure('Label4.TLabel',anchor='center', justify='center')
        photo = Image.open("E:/新桌面/ttttt/background2.png")
        photo = photo.resize((409,300))
        img0 = ImageTk.PhotoImage(photo)
        self.Label4 = Label(self.top, image=img0, style='Label4.TLabel')
        self.Label4.pack()
        
        self.style.configure('Label1.TLabel',relief=SUNKEN, anchor='center', font=('楷体',16))
        self.Label1 = Label(self.top, text='身份验证', style='Label1.TLabel')
        self.Label1.place(relx=0.02, rely=0.027, relwidth=0.257, relheight=0.083)

        self.Text1Var = StringVar()
        self.Text1 = Entry(self.top, textvariable=self.Text1Var)
        self.Text1.place(relx=0.372, rely=0.32, relwidth=0.374, relheight=0.083)

        self.style.configure('Label2.TLabel',anchor='center', font=('楷体',15))
        self.Label2 = Label(self.top, text='用户名：', style='Label2.TLabel')
        self.Label2.place(relx=0.117, rely=0.32, relwidth=0.198, relheight=0.083)

        self.Text2Var = StringVar()
        self.Text2 = Entry(self.top, textvariable=self.Text2Var)
        self.Text2.place(relx=0.372, rely=0.507, relwidth=0.374, relheight=0.083)

        self.style.configure('Label3.TLabel',anchor='center', font=('楷体',15))
        self.Label3 = Label(self.top, text='密码：', style='Label3.TLabel')
        self.Label3.place(relx=0.156, rely=0.507, relwidth=0.159, relheight=0.083)

        self.style.configure('Command1.TButton',font=('楷体',16))
        self.Command1 = Button(self.top, text='登陆', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.372, rely=0.72, relwidth=0.257, relheight=0.11)

    def Command1_Cmd(self, event=None):
        self.identity_in_db()

    def identity_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        cursor.execute("select username from usr where username={} and pw={}".format(self.Text1.get(),self.Text2.get()))
        data = cursor.fetchone()
        if data == None:
            showwarning("警告","您不是餐厅管理人员！")
        else:
            showinfo("成功","已成功确认您的餐厅管理人员身份！")
            self.top.destroy()
            iden2.identity2()

        db.close()

