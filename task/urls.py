from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('login/',views.loginView,name='login'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.aboutView,name='about'),
    path('user_login/',views.userLogin,name='user_login'),
    path('add_todo/',views.addTodo,name='add_todo'),
    path('logout/',views.userLogout,name='logout_user'),
    path('update_task/<int:pk>/update/',views.updateTodo,name='update_task'),
    path('delete_task/<int:pk>/remove/',views.deleteTodo,name='delete_task'),
    path('complete_task/<int:pk>/completed/',views.taskComplete,name='complete_task'),
    path('completed_tasks/',views.completedTasks,name='accomplished_tasks_list'),
]