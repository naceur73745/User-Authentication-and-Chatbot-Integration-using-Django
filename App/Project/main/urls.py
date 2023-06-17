from django.urls import path , include
from  .  import views

urlpatterns = [ 
   path( 'home/' , views.home),
   path('register/' , views.register), 
   path( 'login/' , views.login),
   path( 'logout/' , views.logout_page),
   path( 'check/' , views.check),
   path( 'chat/' , views.chatbot),

]