from django.urls import path
from employee import views
from.import views

urlpatterns = [
    path('',views.emp),
    path('show',views.show),
    path('edit/<int:id>/',views.edit),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/',views.destroy),
]
 