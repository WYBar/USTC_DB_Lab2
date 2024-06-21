import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
from login import StartPage

# 管理员账号设置
class Adminlogin:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('请先登录任意管理员账号')
        self.window.geometry('300x500')  # 这里的乘是小x

        label = tk.Label(self.window, text='管理员登陆', bg='green', font=('Verdana', 20), width=30, height=2)
        label.pack()

        Label(self.window, text='管理员账号：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_username = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_username.pack()

        Label(self.window, text='管理员密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="修改密码", width=8, font=tkFont.Font(size=12), command=self.login_change).pack(pady=25)
        Button(self.window, text="创建账号", width=8, font=tkFont.Font(size=12), command=self.login_create).pack(pady=25)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack(pady=25)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login_create(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student',user='root', password='767022')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin_login_k WHERE admin_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员创建界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            CreateAdminPage(self.window)
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def login_change(self):
        print(str(self.admin_username.get()))
        print(str(self.admin_pass.get()))
        admin_pass = None

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin_login_k WHERE admin_id = '%s'" % (self.admin_username.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                admin_pass = row[1]
                # 打印结果
                print("admin_id=%s,admin_pass=%s" % (admin_id, admin_pass))
        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')
        db.close()  # 关闭数据库连接

        print("正在登陆管理员修改密码界面")
        print("self", self.admin_pass)
        print("local", admin_pass)

        if self.admin_pass.get() == admin_pass:
            AdminChange(self.window)
        else:
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


class CreateAdminPage:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员账号注册')
        self.window.geometry('300x450')  # 这里的乘是小x

        Label(self.window, text='管理员用户名：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_id.pack()

        Label(self.window, text='设置密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="创建用户", width=8, font=tkFont.Font(size=12), command=self.find).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

    def find(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_pass.get()))

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT admin_id FROM admin_login_k WHERE admin_id = '%s'" % \
              (self.admin_id.get())  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print(results)
            if self.admin_id.get in results:
                print("Error: name already exists！")
                messagebox.showinfo('警告！', '用户名已存在！')
            else:
                self.change()

        except:
            print("Error: unable to fecth data")
            messagebox.showinfo('警告！', '用户名或密码不正确！')

    def change(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_pass.get()))

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student',user='root', password='767022') # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "INSERT INTO admin_login_k(admin_id, admin_pass) VALUES ('%s', '%s')" % \
              (self.admin_id.get(), self.admin_pass.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '数据库连接失败！')

        db.close()  # 关闭数据库连接

        messagebox.showinfo('提示', '创建成功')


# 管理员密码修改
class AdminChange:
    def __init__(self, parent_window):
        parent_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员密码修改')
        self.window.geometry('300x450')  # 这里的乘是小x

        Label(self.window, text='管理员用户名：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_id = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory')
        self.admin_id.pack()

        Label(self.window, text='设置密码：', font=tkFont.Font(size=14)).pack(pady=25)
        self.admin_pass = tk.Entry(self.window, width=30, font=tkFont.Font(size=14), bg='Ivory', show='*')
        self.admin_pass.pack()

        Button(self.window, text="确定修改", width=8, font=tkFont.Font(size=12), command=self.chage).pack(pady=40)
        Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back).pack()

    def chage(self):
        print(str(self.admin_id.get()))
        print(str(self.admin_pass.get()))

        # 数据库操作 查询管理员表
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')  # 打开数据库连接
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "UPDATE admin_login_k SET admin_pass = '%s' WHERE admin_id = '%s'" % \
              (self.admin_pass.get(), self.admin_id.get())  # SQL 查询语句
        try:
            cursor.execute(sql)  # 执行sql语句
            db.commit()  # 提交到数据库执行
            messagebox.showinfo('提示！', '更新成功！')
        except:
            db.rollback()  # 发生错误时回滚
            messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
        db.close()  # 关闭数据库连接

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口


if __name__ == '__main__':
    try:
        # 打开数据库连接 连接测试
        db = pymysql.connect(host='localhost', port=3306, db='student', user='root', password='767022')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 如果数据表不存在则创建表 若存在则跳过
        # 设置主键唯一
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS admin_login_k(
						admin_id char(20) NOT NULL,
						admin_pass char(20) default NULL,
						PRIMARY KEY (admin_id)
						) ENGINE = InnoDB 
						DEFAULT	CHARSET = utf8
						"""
        cursor.execute(sql)
        # 如果数据表不存在则创建表 若存在则跳过
        sql = """CREATE TABLE IF NOT EXISTS stu_login_k(
						stu_id char(20) NOT NULL,
						stu_pass char(20) default NULL,
						PRIMARY KEY (stu_id)
						) ENGINE = InnoDB 
						DEFAULT	CHARSET = utf8
						"""
        cursor.execute(sql)

        # 关闭数据库连接
        db.close()

        # 实例化Application
        window = tk.Tk()
        StartPage(window)
    except:
        messagebox.showinfo('错误！', '连接数据库失败！')
