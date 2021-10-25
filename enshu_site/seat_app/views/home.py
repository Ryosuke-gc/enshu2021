from django.shortcuts import HttpResponse,render,redirect
from seat_app.forms.user import UserModelForm
from seat_app import models
from seat_app.views import my_page
user ={"USER":None}
#登录函数
def login(request):
    errmsg = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        usertype = request.POST['usertype']
        admn_object = models.UserInfo.objects.filter(username=username, password=password,usertype=usertype).first()
        if admn_object :
            if usertype == "administrator":
                return redirect('/asset/index/')
            else:
                user["USER"] = username
                return redirect('/asset/stuindex/')
        else:
            return render(request, 'login.html', {"errmsg": "wrong password"})
    return render(request, 'login.html')
#用户注册函数
def register(request):
    err_msg = ''
    if request.method == 'POST':
        list_name = request.POST.get('username')
        list_pwd = request.POST.get('password')
        if list_name:
            #判断账户是否存在
            pub_list = models.UserInfo.objects.filter(username=list_name)
            if pub_list:
                err_msg = 'user has been existed'
                return render(request, 'alerttest.html')
            else:
                user["USER"] = list_name
                pub_obj = models.UserInfo.objects.create(username=list_name, password=list_pwd,usertype="student")
                pub_obj.save()
                return redirect('/asset/assetlist/')
        else:
            err_msg = 'user name cannot be empty'
            return render(request, 'alerttest.html')

def index(request):
    return render(request,'index.html')

def stuindex(request):
    return render(request,'stuindex.html')


def userlist(request):
    user_queryset = models.UserInfo.objects.all()
    return render(request, 'userlist.html', {"user_queryset": user_queryset})


# def adduser(request):
#     if request.method == "GET":
#         form = UserModelForm()
#         return render(request, 'user_form.html', {"form": form})
#     form = UserModelForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('/asset/userlist/')
#     return render(request, 'user_form.html', {"form": form})
# def edituser(request,nid):
#     obj = models.UserInfo.objects.filter(id=nid).first()
#     if request.method == "GET":
#         form = UserModelForm(instance=obj)
#         return render(request, 'user_form.html', {"form": form})
#     form = UserModelForm(data=request.POST, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/asset/userlist/')
#     return render(request, 'user_form.html', {"form": form})
# def deluser(request,nid):
#     models.UserInfo.objects.filter(id=nid).delete()
#     return redirect('/asset/userlist/')