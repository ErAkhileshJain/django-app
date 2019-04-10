from django.shortcuts import render
from testapp.forms import UserForm


# Create your views here.

def helloWorld(req):
    form = UserForm()
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            pass
    d1 = {
        'form': form
        # 'name': 'akhil',
        # 'email':'jain@gmail.com',
        # 'l1':[1,2,3,4],
        # 'd2':{'address':'BTM','city':'Bangalore'}
    }
    return render(req, 'hello.html', d1)


def testing(req):
    return render(req, 'test1.html')
