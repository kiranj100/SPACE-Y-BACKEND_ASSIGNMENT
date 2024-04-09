
from django.urls import path
from .views import (
    EmployeeLoginView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,
    BillListCreateView,
    BillRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('employee/login/', EmployeeLoginView.as_view(), name='employee-login'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('bills/', BillListCreateView.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillRetrieveUpdateDestroyView.as_view(), name='bill-detail'),
]
