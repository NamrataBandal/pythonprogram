from django.shortcuts import render

import mysql.connector as sql
fn=''
ln=''
dob=''
un=''
pwd=''
sq=''
sa=''
ad=''

# Create your views here.

def signaction(request):
    global fn,ln,dob,un,pwd,sq,sa,ad
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="root",database='assignmentdb')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
              fn=value
            if key=="last_name":
              ln=value
            if key=="dob":
                dob=value
            if key=="user_name":
                un=value
            if key=="password":
                pwd=value
            if key=="security_que":
                sq=value
            if key=="security_ans":
                sa=value
            if key=="address":
                ad=value
        c="insert into users values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn , ln,dob,un,pwd,sq,sa,ad)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')
