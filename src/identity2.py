from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import pymysql
import select_food_table as sft
import select_score_table as sscoret
import select_usr_table as sut
import select_customer_table as sct
import select_sell_table as ssellt
import change_food_table as cft
import change_customer_table as cct

class identity2(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('餐厅管理人员界面')
        self.master.geometry('889x509')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        self.style.configure('Frame2.TLabelframe',font=('楷体',15))
        self.Frame2 = LabelFrame(self.top, text='修改', style='Frame2.TLabelframe')
        self.Frame2.place(relx=0.504, rely=0., relwidth=0.487, relheight=0.992)

        self.style.configure('Frame1.TLabelframe',font=('楷体',15))
        self.Frame1 = LabelFrame(self.top, text='查看', style='Frame1.TLabelframe')
        self.Frame1.place(relx=0.009, rely=0., relwidth=0.487, relheight=0.992)
        
        self.style.configure('Command1.TButton',font=('楷体',14))
        self.Command10 = Button(self.Frame2, text='修改用户信息表', command=self.Command10_Cmd, style='Command1.TButton')
        self.Command10.place(relx=0.296, rely=0.792, relwidth=0.39, relheight=0.065)

        self.Command9 = Button(self.Frame2, text='修改打分信息表', command=self.Command9_Cmd, style='Command1.TButton')
        self.Command9.place(relx=0.296, rely=0.618, relwidth=0.39, relheight=0.065)

        self.Command8 = Button(self.Frame2, text='修改售卖信息表', command=self.Command8_Cmd, style='Command1.TButton')
        self.Command8.place(relx=0.296, rely=0.456, relwidth=0.39, relheight=0.065)

        self.Command7 = Button(self.Frame2, text='修改顾客信息表', command=self.Command7_Cmd, style='Command1.TButton')
        self.Command7.place(relx=0.296, rely=0.283, relwidth=0.39, relheight=0.065)

        self.Command6 = Button(self.Frame2, text='修改菜品信息表', command=self.Command6_Cmd, style='Command1.TButton')
        self.Command6.place(relx=0.296, rely=0.127, relwidth=0.39, relheight=0.065)

        self.Command5 = Button(self.Frame1, text='查看售卖信息表', command=self.Command5_Cmd, style='Command1.TButton')
        self.Command5.place(relx=0.296, rely=0.456, relwidth=0.39, relheight=0.065)

        self.Command4 = Button(self.Frame1, text='查看顾客信息表', command=self.Command4_Cmd, style='Command1.TButton')
        self.Command4.place(relx=0.296, rely=0.283, relwidth=0.39, relheight=0.065)

        self.Command3 = Button(self.Frame1, text='查看用户信息表', command=self.Command3_Cmd, style='Command1.TButton')
        self.Command3.place(relx=0.296, rely=0.792, relwidth=0.39, relheight=0.065)

        self.Command2 = Button(self.Frame1, text='查看打分信息表', command=self.Command2_Cmd, style='Command1.TButton')
        self.Command2.place(relx=0.296, rely=0.618, relwidth=0.39, relheight=0.065)

        self.Command1 = Button(self.Frame1, text='查看菜品信息表', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.296, rely=0.127, relwidth=0.39, relheight=0.065)

    def Command1_Cmd(self, event=None):
        sft.select_food_table()
    
    def Command2_Cmd(self, event=None):
        sscoret.select_score_table()
        
    def Command3_Cmd(self, event=None):
        sut.select_usr_table()
    
    def Command4_Cmd(self, event=None):
        sct.select_customer_table()
        
    def Command5_Cmd(self, event=None):
        ssellt.select_sell_table()
    
    def Command6_Cmd(self, event=None):
        cft.change_food_table()
        
    def Command7_Cmd(self, event=None):
        cct.change_customer_table()
    
    def Command8_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass
        
    def Command9_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass
    
    def Command10_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass
