from django.urls import path
from . import views

urlpatterns = [
    path('total_items', views.total_items),
    path('nth_most_total_item', views.nth_most_total_item),
    path('percentage_of_department_wise_sold_items', views.percentage_of_department_wise_sold_items),
    path('monthly_sales', views.monthly_sales)
]
