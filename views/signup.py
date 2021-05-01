from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View



class Signup(View):
    def validateCustomer(self,customer):
        error_message = None;
        if(not customer.username):
            error_message = "Name required"
        
        elif len(customer.username)<7:
            error_message = "username must be 8 characters atleast"
        
        elif (not customer.email):
            error_message = "email required"
        
        elif len(customer.email)<9:
            error_message = "email must 9 be characters atleast"

        elif (not customer.password):
            error_message = "password required"
        
        elif len(customer.password)<3:
            error_message = "password must be 3 characters atleast"
        
        elif customer.isExists():
             error_message = "Email already registered"
       
        
        return error_message
    def get(self,request):
        return render(request, 'signup.html')
    

    def post(self,request):
        postData = request.POST
        username = postData.get('username')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'username':username,
            'email':email,
            'password':password

        }
        error_message = None
        customer = Customer(username = username,
            email = email,
            password = password)
        error_message = self.validateCustomer(customer)
        if not error_message:
            print(username,email,password) 
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
            'error': error_message ,
            'values':  value}
            return render(request,'signup.html' ,data )