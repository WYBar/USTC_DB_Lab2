import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
from PIL import Image, ImageTk

class StudentView:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁子界面
        self.student_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息管理系统学生端')
        self.window.geometry('500x600')

        label = Label(self.window, text="学生信息管理系统学生端", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="基础信息", font=tkFont.Font(size=16),
               command=lambda: BasicInfo(self.window, self.student_id), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="课程成绩", font=tkFont.Font(size=16),
               command=lambda: GradeInfo(self.window, self.student_id), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="课程信息", font=tkFont.Font(size=16),
               command=lambda: CourseInfo(self.window, self.student_id), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="奖惩情况", font=tkFont.Font(size=16),
               command=lambda: RewardInfo(self.window, self.student_id), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="修改密码", width=8, font=tkFont.Font(size=16),
               command=lambda: Changekey(self.window, self.student_id)).pack(pady=25)

        self.window.mainloop()  # 主消息循环

class BasicInfo:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.student_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息')
        self.window.geometry('300x570')  # 这里的乘是小x

        label = tk.Label(self.window, text='学生信息查看', bg='silver', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        self.id = '学号:' + ''
        self.name = '姓名:' + ''
        self.gender = '性别:' + ''
        self.age = '年龄:' + ''
        self.cname = '班级:' + ''
        self.mname = '专业:' + ''
        self.dname = '学院:' + ''
        self.image = None
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM BasicInfo WHERE sid = '%s'" % (student_id)  # SQL 查询语句
        sqlimg = "SELECT photo FROM student WHERE sid = '%s'" % (student_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id = '学号:' + row[0]
                self.name = '姓名:' + row[1]
                self.gender = '性别:' + row[2]
                self.age = '年龄:' + row[3]
                self.cname = '班级:' + row[4]
                self.mname = '专业:' + row[5]
                self.dname = '学院:' + row[6]

            cursor.execute(sqlimg)
            result = cursor.fetchone()
            if result:
                print('result IS NOT NULL')
                with open('temp.jpg', 'wb') as f:
                    f.write(result[0])
                self.image = result[0]
            else:
                print('result IS NULL')
                self.image = None
        except:
            print("Error: unable to fetch data")
        db.close()  # 关闭数据库连接

        if self.image is None:
            img = Image.open("./PB21151765.jpg")
            img = img.resize((70, 100), Image.Resampling.BILINEAR)
        else:
            img = Image.open("./temp.jpg")
            img = img.resize((70, 100), Image.Resampling.BILINEAR)
        photo = ImageTk.PhotoImage(img)
        Label(self.window, image=photo, width=70, height=100).pack(expand=True, fill='both', pady=3)
        Label(self.window, text=self.id, font=('Verdana', 16)).pack(pady=3)
        Label(self.window, text=self.name, font=('Verdana', 16)).pack(pady=3)
        Label(self.window, text=self.gender, font=('Verdana', 16)).pack(pady=3)
        Label(self.window, text=self.age, font=('Verdana', 16)).pack(pady=3)
        Label(self.window, text=self.cname, font=('Verdana', 16)).pack(pady=3)
        Label(self.window, text=self.mname, font=('Verdana', 16)).pack(pady=3)
        Label(self.window, text=self.dname, font=('Verdana', 16)).pack(pady=3)

        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=16),
               command=self.back).pack(pady=25)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StudentView(self.window, self.student_id)  # 显示主窗口 销毁本窗口

class GradeInfo:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.student_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('成绩信息')
        self.window.geometry('550x500')  # 这里的乘是小x
        self.frame_top = tk.Frame(width=520, height=50)
        self.frame_center = tk.Frame(width=520, height=300)
        self.frame_down = tk.Frame(width=520, height=50)

        label = tk.Label(self.frame_top, text='成绩信息查看', bg='silver', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        # 定义下方中心列表区域
        self.columns = ("学号", "课程号", "课程名", "教师名", "学分", "成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=90, anchor='center')  # 表示列,不显示
        self.tree.column("课程号", width=60, anchor='center')
        self.tree.column("课程名", width=120, anchor='center')
        self.tree.column("教师名", width=100, anchor='center')
        self.tree.column("学分", width=60, anchor='center')
        self.tree.column("成绩", width=70, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.sid = []
        self.cid = []
        self.cname = []
        self.tname = []
        self.credit = []
        self.score = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM ScoreInfo WHERE sid = '%s'" % (student_id) # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.sid.append(row[0])
                self.cid.append(row[1])
                self.cname.append(row[2])
                self.tname.append(row[3])
                self.credit.append(row[4])
                self.score.append(row[5])
            # print(self.id)
            # print(self.name)
            # print(self.gender)
            # print(self.age)
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(len(self.sid)):  # 写入数据
            self.tree.insert('', i, values=(self.sid[i], self.cid[i], self.cname[i], self.tname[i],
                                            self.credit[i], self.score[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        Button(self.frame_down, text="返回首页", width=8, font=tkFont.Font(size=16),
               command=self.back).pack(pady=5)

        self.frame_top.grid(row=0, column=0, columnspan=2, padx=4, pady=5)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_down.grid(row=2, column=0, columnspan=2, padx=4, pady=5)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_down.grid_propagate(0)
        self.frame_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_down.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def back(self):
        StudentView(self.window, self.student_id)  # 显示主窗口 销毁本窗口

class CourseInfo:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.student_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('课程信息')
        self.window.geometry('550x500')  # 这里的乘是小x
        self.frame_top = tk.Frame(width=430, height=50)
        self.frame_center = tk.Frame(width=430, height=300)
        self.frame_down = tk.Frame(width=430, height=50)

        label = tk.Label(self.frame_top, text='课程信息', bg='silver', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        # 定义下方中心列表区域
        self.columns = ("课程号", "课程名", "教师号", "教师名", "学分")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程号", width=60, anchor='center')
        self.tree.column("课程名", width=120, anchor='center')
        self.tree.column("教师号", width=70, anchor='center')
        self.tree.column("教师名", width=100, anchor='center')
        self.tree.column("学分", width=60, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.cid = []
        self.cname = []
        self.tid = []
        self.tname = []
        self.credit = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM CourseInfo"# SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.cid.append(row[0])
                self.cname.append(row[1])
                self.tid.append(row[2])
                self.tname.append(row[3])
                self.credit.append(row[4])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(len(self.cid)):  # 写入数据
            self.tree.insert('', i, values=(self.cid[i], self.cname[i], self.tid[i], self.tname[i],
                                            self.credit[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        Button(self.frame_down, text="返回首页", width=8, font=tkFont.Font(size=16),
               command=self.back).pack(pady=5)

        self.frame_top.grid(row=0, column=0, columnspan=2, padx=4, pady=5)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_down.grid(row=2, column=0, columnspan=2, padx=4, pady=5)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_down.grid_propagate(0)
        self.frame_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_down.tkraise()



        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def back(self):
        StudentView(self.window, self.student_id)  # 显示主窗口 销毁本窗口

class RewardInfo:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.student_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('奖惩信息')
        self.window.geometry('550x500')  # 这里的乘是小x
        self.frame_top = tk.Frame(width=400, height=50)
        self.frame_center = tk.Frame(width=400, height=200)
        self.frame_down = tk.Frame(width=400, height=50)

        label = tk.Label(self.frame_top, text='奖惩信息查看', bg='silver', font=('Verdana', 20), width=30, height=2)
        label.pack(pady=20)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "奖惩", "类型")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=90, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=90, anchor='center')
        self.tree.column("奖惩", width=120, anchor='center')
        self.tree.column("类型", width=80, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.sid = []
        self.sname = []
        self.reward = []
        self.type = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM RewardInfo WHERE sid = '%s'" % (student_id)  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.sid.append(row[0])
                self.sname.append(row[1])
                self.reward.append(row[2])
                self.type.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(len(self.sid)):  # 写入数据
            self.tree.insert('', i, values=(self.sid[i], self.sname[i], self.reward[i], self.type[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        Button(self.frame_down, text="返回首页", width=8, font=tkFont.Font(size=16),
               command=self.back).pack(pady=5)

        self.frame_top.grid(row=0, column=0, columnspan=2, padx=4, pady=5)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_down.grid(row=2, column=0, columnspan=2, padx=4, pady=5)
        self.frame_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_down.grid_propagate(0)
        self.frame_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_down.tkraise()

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def back(self):
        StudentView(self.window, self.student_id)  # 显示主窗口 销毁本窗口

class Changekey:
    def __init__(self, parent_window, student_id):
        parent_window.destroy()  # 销毁主界面
        self.student_id = student_id

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生账号修改页面')
        self.window.geometry('300x550')  # 这里的乘是小x

        label = tk.Label(self.window, text='修改学生密码', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='学号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_id.pack()

        Label(self.window, text='旧密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_key = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_key.pack()

        Label(self.window, text='新密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="确定修改", width=8, font=tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

    def login(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_key.get()))
        stu_pass = None
        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')  # 打开数据库连接   已经修正删除多余空格
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM stu_login_k WHERE stu_id = '%s'" % (self.admin_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                stu_id = row[0]
                stu_pass = row[1]
                # 打印结果
                print("stu_id=%s,stu_pass=%s" % (stu_id, stu_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在修改")
        print("旧密码", self.admin_key.get())
        print("新密码", stu_pass)

        if self.admin_key.get() == stu_pass:
            self.change()
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def change(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_key.get()))
        print(str(self.admin_pass.get()))
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "UPDATE stu_login_k SET stu_pass = '%s' WHERE stu_id = '%s'" % (
            self.admin_pass.get(), self.admin_id.get())
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '更新成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
        db.close()  # 关闭数据库连接

    def back(self):
        StudentView(self.window, self.student_id)  # 显示主窗口 销毁本窗口

