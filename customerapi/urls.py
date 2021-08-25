from django.urls import path
from .views import CustomerAPIView,Customerdetails, customer_list,customer_details, basket_details, basket_list, product_details, product_list,basket_list,basket_details


urlpatterns = [
    #path('customer/',customer_list),
    path('customer/',CustomerAPIView.as_view()),
    path('customerdetail/<int:id>/',Customerdetails.as_view()),
    path('product/',product_list),
    path('productdetail/<int:pk>/',product_details),
    path('basket/',basket_list),
    path('basketdetail/<int:pk>/',basket_details),
]

