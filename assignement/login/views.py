from django.shortcuts import render
import mysql.connector as sql
# Create your views here.

un = ''
pwd = ''


# Create your views here.

def loginaction(request):
    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="root",database='assignmentdb')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_name":
                un=value
            if key=="password":
                pwd=value
        c="select * from users where user_name='{}' and password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t ==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')

