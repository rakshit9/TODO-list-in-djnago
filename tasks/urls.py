from django.urls import path

from tasks.views import(index,
    updateTask,deleteTask

)




urlpatterns = [
    path('',index,name='list'),
    path('update_task/<str:id>/',updateTask,name='update_task'),
    path('delete/<str:id>/',deleteTask,name='delete'),
]
