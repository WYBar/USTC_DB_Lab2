import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

# 管理员操作界面
class AdminManage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁子界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('学生信息管理系统管理端')
        self.window.geometry('500x600')

        label = Label(self.window, text="学生信息管理系统管理端", font=("Verdana", 20))
        label.pack(pady=100)  # pady=100 界面的长度

        Button(self.window, text="基础信息", font=tkFont.Font(size=16),
               command=lambda: BasicInfo(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="课程成绩", font=tkFont.Font(size=16),
               command=lambda: ScoreInfo(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="课程信息", font=tkFont.Font(size=16),
               command=lambda: CourseInfo(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="奖惩情况", font=tkFont.Font(size=16),
               command=lambda: RewardInfo(self.window), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        # Button(self.window, text="修改密码", width=8, font=tkFont.Font(size=16),
        #        command=lambda: Changekey(self.window, self.student_id)).pack(pady=25)

        self.window.mainloop()  # 主消息循环

class BasicInfo:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('学生信息操作界面')

        self.frame_left_top = tk.Frame(width=350, height=300)
        self.frame_right_top = tk.Frame(width=280, height=270)
        self.frame_center = tk.Frame(width=600, height=250)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "年龄", "班级", "专业", "学院")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=70, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=70, anchor='center')
        self.tree.column("性别", width=50, anchor='center')
        self.tree.column("年龄", width=50, anchor='center')
        self.tree.column("班级", width=110, anchor='center')
        self.tree.column("专业", width=120, anchor='center')
        self.tree.column("学院", width=120, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.sid = []
        self.sname = []
        self.gender = []
        self.age = []
        self.clid = []
        self.mname = []
        self.dname = []
        self.views = [self.sid, self.sname, self.gender, self.age, self.clid, self.mname, self.dname]
        self.select_view(self.views)

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.columns = ("学号", "姓名", "性别", "年龄", "班级", "专业", "学院")
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_sid = StringVar()  # 声明学号
        self.var_sname = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        self.var_clid = StringVar()  # 声明年龄
        self.var_mname = StringVar()  # 声明年龄
        self.var_dname = StringVar()  # 声明年龄
        self.vars = [self.var_sid, self.var_sname, self.var_gender, self.var_age,
                     self.var_clid, self.var_mname, self.var_dname]

        for i, (text, var) in enumerate(zip(self.columns, self.vars)):
            label = Label(self.frame_left_top, text=text + "：", font=('Verdana', 13))
            entry = Entry(self.frame_left_top, textvariable=var, font=('Verdana', 13))
            label.grid(row=i+1, column=0)
            entry.grid(row=i+1, column=1)

        label = Label(self.frame_left_top, text="照片：", font=('Verdana', 13))
        self.entry_photo = Entry(self.frame_left_top, font=('Verdana', 13))
        label.grid(row=len(self.columns)+1, column=0)
        self.entry_photo.grid(row=len(self.columns)+1, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 16))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中学生信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中学生信息', width=20,
                                            command=self.del_row)
        self.right_top_button6 = ttk.Button(self.frame_right_top, text='返回首页', width=20,
                                            command=self.back)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='选择图片', width=20, command=self.select_photo)
        self.right_top_button5 = ttk.Button(self.frame_right_top, text='查看所选学生信息', width=20,
                                            command=lambda: BasicInfo_show(self.window, self.var_sid.get()))

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=3)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=3)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=3)
        self.right_top_button6.grid(row=5, column=0, padx=20, pady=3)
        self.right_top_button4.grid(row=6, column=0, padx=20, pady=3)
        self.right_top_button5.grid(row=7, column=0, padx=20, pady=3)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=17, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=15, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=0)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        for i, row_item in enumerate(self.row_info):
            self.vars[i].set(row_item)
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_sid,
                                        font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def select_view(self, views):
        for view in views:
            view.clear()
        count = 0
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = """SELECT
  s.sid AS sid,
  s.sname AS sname,
  s.gender AS gender,
  s.age AS age,
  cl.class_id AS cid,
  m.mname AS mname,
  d.dname AS dname
FROM
  student s
  JOIN class cl ON s.class_id = cl.class_id
  JOIN major m ON cl.mname = m.mname
  JOIN department d ON m.dname = d.dname
  ORDER BY sid ASC;"""  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            count = len(results)
            for row in results:
                for i, view in enumerate(views):
                    view.append(row[i])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("select_view")
        print(count)
        self.tree.delete(*self.tree.get_children())
        for i in range(count):  # 写入数据
            values = []
            for view in views:
                values.append(view[i])
            self.tree.insert('', i, values=tuple(values))
        self.tree.update()

    def select_photo(self):
        filepath = askopenfilename(filetypes=[("Image Files", "*png;*.jpg;*.jpeg")])
        if filepath:
            self.entry_photo.delete(0, END)
            self.entry_photo.insert(0, filepath)

    def new_row(self):
        print('new')
        print(self.var_sid.get())
        if str(self.var_sid.get()) in self.sid:
            messagebox.showinfo('警告！', '该学生已存在！')
        else:
            if (self.var_sid.get() != '' and self.var_sname.get() != '' and self.var_gender.get() != ''
                    and self.var_age.get() != '' and self.var_clid.get() != ''):
                if self.entry_photo.get():
                    with open(self.entry_photo.get(), 'rb') as f:
                        img = f.read()
                else:
                    img = None
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "CALL INSERT_STU(%s, %s, %s, %s, %s, %s)"  # SQL 插入语句
                try:
                    cursor.execute(sql, (self.var_sid.get(), self.var_sname.get(), self.var_gender.get(),
                       self.var_age.get(), self.var_clid.get(), img))  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '插入失败！')
                db.close()  # 关闭数据库连接

                self.select_view(self.views)
            else:
                messagebox.showinfo('警告！', '请填写学生数据')

    def updata_row(self):
        print('update')
        print(self.var_sid.get())
        if self.var_sid.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
            with open(self.entry_photo.get(), 'rb') as f:
                img = f.read()
            db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_update = "CALL UPDATE_STU(%s, %s, %s, %s, %s, %s)"
            try:
                cursor.execute(sql_update, (self.var_sid.get(), self.var_sname.get(), self.var_gender.get(),
                       self.var_age.get(), self.var_clid.get(), img))  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败！')
            db.close()  # 关闭数据库连接

            self.select_view(self.views)
        else:
            messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        print('delete')
        print(self.var_sid.get())
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql_delete = "CALL DELETE_STU('%s')" % \
                      (self.var_sid.get())
        try:
            cursor.execute(sql_delete)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '删除成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '删除失败！')
        db.close()  # 关闭数据库连接

        self.select_view(self.views)
        print(self.tree.get_children())

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

class CourseInfo:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('课程操作界面')

        self.frame_left_top = tk.Frame(width=300, height=300)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=500, height=250)
        self.frame_bottom = tk.Frame(width=550, height=50)

        # 定义下方中心列表区域
        self.columns = ("课程号", "课程名", "教师号", "教师名", "学分")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程号", width=70, anchor='center')  # 表示列,不显示
        self.tree.column("课程名", width=120, anchor='center')
        self.tree.column("教师号", width=70, anchor='center')
        self.tree.column("教师名", width=100, anchor='center')
        self.tree.column("学分", width=80, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.cid = []
        self.cname = []
        self.tid = []
        self.tname = []
        self.credit = []
        self.views = [self.cid, self.cname, self.tid, self.tname, self.credit]
        self.select_view(self.views)

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.columns = ("课程号", "课程名", "教师号", "教师名", "学分")
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_cid = StringVar()  # 声明学号
        self.var_cname = StringVar()  # 声明姓名
        self.var_tid = StringVar()  # 声明性别
        self.var_tname = StringVar()  # 声明年龄
        self.var_credit = StringVar()  # 声明年龄
        self.vars = [self.var_cid, self.var_cname, self.var_tid, self.var_tname,
                     self.var_credit]

        for i, (text, var) in enumerate(zip(self.columns, self.vars)):
            label = Label(self.frame_left_top, text=text + "：", font=('Verdana', 16))
            entry = Entry(self.frame_left_top, textvariable=var, font=('Verdana', 16))
            label.grid(row=i + 1, column=0, padx=10)
            entry.grid(row=i + 1, column=0)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 16))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建课程信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中课程信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中课程信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20,
                                            command=self.back)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=3)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=3)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=3)
        self.right_top_button4.grid(row=5, column=0, padx=20, pady=3)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=17, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=15, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=0)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        for i, row_item in enumerate(self.row_info):
            self.vars[i].set(row_item)
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_cid,
                                        font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def select_view(self, views):
        for view in views:
            view.clear()
        count = 0
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = """SELECT
  c.cid AS cid,
  c.cname AS cname,
  t.tid AS tid,
  t.tname AS tname,
  c.credit AS credit
FROM
  course c JOIN teacher t ON c.tid = t.tid
  ORDER BY cid ASC;"""  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            count = len(results)
            for row in results:
                for i, view in enumerate(views):
                    view.append(row[i])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("select_view")
        print(count)
        self.tree.delete(*self.tree.get_children())
        for i in range(count):  # 写入数据
            values = []
            for view in views:
                values.append(view[i])
            self.tree.insert('', i, values=tuple(values))
        self.tree.update()

    def new_row(self):
        print('new')
        print(self.var_cid.get())
        if str(self.var_cid.get()) in self.cid:
            messagebox.showinfo('警告！', '该学生已存在！')
        else:
            if (self.var_cid.get() != '' and self.var_cname.get() != '' and self.var_tid.get() != ''
                    and self.var_tname.get() != '' and self.var_credit.get() != ''):
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "CALL INSERT_COU('%s', '%s', '%s', '%s', '%s')" % \
                      (self.var_cid.get(), self.var_cname.get(), self.var_tid.get(),
                       self.var_tname.get(), self.var_credit.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '插入失败！')
                db.close()  # 关闭数据库连接

                self.select_view(self.views)
            else:
                messagebox.showinfo('警告！', '请填写课程数据')

    def updata_row(self):
        print('update')
        print(self.var_cid.get())
        if self.var_cid.get() == self.row_info[0]:  # 如果所填学号 与 所选学号一致
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_update = "CALL UPDATE_COU('%s', '%s', '%s', '%s', '%s')" % \
                         (self.var_cid.get(), self.var_cname.get(), self.var_tid.get(),
                          self.var_tname.get(), self.var_credit.get())
            try:
                cursor.execute(sql_update)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败！')
            db.close()  # 关闭数据库连接

            self.select_view(self.views)
        else:
            messagebox.showinfo('警告！', '不能修改课程号！')

    def del_row(self):
        print('delete')
        print(self.var_cid.get())
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql_delete = "CALL DELETE_COU('%s')" % \
                     (self.var_cid.get())
        try:
            cursor.execute(sql_delete)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '删除成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '删除失败！')
        db.close()  # 关闭数据库连接

        self.select_view(self.views)

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

class RewardInfo:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('学生奖惩操作界面')

        self.frame_left_top = tk.Frame(width=250, height=200)
        self.frame_right_top = tk.Frame(width=200, height=200)
        self.frame_center = tk.Frame(width=400, height=250)
        self.frame_bottom = tk.Frame(width=450, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "奖惩", "类型")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=70, anchor='center')  # 表示列,不显示
        self.tree.column("姓名", width=70, anchor='center')
        self.tree.column("奖惩", width=120, anchor='center')
        self.tree.column("类型", width=70, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.sid = []
        self.sname = []
        self.content = []
        self.type = []
        self.views = [self.sid, self.sname, self.content, self.type]
        self.select_view(self.views)

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="奖惩信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.columns = ("学号", "姓名", "奖惩", "类型")
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_sid = StringVar()  # 声明学号
        self.var_sname = StringVar()  # 声明姓名
        self.var_content = StringVar()  # 声明性别
        self.var_type = StringVar()  # 声明年龄
        self.vars = [self.var_sid, self.var_sname, self.var_content, self.var_type]

        for i, (text, var) in enumerate(zip(self.columns, self.vars)):
            label = Label(self.frame_left_top, text=text + "：", font=('Verdana', 16))
            entry = Entry(self.frame_left_top, textvariable=var, font=('Verdana', 16))
            label.grid(row=i + 1, column=0)
            entry.grid(row=i + 1, column=0)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 16))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建奖惩信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='删除选中奖惩信息', width=20,
                                            command=self.del_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='查看所选学生奖惩信息', width=20,
                                            command=lambda: RewardInfo_show(self.window, self.var_sid.get()))
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='返回首页', width=20,
                                            command=self.back)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=3)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=3)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=3)
        self.right_top_button4.grid(row=5, column=0, padx=20, pady=3)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=17, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=15, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=0)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        for i, row_item in enumerate(self.row_info):
            self.vars[i].set(row_item)
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_sid,
                                        font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def select_view(self, views):
        for view in views:
            view.clear()
        count = 0
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = """SELECT
  s.sid AS sid,
  s.sname AS sname,
  rps.content AS content,
  rp.type AS type
FROM
  student s LEFT OUTER JOIN (reward_punish_student rps JOIN reward_punish rp ON rps.content = rp.content) ON s.sid = rps.sid
  ORDER BY sid ASC;"""  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            count = len(results)
            for row in results:
                for i, view in enumerate(views):
                    view.append(row[i])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("select_view")
        print(count)
        self.tree.delete(*self.tree.get_children())
        for i in range(count):  # 写入数据
            values = []
            for view in views:
                values.append(view[i])
            self.tree.insert('', i, values=tuple(values))
        self.tree.update()

    def new_row(self):
        print('new')
        print(self.var_sid.get())
        flag = 0
        seen = set()
        for i, (sid, content) in enumerate(zip(self.sid, self.content)):
            if (sid, content) in seen:
                flag = 1  # 发现重复项，设置标志为1
                break  # 退出循环
            else:
                seen.add((sid, content))  # 将当前遍历的元组添加到集合中
        if flag == 1:
            messagebox.showinfo('警告！', '该奖惩已存在！')
        else:
            if (self.var_sid.get() != '' and self.var_sname.get() != '' and self.var_content.get() != ''
                    and self.var_type.get() != ''):
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "CALL INSERT_REW('%s', '%s')" % \
                      (self.var_sid.get(), self.var_content.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '插入失败！')
                db.close()  # 关闭数据库连接

                self.select_view(self.views)
            else:
                messagebox.showinfo('警告！', '请填写奖惩数据')

    def del_row(self):
        print('delete')
        print(self.var_sid.get())
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql_delete = "CALL DELETE_REW('%s', '%s')" % \
                     (self.var_sid.get(), self.var_content.get())
        try:
            cursor.execute(sql_delete)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '删除成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '删除失败！')
        db.close()  # 关闭数据库连接

        self.select_view(self.views)
        print(self.tree.get_children())

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

class ScoreInfo:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('学生选课操作界面')

        self.frame_left_top = tk.Frame(width=250, height=300)
        self.frame_right_top = tk.Frame(width=250, height=250)
        self.frame_center = tk.Frame(width=550, height=250)
        self.frame_bottom = tk.Frame(width=680, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "课程号", "课程名", "老师名", "学分", "成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=70, anchor='center')  # 表示列,不显示
        self.tree.column("课程号", width=70, anchor='center')
        self.tree.column("课程名", width=120, anchor='center')
        self.tree.column("老师名", width=100, anchor='center')
        self.tree.column("学分", width=70, anchor='center')
        self.tree.column("成绩", width=80, anchor='center')

        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.sid = []
        self.cid = []
        self.cname = []
        self.tname = []
        self.credit = []
        self.score = []
        self.views = [self.sid, self.cid, self.cname, self.tname, self.credit, self.score]
        self.select_view(self.views)

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="选课信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_sid = StringVar()  # 声明学号
        self.var_cid = StringVar()  # 声明姓名
        self.var_cname = StringVar()  # 声明性别
        self.var_tname = StringVar()  # 声明年龄
        self.var_credit = StringVar()  # 声明年龄
        self.var_score = StringVar()  # 声明年龄
        self.vars = [self.var_sid, self.var_cid, self.var_cname, self.var_tname,
                     self.var_credit, self.var_score]

        for i, (text, var) in enumerate(zip(self.columns, self.vars)):
            label = Label(self.frame_left_top, text=text + "：", font=('Verdana', 16))
            entry = Entry(self.frame_left_top, textvariable=var, font=('Verdana', 16))
            label.grid(row=i+1, column=0)
            entry.grid(row=i+1, column=0)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 16))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建选课信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新成绩信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选课信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='查看所选学生成绩信息', width=20,
                                            command=lambda: GradeInfo_show(self.window, self.var_sid.get()))
        self.right_top_button5 = ttk.Button(self.frame_right_top, text='计算所选学生GPA', width=20,
                                            command=self.cal_gpa)
        self.right_top_button6 = ttk.Button(self.frame_right_top, text='返回首页', width=20,
                                            command=self.back)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=3)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=3)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=3)
        self.right_top_button4.grid(row=5, column=0, padx=20, pady=3)
        self.right_top_button5.grid(row=6, column=0, padx=20, pady=3)
        self.right_top_button6.grid(row=7, column=0, padx=20, pady=3)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=17, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=15, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=0)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        for i, row_item in enumerate(self.row_info):
            self.vars[i].set(row_item)
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_sid,
                                        font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

    def select_view(self, views):
        for view in views:
            view.clear()
        count = 0
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = """SELECT
  g.sid AS sid,
  g.cid AS cid,
  c.cname AS cname,
  t.tname AS tname,
  c.credit AS credit,
  g.score AS score
FROM
  grade g
  LEFT JOIN (course c JOIN teacher t ON c.tid = t.tid) ON g.cid = c.cid
  ORDER BY sid ASC;"""  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            count = len(results)
            for row in results:
                for i, view in enumerate(views):
                    view.append(row[i])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("select_view")
        print(count)
        self.tree.delete(*self.tree.get_children())
        for i in range(count):  # 写入数据
            values = []
            for view in views:
                values.append(view[i])
            self.tree.insert('', i, values=tuple(values))
        self.tree.update()

    def cal_gpa(self):
        print('cal_gpa')
        print(self.var_sid.get())
        if self.var_sid.get() != '':
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "SELECT GPA('%s');" % \
                  (self.var_sid.get())  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                result = cursor.fetchone()
                messagebox.showinfo('提示！', '计算成功！结果为 %s !' % result)
            except:
                messagebox.showinfo('警告！', '计算失败！')
            db.close()  # 关闭数据库连接

            self.select_view(self.views)
        else:
            messagebox.showinfo('警告！', '请填写学号数据')

    def new_row(self):
        print('new')
        print(self.var_sid.get())
        flag = 0
        seen = set()
        for i, (sid, cid) in enumerate(zip(self.sid, self.cid)):
            if (sid, cid) in seen:
                flag = 1  # 发现重复项，设置标志为1
                break  # 退出循环
            else:
                seen.add((sid, cid))
        if flag == 1:
            messagebox.showinfo('警告！', '已存在！')
        else:
            if (self.var_sid.get() != '' and self.var_cid.get() != ''):
                # 打开数据库连接
                db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "CALL INSERT_SCO('%s', '%s', '%s')" % \
                      (self.var_sid.get(), self.var_cid.get(), self.var_score.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '插入成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '插入失败！')
                db.close()  # 关闭数据库连接

                self.select_view(self.views)
            else:
                messagebox.showinfo('警告！', '请填写选课数据')

    def updata_row(self):
        print('update')
        print(self.var_sid.get())
        if self.var_sid.get() == self.row_info[0] and self.var_cid.get() == self.row_info[1] \
                and self.var_cname.get() == self.row_info[2]  and self.var_tname.get() == self.row_info[3]\
            and self.var_credit.get() == self.row_info[4]:# 如果所填学号 与 所选学号一致
            # 打开数据库连接
            db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql_update = "CALL UPDATE_SCO('%s', '%s', '%s')" % \
                      (self.var_sid.get(), self.var_cid.get(), self.var_score.get())
            try:
                cursor.execute(sql_update)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '更新成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '更新失败！')
            db.close()  # 关闭数据库连接

            self.select_view(self.views)
        else:
            messagebox.showinfo('警告！', '只能修改学生成绩！')

    def del_row(self):
        print('delete')
        print(self.var_sid.get())
        # 打开数据库连接
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql_delete = "CALL DELETE_SCO('%s', '%s')" % \
                      (self.var_sid.get(), self.var_cid.get())
        try:
            cursor.execute(sql_delete)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '删除成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '删除失败！')
        db.close()  # 关闭数据库连接

        self.select_view(self.views)
        print(self.tree.get_children())

    def back(self):
        AdminManage(self.window)  # 显示主窗口 销毁本窗口

class BasicInfo_show:
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
        BasicInfo(self.window)  # 显示主窗口 销毁本窗口

class GradeInfo_show:
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
        ScoreInfo(self.window)  # 显示主窗口 销毁本窗口

class CourseInfo_show:
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
        CourseInfo(self.window)  # 显示主窗口 销毁本窗口

class RewardInfo_show:
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
        RewardInfo(self.window)  # 显示主窗口 销毁本窗口
