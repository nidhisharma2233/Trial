from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.post,name='post'),
    path('view', views.all, name='view'),
    path('add', views.add, name='add'),
    path('remove', views.get, name='remove'),
    path('remove/<int:id>', views.delete, name='remove'),
    path('filter', views.filter, name='filter'),
    path('Register-View',views.viewalldataupdatepage,name='Register-View'),
    path('update/<int:id>', views.update, name='update'),
    path('formupdate/update/<int:id>', views.updatedata, name='formupdate'),


    # # path('',views.index,name='index'),

       ]
     # path('All', views.all, name='all'),
     #
     # path('filter', views.filter, name='filter')]