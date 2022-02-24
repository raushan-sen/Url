from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='Home Page'),
    path('page/about-us/',views.abpoutus,name='About US'),
    path('page/contact-me/',views.contactus,name='Contact Me'),
    path('page/dmca/',views.dmcapage,name='DMCA Page'),
    path('page/privacy-policy/',views.privacypolicy,name='Privacy Policy'),
    path('blog/',views.blogs,name='Blog Page'),
    path('blog/<slug>/',views.blogger,name='Blogger Page'),
    path('dashboard/',views.dashboard,name='Admin Dashboard'),
]

