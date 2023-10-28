from django.urls import path
from directory import views

urlpatterns = [
    path('show', views.show, name="show"),
    path('staf', views.staf, name="staf"),
    path('edit/<str:id>', views.edit, name="edit"),
    path('update/<str:id>', views.update, name="update"),
    path('delete/<str:id>', views.destroy, name="destroy"),  
]