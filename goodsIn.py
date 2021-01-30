# coding = utf-8 
import tkinter as tk
import tkinter.messagebox as msg
# import search
import begin
from tkinter import ttk
import pymysql
def frame():
    global win
    win = tk.Tk()
    win.title('新增进货数据')
    win.geometry('1000x900')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='请填写粮食进货信息:', font=('微软雅黑', 20)).place(x=30, y=100)

    tk.Label(win, text='进货地：', font=('宋体', 12)).place(x=30, y=200)
    global list_place#这个是一个下拉页表项，只能从下面的list['values']里边选
    comvalue1 = tk.StringVar()
    list_place = ttk.Combobox(win, textvariable=comvalue1, height=10, width=10)
    list_place.place(x=100, y=200)
    list_place['values'] = ('全部', '山东', '赣榆', '其他')
    list_place.current(0)#默认显示'全部'

    tk.Label(win, text='货名：', font=('宋体', 12)).place(x=200, y=200)
    global list_goods#这个是一个下拉页表项，只能从下面的list['values']里边选
    comvalue2 = tk.StringVar()
    list_goods = ttk.Combobox(win, textvariable=comvalue2, height=10, width=10)
    list_goods.place(x=250, y=200)
    list_goods['values'] = ('全部', '大米', '面粉', '本地花生油')
    list_goods.current(0)#默认显示'全部'

    global author
    tk.Label(win, text='进价（元）：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(win, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    global num
    tk.Label(win, text='数量：', font=('宋体', 12)).place(x=350, y=200)
    num = tk.Entry(win, font=('宋体', 12), width=10)
    num.place(x=400, y=200)

    global priced
    tk.Label(win, text='批发价：', font=('宋体', 12)).place(x=500, y=200)
    price = tk.Entry(win, font=('宋体', 12), width=10)
    price.place(x=570, y=200)

    global amount
    tk.Label(win, text='零售价：', font=('宋体', 12)).place(x=650, y=200)
    amount = tk.Entry(win, font=('宋体', 12), width=10)
    amount.place(x=710, y=200)

    tk.Button(win, text='确认添加', font=('宋体', 12), width=10, command=add).place(x=900, y=195)
    tk.Button(win, text='查询', font=('宋体', 12), width=10).place(x=800, y=195)
    tk.Button(win, text='返回', font=('宋体', 12), width=10, command=reback).place(x=0, y=50)

    win.mainloop()

def reback():
    win.destroy()
    begin.frame()

#添加图书信息到数据库中
def add():
    print('新增成功啦')
#     # sql="INSERT INTO book VALUES('%s','%s','%s','%s','%s')"% (list.get(),b_name.get(),author.get(),price.get(),amount.get())
#     # db = pymysql.connect("localhost", "root", "qwer", "library")
#     # cursor = db.cursor()
#     # cursor.execute(sql)
#     # db.commit()#这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
#     # db.close()
#     # msg.showinfo(title='成功！', message='新书已入库！')
#
def cancel():#查询数据
    frame()
#     global win
#     win = tk.Tk()
#     win.title('管理员')
#     win.geometry('900x300')
#     win.wm_attributes('-topmost', 1)
#     lable1 = tk.Label(win, text='请填写注销图书的信息:', font=('微软雅黑', 20)).place(x=30, y=100)
#
#     tk.Label(win, text='图书类目：', font=('宋体', 12)).place(x=30, y=200)
#     global list
#     comvalue = tk.StringVar()
#     list = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
#     list.place(x=100, y=200)
#     list['values'] = ('全部', '人文', '艺术', '计算机', '科技', '杂志')
#     list.current(0)
#
#     global b_name
#     tk.Label(win, text='书名：', font=('宋体', 12)).place(x=200, y=200)
#     b_name = tk.Entry(win, font=('宋体', 12), width=10)
#     b_name.place(x=250, y=200)
#
#     global author
#     tk.Label(win, text='作者：', font=('宋体', 12)).place(x=350, y=200)
#     author = tk.Entry(win, font=('宋体', 12), width=10)
#     author.place(x=400, y=200)
#
#     tk.Button(win, text='确认注销', font=('宋体', 12), width=10, command=delete).place(x=600, y=195)
#
def delete(): # 删除图书
    frame()
#     sql = "DELETE FROM book WHERE type='%s' AND name='%s' AND author='%s'" % (list.get(),b_name.get(),author.get())
#     db = pymysql.connect("localhost", "root", "qwer", "library")
#     cursor = db.cursor()
#     cursor.execute(sql)
#     db.commit()#这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
#     msg.showinfo(title='成功！', message='该书已删除！')