from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql
import select_food_table as sft
import select_score_table as sscoret
import rate
import select_customer_table as sct
import recommendation
import insert_customer_table as ict

class customer_page(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('顾客界面')
        self.master.geometry('714x496')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Frame4.TLabelframe',font=('楷体',15))
        self.Frame4 = LabelFrame(self.top, text='顾客信息', style='Frame4.TLabelframe')
        self.Frame4.place(relx=0.493, rely=0.339, relwidth=0.494, relheight=0.647)

        self.style.configure('Frame3.TLabelframe',font=('楷体',15))
        self.Frame3 = LabelFrame(self.top, text='推荐', style='Frame3.TLabelframe')
        self.Frame3.place(relx=0.011, rely=0.645, relwidth=0.472, relheight=0.341)

        self.style.configure('Frame2.TLabelframe',font=('楷体',15))
        self.Frame2 = LabelFrame(self.top, text='打分', style='Frame2.TLabelframe')
        self.Frame2.place(relx=0.493, rely=0., relwidth=0.494, relheight=0.341)

        self.style.configure('Frame1.TLabelframe',font=('楷体',15))
        self.Frame1 = LabelFrame(self.top, text='查看', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.011, rely=0., relwidth=0.472, relheight=0.647)

        self.style.configure('Command2.TButton',font=('楷体',14))
        self.Command2 = Button(self.Frame2, text='菜品打分评价', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.272, rely=0.426, relwidth=0.433, relheight=0.243)

        self.style.configure('Command1.TButton',font=('楷体',14))
        self.Command1 = Button(self.Frame1, text='查看菜品信息', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.261, rely=0.274, relwidth=0.454, relheight=0.128)

        self.style.configure('Command3.TButton',font=('楷体',14))
        self.Command3 = Button(self.Frame4, text='添加顾客信息', command=self.Command3_Cmd, style='Command4.TButton')
        self.Command3.place(relx=0.272, rely=0.623, relwidth=0.433, relheight=0.128)
        
        self.style.configure('Command6.TButton',font=('楷体',14))
        self.Command6 = Button(self.top, text='查看菜品推荐', command=self.Command6_Cmd, style='Command6.TButton')
        self.Command6.place(relx=0.134, rely=0.79, relwidth=0.214, relheight=0.083)

        self.style.configure('Command4.TButton',font=('楷体',14))
        self.Command4 = Button(self.top, text='查看顾客信息', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.627, rely=0.516, relwidth=0.214, relheight=0.083)

        self.style.configure('Command5.TButton',font=('楷体',14))
        self.Command5 = Button(self.top, text='查看打分信息', command=self.Command5_Cmd, style='Command5.TButton')
        self.Command5.place(relx=0.134, rely=0.419, relwidth=0.214, relheight=0.083)

    def Command5_Cmd(self, event=None):
        sscoret.select_score_table()

    def Command4_Cmd(self, event=None):
        sct.select_customer_table()

    def Command6_Cmd(self, event=None):
        recommendation.recommendation()

    def Command1_Cmd(self, event=None):
        sft.select_food_table()

    def Command2_Cmd(self, event=None):
        rate.rate()

    def Command3_Cmd(self, event=None):
        ict.insert_customer_table()

