from django.shortcuts import redirect, render
from .models import User
import mysql.connector
from django.contrib import messages
from .forms import sell_property_Form,sell_property_Form1
from .models import sell_property,sell_property1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
# Create your views here.
def homepage(req):
    return render(req,'index.html')

def register(req):
    if req.method=="POST":
        user = User()

        user.fname=req.POST['fname']
        user.lname=req.POST['lname']
        user.email=req.POST['email']
        user.password=req.POST['password']
        user.repassword=req.POST['repassword']
        #print(user.password)



        if user.password != user.repassword:
            return redirect('register')
        elif user.fname == "" or user.password == "":
            messages.info(req,'enter details correctly')
            return redirect('register')

        else:
            user.save()    
        
    return render(req,'register.html') 

def login(req):
    con = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='dreamvilla')
    cursor= con.cursor()
    sqlcommand="select email,password,repassword from dreamvilla_mainapp_user "
    
    cursor.execute(sqlcommand)
   
    login_details=[]
   
    for i in cursor:
        login_details.append(i)
    
    
    if req.method=="POST":
        email=req.POST['email']
        print(email)
        password=req.POST['password']
        print(password)
        repassword=req.POST['repassword']
        global value
        def value():
            return email   

        
        for o in range(len(login_details)):
            #request.session['email_id']=email
            print(login_details[o][0],login_details[o][1],login_details[o][2])
            if (email == login_details[o][0] and password== login_details[o][1]) and repassword== login_details[o][2] :
                print("login successfull:",login_details[o][0])
                return render(req,'after_login_homepage.html',{'email':email})
                     
                break     
        else:
            messages.info(req,"check email or password") 
            return redirect('login')
        



        
             
    return render(req,'login.html')

def homepage_after_login(req):
    return render(req,'after_login_homepage.html')

def sell(req):
    if req.method == "POST":
        form = sell_property_Form(req.POST, req.FILES)
        form1 = sell_property_Form1(req.POST, req.FILES)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
           
    data=sell_property.objects.all()
    data1=sell_property1.objects.all()
    global sell_data
    def sell_data():
        return data        
    form = sell_property_Form()  
    form1 = sell_property_Form1()

    return render(req, 'sell.html', {'data':data,'form':form,'data1':data1,'form1':form1})
    


    




    #return render(req,'sell.html')

def buy(req):
    data11=sell_property.objects.all()
    #for i in data11:
     #   print(i)
    return render(req,'buy.html',{'data_details':data11})    

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def team1(req):
    return render(req,'team1.html')

def team2(req):
    return render(req,'team2.html')

def team3(req):
    return render(req,'team3.html')

def team4(req):
    return render(req,'team4.html')


def propertysingle(req):

    return render(req,'property-single.html')


def buy_propperty(req):
    if req.method=="POST":
        propertys=req.POST['propertys']

        con1 = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='dreamvilla')
        cursor1= con1.cursor()
        query="select * from dreamvilla_mainapp_sell_property1 where Property_Name =%s "%(propertys)   
        res=cursor1.execute(query)

    data1a=sell_property1.objects.all() 
    data111=sell_property.objects.all()
    #ataa=sell_property1.objects.all()  
    print(data111) 
    return render(req,'property-single1.html',{'deteils':data1a , 'deteils1':data111})

        
        
    

#def propertysingle1(req):


   # return render(req,'property-single1.html',{'deteils':res1})

def predict(req):
    return render(req, "predict.html")

def result(request):
    data = pd.read_csv(r"D:\USA_Housing.csv")
    data = data.drop(['Address'],axis=1)
    x = data.drop('Price',axis=1)
    y= data['Price']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.30)
    model = LinearRegression()
    model.fit(x_train,y_train)
    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    pred=model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
    pred = round(pred[0])

    price="the predicted price is $"+str(pred)
    return render(request,'predict.html',{'result2':price})

    