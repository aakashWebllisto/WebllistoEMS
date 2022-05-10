from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('users/home', views.Homepage),
    
    # path('cars/listing_buy_query/<int:id>', views.Listing_buy_query),
    # path('cars/submit_listing_query/<int:id>', views.Submit_listing_query),

]
