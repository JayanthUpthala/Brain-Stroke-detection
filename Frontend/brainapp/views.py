from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate  # add thi
from django.contrib.auth.forms import AuthenticationForm 
import pandas as pd
from sklearn.metrics import accuracy_score,classification_report
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split


Index = 'index.html'
About = 'about.html'
Registration = 'registration.html'
Login = 'login.html'
Userhome='userhome.html'
Load = "load.html"
View = 'view.html'
Modules = 'modules.html'
Prediction = "prediction.html"
Graph = 'graph.html'

# Create your views here.
def index(request):
    return render(request,Index )

def about(request):
    return render(request, About)

# Registration page
# for filling a Detail of Usernamem,mail,password,confpassword
def registration(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name= Registration, context={"register_form": form})



# login page
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                messages.info(request, f"You are now logged in as {username}.")
                return redirect("userhome")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name= Login, context={"login_form": form})

def userhome(request):
    return render(request, Userhome )


def load(request):
    if request.method == "POST":
        global df
        file = request.FILES['myfile']
        df = pd.read_csv(file)
        return render(request, Load, {'res': "Data Uploaded Succesfully", })
    return render(request, Load)

# before preprocessing
def view(request):
    global df
    col = df.head(100).to_html
    return render(request, View, {'table': col})

def modules(request):
    global df
    if request.method == "POST":
        x = df.drop("Fracture_Yes_No", axis=1)
        y = df["Fracture_Yes_No"]
        Oversample = SMOTE()
        x_sm, y_sm = Oversample.fit_resample(x,y)
        x_train,x_test,y_train,y_test = train_test_split(x_sm,y_sm,test_size=0.3,random_state=72)


        model = request.POST['algo']
        if model == "1":
            kn = KNeighborsClassifier()
            kn.fit(x_train,y_train)
            k_pred = kn.predict(x_test)
            k_ac = accuracy_score(k_pred, y_test)
            k_acc = classification_report(k_pred, y_test)
            print(k_acc)
            msg =  k_acc
            return render(request, Modules, {'msg': msg})
        if model == "2":
            ln = LogisticRegression()
            ln.fit(x_train,y_train)
            l_pred = ln.predict(x_test)
            l_ac = accuracy_score(l_pred, y_test)
            l_acc = classification_report(l_pred, y_test)
            print(l_acc)
            print("accuracy_score of LogisticRegression is"+": "+str(l_ac))
            msg = l_acc
            return render(request, Modules, {'msg': msg})
        if model == "3":
            nb = GaussianNB()
            nb.fit(x_train,y_train)
            nb_pred = nb.predict(x_test)
            nb_ac = accuracy_score(y_test,nb_pred)
            nb_acc =classification_report(y_test,nb_pred)
            print(nb_acc)
            print("accuracy_score of Naive Bias is"+": "+str(nb_ac))
            msg = nb_acc
            return render(request, Modules, {'msg': msg})

        if model == "4":
            de = DecisionTreeClassifier()
            de.fit(x_train,y_train)
            de_pred = de.predict(x_test)
            de_ac = accuracy_score(y_test,de_pred)
            de_acc =classification_report(y_test,de_pred)
            print(de_acc)
            print("accuracy_score of DecisionTreeClassifier is"+": "+str(de_ac))
            msg = de_acc
            return render(request, Modules, {'msg': msg})
        if model == "5":
            rn = RandomForestClassifier()
            rn.fit(x_train,y_train)
            rn_pred = rn.predict(x_test)
            rn_ac = accuracy_score(y_test,rn_pred)
            rn_acc =classification_report(y_test,rn_pred)
            print(rn_acc)
            print("accuracy_score of RandomForestClassifier is"+": "+str(rn_ac))
            msg = rn_acc
            return render(request, Modules, {'msg': msg})
        if model == "6":
            ml = MLPClassifier()
            ml.fit(x_train,y_train)
            ml_pred = ml.predict(x_test)
            ml_ac = accuracy_score(y_test,ml_pred)
            ml_acc =classification_report(y_test,ml_pred)
            print(ml_acc)
            print("accuracy_score of MLPClassifier is"+": "+str(ml_ac))
            msg = ml_acc
            return render(request, Modules, {'msg': msg})
        if model == "7":
            sv = SVC()
            sv.fit(x_train,y_train)
            sv_pred = sv.predict(x_test)
            sv_ac = accuracy_score(y_test,sv_pred)
            sv_acc =classification_report(y_test,sv_pred)
            print(sv_acc)
            print("accuracy_score of SVC is"+": "+str(sv_ac))
            msg = sv_acc
            return render(request, Modules, {'msg': msg})
        if model == "8":
            cb = CatBoostClassifier()
            cb.fit(x_train,y_train)
            cb_pred = cb.predict(x_test)
            cb_ac = accuracy_score(y_test,cb_pred)
            cb_acc = classification_report(y_test,cb_pred)
            print(cb_acc)
            print("accuracy_score of CatBoostClassifier is"+": "+str(cb_ac))
            msg = cb_acc
            return render(request, Modules, {'msg': msg})
    return render(request, Modules)


def prediction(request):
    global df
    if request.method == "POST":
        x = df.drop("Fracture_Yes_No", axis=1)
        y = df["Fracture_Yes_No"]
        Oversample = SMOTE()
        x_sm, y_sm = Oversample.fit_resample(x,y)
        x_train,x_test,y_train,y_test = train_test_split(x_sm,y_sm,test_size=0.3,random_state=72) 
        if request.method == 'POST':
            a = request.POST['f1']
            b = request.POST['f2']
            c = request.POST['f3']
            d = request.POST['f4']
            e = request.POST['f5']
            f = request.POST['f6']
            g = request.POST['f7']
            h = request.POST['f8']
        result = [[a,b,c,d,e,f,g,h]]
        cb = CatBoostClassifier()
        cb.fit(x_train,y_train)
        final_out = cb.predict(result)
        if final_out == 0:
            msg = "NO CHANCE TO GET A Brain Stroke" 
        else:
            msg = "CHANCE TO GET A Brain Stroke"
        return render(request,Prediction , {'msg':msg})
    return render(request, Prediction)

def graph(request):
    return render(request, Graph)