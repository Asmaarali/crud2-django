from django.urls import path
from crudapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('editstudent/<int:id>',views.editstudent,name="editstudent"),
    path('delstudent/<int:id>',views.delstudent,name="delstudent"),
]
