from django.shortcuts import render,redirect
from .forms import BookForm

# Create your views here.


def home(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'index2.html')

def user(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        contactnum = request.POST['contact']
        address = request.POST['address']
        pincode = request.POST['pincode']
        device = request.POST['device']
        defect = request.POST['defects']
        date = request.POST['date']
        return render(request,'user.html',{
            'fullname':fullname,
            'email' : email,
            "contactnum" : contactnum, 
            'address':address,
            'pincode':pincode,
            'device':device,
            'defects': defect ,
            'date' : date
            })
        if form.is_valid():
            form.save()
            return redirect('user.html')
        

    else:
        form = BookForm()
        return render(request, 'index2.html', {'form':form})

   