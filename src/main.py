from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
import identity1 as iden1
import pymysql
import customer_page as cp

class home_page(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('大学餐厅菜品及服务管理系统首页')
        self.master.geometry('820x538')
        self.createWidgets()
        
    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        global photo
        self.style.configure('Label3.TLabel',anchor='center', justify='center')
        photo = PhotoImage(file="E:/新桌面/ttttt/background1.png")
        self.Label3 = Label(self.top, image=photo, style='Label3.TLabel')
        self.Label3.pack()
        
        self.style.configure('Command3.TButton',font=('楷体',16))
        self.Command3 = Button(self.top, text='退出', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.873, rely=0.917, relwidth=0.119, relheight=0.065)

        self.style.configure('Command2.TButton',font=('楷体',18))
        self.Command2 = Button(self.top, text='我是餐厅管理人员', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.507, rely=0.669, relwidth=0.255, relheight=0.061)

        self.style.configure('Command1.TButton',font=('楷体',18))
        self.Command1 = Button(self.top, text='我是顾客', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.234, rely=0.669, relwidth=0.255, relheight=0.061)

        self.style.configure('Label1.TLabel',anchor='center', font=('楷体',18))
        self.Label1 = Label(self.top, text='请选择您的身份？', style='Label1.TLabel')
        self.Label1.place(relx=0.39, rely=0.461, relwidth=0.235, relheight=0.059)

        self.style.configure('Label2.TLabel',anchor='center', font=('楷体',26))
        self.Label2 = Label(self.top, text='大学餐厅菜品及服务管理系统', style='Label2.TLabel')
        self.Label2.place(relx=0.205, rely=0.193, relwidth=0.572, relheight=0.095)
        
    def Command3_Cmd(self, event=None):
        if askokcancel("确认","是否退出？"):
            top.destroy()

    def Command2_Cmd(self, event=None):
        top.destroy()
        iden1.identity1()

    def Command1_Cmd(self, event=None):
        top.destroy()
        cp.customer_page()
        
if __name__ == "__main__":
    top = Tk()
    home_page(top).mainloop()
