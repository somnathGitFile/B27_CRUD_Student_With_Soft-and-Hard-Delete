from django.urls import path
from . import views

urlpatterns = [
    path('sf/', views.studentFormView, name='stuform_url'),
    path('ss/', views.showstudentView, name='showstu_url'),
    path('ss/<int:page>/', views.showstudentView, name='showstu_url'),
    path('us/<int:id>/',views.updateStuView, name='update_url'),
    path('ds/<int:id>/', views.softdeleteStuview, name='delete_url'),
    path('sdv/<int:page>/', views.showdeletestudentView, name = 'showdeleted_url'),
    path('sdv/', views.showdeletestudentView, name = 'showdeleted_url'),
    path('restore/<int:id>/', views.restorestudentView, name='restore_url'),
    path('hdv/<int:id>/', views.HarddeleteView, name= 'harddel_url')

]