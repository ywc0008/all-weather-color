from django.urls import path

from . import views


app_name='monitor'

urlpatterns = [
    # /monitor
    path('', views.index, name='index'),

    # /monitor/detail/data_id
    path('detail/<int:data_id>', views.detail, name='detail'),

    # /monitor/update
    #path('update/<int:data_id>', views.update, name='update'),

    # /monitor/delete
    #path('delete/<int:data_id>', views.delete, name='delete'),

]