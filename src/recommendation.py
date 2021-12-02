from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import pymysql
import customer_page as cp

class recommendation(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('菜品推荐查询')
        self.master.geometry('467x283')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        global img0
        self.style.configure('Label4.TLabel',anchor='center', justify='center')
        photo = Image.open("E:/新桌面/ttttt/pic5.jpg")
        photo = photo.resize((467,283))
        img0 = ImageTk.PhotoImage(photo)
        self.Label4 = Label(self.top, image=img0, style='Label4.TLabel')
        self.Label4.pack()
        
        self.style.configure('Label1.TLabel',anchor='w', font=('楷体',14))
        self.Label1 = Label(self.top, text='甜或不甜：', style='Label1.TLabel')
        self.Label1.place(relx=0.188, rely=0.141, relwidth=0.214, relheight=0.095)

        self.style.configure('Label2.TLabel',anchor='w', font=('楷体',14))
        self.Label2 = Label(self.top, text='辣或不辣：', style='Label2.TLabel')
        self.Label2.place(relx=0.188, rely=0.339, relwidth=0.214, relheight=0.095)

        self.style.configure('Label3.TLabel',anchor='w', font=('楷体',14))
        self.Label3 = Label(self.top, text='高或低热量：', style='Label3.TLabel')
        self.Label3.place(relx=0.154, rely=0.537, relwidth=0.257, relheight=0.067)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.463, rely=0.141, relwidth=0.345, relheight=0.088)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='Text2', textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.463, rely=0.339, relwidth=0.345, relheight=0.088)

        self.Text3Var = StringVar(value='Text3')
        self.Text3 = Entry(self.top, text='Text3', textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.463, rely=0.537, relwidth=0.345, relheight=0.088)

        self.style.configure('Command1.TButton',font=('楷体',14))
        self.Command1 = Button(self.top, text='确认', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.394, rely=0.763, relwidth=0.191, relheight=0.117)
        
    def Command1_Cmd(self, event=None):
        self.recommendation_search_in_db()

    def recommendation_search_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        cursor.execute("call recommendation('%s','%s','%s');" % (self.Text1.get(),self.Text2.get(),self.Text3.get()))
        data = cursor.fetchall()
        for row in data:
            fno = row[0]
            fname = row[1]
            main_material1 = row[2]
            main_material2 = row[3]
            score = row[4]
            showinfo("查询结果","fno=%s,fname=%s,main_material1=%s,main_material2=%s,score=%s" % (fno,fname,main_material1,main_material2,score))

        db.close()
        self.top.destroy()
        cp.customer_page().__init__()
