# # accounts/urls.py
# from django.urls import path
# from . import views

# app_name = 'accounts'

# urlpatterns = [
#     path('', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('dashboard/', views.dashboard_view, name='dashboard'),

#     path("report/", views.report, name="report"),
#     path("report/success/", views.report_success, name="report_success"),

#     # path('report/success/', views.report_page, name='report_success'),
#     path('search/', views.search_location, name='search_location'),
#     # path('contact/', views.contact_view, name='contact'),
#     path("contact/", views.contact, name="contact"),

# ]


from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   # path('', views.home, name='home'),
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path("report/", views.report, name="report"),
    path("report/success/", views.report_success, name="report_success"),
    path('search/', views.search_location, name='search_location'),
    path("contact/", views.contact, name="contact"),
]




