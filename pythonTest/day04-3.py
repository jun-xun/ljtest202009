from dbtools import query

username = input("请输入账号：")
password = input("请输入密码：")

sql = "select * from t_pymysql_account where username='{}' and password='{}'".format(username, password)
r = query(sql)
a = query(sql)
if len(r) != 0:
    print("登陆成功")
else:
    print("登陆失败")