from django.urls import path
from polling_app import views


#Template Tagging
#app_name = 'polling_app'

urlpatterns = [
    
    path('landing_page/', views.landing_page, name="landing_page"),
    # path('index/', views.index, name="index"),
    path('login_page/', views.login_page, name="login_page"),
    path('logout/', views.logout_user, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('vote/', views.vote, name="vote"),
    path('timeline/', views.timeline, name="timeline"),
    path('register/', views.register, name="register"),
    
]