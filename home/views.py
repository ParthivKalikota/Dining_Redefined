from django.shortcuts import render
from .models import Customer

def home(request):
    return render(request,'index.html')
def sample_page(request):
    return render(request,'sample_page.html')
def restaurant_page_Builder(request):
    if request.method == 'POST':
        restaurant_name = request.POST['restaurant_name']
        about = request.POST['about']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        Template = request.POST['template']
        print(Template)

        restaurant = Customer(
            Restaurant_name = restaurant_name,
            About = about,
            location = location,
            phone_no = phone,
            email = email,
            template = Template,
        )
        restaurant.save()
        print("data added to database")

        return render(request,f"{Template}.html",{
            'restaurant_name' : restaurant_name,
            'about' : about,
            'location' : location,
            'phone_number' : phone,
            'email' : email

        })
    return render(request, 'restaurant_page_Builder.html')

# def login_page(request):
#     return render(request,'login.html')
# def signup_page(request):
#     return render(request,'signup.html')
 