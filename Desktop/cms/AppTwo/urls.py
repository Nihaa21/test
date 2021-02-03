from django.conf.urls import url
from AppTwo import views
from django.urls import path



urlpatterns = [
path('', views.login, name='login'),


path('cms/', views.cms, name='user_cms'),
path('logout/', views.user_logout, name='user_logout'),

path('add_client/', views.show_form, name='add_client'),
path('form_submit/', views.form_submit, name='form_submit'),
path('edit_client/<int:id>' ,views.edit_client,name="edit_client"),
path('edit_client/update/<int:id>' ,views.update,name="update"),
# path('date_order/', views.date_order, name='date_order'),
]
