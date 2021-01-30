import tkinter as tk
import goodsIn
import goodsSell

def frame():#初始界面
    global root
    root=tk.Tk()
    root.geometry('700x700')
    root.title('欢迎来到四姨的粮店')
    # lable0=tk.Label(root, text='欢迎来到四姨的粮店',bg='pink',font=('微软雅黑',30)).pack()#上
    # #canvas是个画布，想要插入图片的话首先要定义个canvas
    # canvas=tk.Canvas(root,height=300,width=300)#中
    # image_file=tk.PhotoImage(file='resourse/door.gif')
    # #图片文件的后缀必须是.gif，且亲测不能自行鼠标右键重命名更改成.gif，要用win10里内置的画图功能，打开图片然后另存为的时候选择.gif
    # #图片文件必须放到你的项目目录里边才有效
    # image=canvas.create_image(250,100,image=image_file)
    # canvas.place(x=170,y=170)

    # lable1=tk.Label(root,text='请选择用户类型:',font=('微软雅黑',20)).place(x=20,y=320)#下
    tk.Button(root, text='进货管理',font=('微软雅黑',15),width=10, height=2,command=goodsIn_in).place(x=300, y=100)
    tk.Button(root, text='出售登记',font=('微软雅黑',15),width=10, height=2,command=goodsSell_in).place(x=300, y=200)

    root.mainloop()#必须要有这句话，你的页面才会动态刷新循环，否则页面不会显示

def goodsIn_in():#跳转至读者界面
    root.destroy()
    goodsIn.frame()

def goodsSell_in():#跳转至管理员界面
    root.destroy()
    goodsSell.frame()

if __name__ == '__main__':
    frame()
