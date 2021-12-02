from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import pymysql
import customer_page as cp

class rate(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('菜品打分评价')
        self.master.geometry('372x303')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        global img0
        self.style.configure('Label4.TLabel',anchor='center', justify='center')
        photo = Image.open("E:/新桌面/ttttt/pic2.jpg")
        photo = photo.resize((372,303))
        img0 = ImageTk.PhotoImage(photo)
        self.Label4 = Label(self.top, image=img0, style='Label4.TLabel')
        self.Label4.pack()

        self.style.configure('Label1.TLabel',anchor='w', font=('楷体',14))
        self.Label1 = Label(self.top, text='菜号：', style='Label1.TLabel')
        self.Label1.place(relx=0.151, rely=0.211, relwidth=0.161, relheight=0.089)

        self.style.configure('Label2.TLabel',anchor='w', font=('楷体',14))
        self.Label2 = Label(self.top, text='分数：', style='Label2.TLabel')
        self.Label2.place(relx=0.151, rely=0.422, relwidth=0.161, relheight=0.089)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.344, rely=0.211, relwidth=0.39, relheight=0.083)

        self.Combo1List = ['0','1']
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('宋体',9))
        self.Combo1.place(relx=0.344, rely=0.422, relwidth=0.39, relheight=0.066)
        self.Combo1.set(self.Combo1List[0])

        self.style.configure('Label3.TLabel',anchor='w', font=('楷体',12))
        self.Label3 = Label(self.top, text='提示：若喜欢该菜品，则为1分；不喜欢则为0分。', style='Label3.TLabel')
        self.Label3.place(relx=0.151, rely=0.554, relwidth=0.583, relheight=0.109)

        self.style.configure('Command1.TButton',font=('楷体',14))
        self.Command1 = Button(self.top, text='确认', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.387, rely=0.739, relwidth=0.239, relheight=0.109)
        
    def Command1_Cmd(self, event=None):
        self.rate_in_db()
		
    def rate_in_db(self):
        global db
        try:
            db = pymysql.connect("139.9.119.34", "s2018302465", "GaussDB@123", "db_2018302465")
        except:
            messagebox.showarning('警告', '连接数据库失败！')
        cursor = db.cursor()
        sql = "call rate(%d, %d);" % (int(self.Text1.get()), int(self.Combo1.get()))
        try:
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo('完成', '已成功为菜品打分!')
        except pymysql.err.OperationalError as err:
            print("发生异常", err)
            messagebox.showinfo('异常', err)
            db.rollback()
        db.close()
        self.top.destroy()
        cp.customer_page().__init__()
