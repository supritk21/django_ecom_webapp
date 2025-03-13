from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .models import Profile, Address
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        print(email, password)
        
        if not user_obj.exists():
            messages.warning(request, 'Account not exist.')
            return HttpResponseRedirect(request.path_info)
        

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')        
        

        messages.warning(request, 'invalid credentials.')
        return HttpResponseRedirect(request.path_info)
    
    return render(request,'accounts/login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        print(first_name,last_name, password)
        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            print("request path info  ", request.path_info)
            return HttpResponseRedirect(request.path_info)

        print(first_name)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html' )


def add_address(request):
    if request.method == 'POST':
        # Make sure zip_code is included in the POST data
        user_obj = request.user
        zip_code = request.POST.get('zip_code')
        Address.objects.create(
            address_line_1=request.POST.get('address_line_1'),
            address_line_2=request.POST.get('address_line_2'),
            zip_code=zip_code,
            locality=request.POST.get('locality'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            profile=user_obj.profile 
        )
        print("address is created  ")
        # messages.success(request, 'Address is created successfully.')
        return render(request,'accounts/show_address.html',  {'user': user_obj} )
        
    else:
        return render(request,'accounts/get_address.html' )


def delete_address(request, address_id ):
    # Get the address object, or 404 if not found
    address = get_object_or_404(Address, id=address_id)
    print("address matched d \n", address )
    # Ensure that the address belongs to the logged-in user's profile
    if address.profile.user == request.user:
        address.delete()  # Delete the address
        # messages.success(request, 'Address deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this address.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
 
    
def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token )
        user.is_email_verified = True
        user.save()
        print(" email is activated")
        return redirect('/')

    except Exception as e:
        return HttpResponse("invalid token")
    

@login_required
def account_details(request):
    # You can access the current logged-in user using request.user
    user = request.user
    print(user)                      
    return render(request, 'accounts/account_details.html', {'user': user})

    # return HttpResponse("my account id clicked ")



