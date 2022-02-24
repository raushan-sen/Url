import random
from django.shortcuts import render

mynumbers=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_letter=''.join(random.sample(mynumbers,7)) # For Random 7 Digit Text For Url

# For HomePage
def homepage(request):
    
    return render(request,'home/index.html')

# For BlogPage
def blogs(request):

    return render(request,'blogs/index.html')

# For Every Articles Page
def blogger(request,slug):
    return render(request,'blogs/blogger.html',{"context":slug})

# for contact Us Page
def contactus(request):

    return render(request,'pages/contactus.html')

# For About Us Page 
def abpoutus(request):

    return render(request,'pages/aboutus.html')

# For Privacy Policy 
def privacypolicy(request):

    return render(request,'pages/privacypolicy.html')


# For Dmca Page
def dmcapage(request):
    return render(request,'pages/dmca.html')


# For Admin Dashboard
def dashboard(request):
    return render(request,'dashboard/index.html')


