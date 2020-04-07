from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('summary/', views.summary, name='summary'),
    path('ranking', views.site_ranking, name='ranking'),
    path('', views.LocationListView.as_view(), name='person_changelist'),
    path('add/', views.LocationCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.LocationUpdateView.as_view(), name='person_change'),
    path('ajax/load-state/', views.load_state, name='ajax_load_state'),

]
