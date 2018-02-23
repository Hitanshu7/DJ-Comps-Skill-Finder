from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/<str:sap_id>/', views.view_profile, name='view_profile'),
    path('requests/<str:sap_id>/', views.send_request, name='send_request'),
    path('requests/<int:pk>/accept/', views.accept_request, name='accept_request'),
    path('requests/<int:pk>/reject/', views.reject_request, name='reject_request'),
    path('requests/<int:pk>/cancel/', views.cancel_request, name='cancel_request'),
    path('search/', views.search, name='search'),
    path('relationship/terminate/<int:pk>/', views.terminate_relationship, name='terminate_relationship'),
    path('hackathons/teams/<int:pk>/', views.view_hackathon_team, name='view_hackathon_team'),
    path('hackathons/teams/add/', views.add_hackathon_team, name='add_hackathon_team'),
    path('hackathons/teams/<int:pk>/request/', views.send_hackteam_request, name='send_hackteam_request'),
    path('hackathons/teams/request/<int:pk>/accept/', views.accept_hack_request, name='accept_hack_request'),
    path('hackathons/teams/request/<int:pk>/reject/', views.reject_hack_request, name='reject_hack_request'),
    path('hackathons/teams/request/<int:pk>/cancel/', views.cancel_hack_request, name='cancel_hack_request'),
    path('projects/teams/<int:pk>/', views.view_project_team, name='view_project_team'),
    path('projects/<int:pk>/teams/add/', views.add_project_team, name='add_project_team'),
    path('projects/teams/<int:pk>/request/', views.send_project_team_request, name='send_project_team_request'),
    path('projects/teams/request/<int:pk>/accept/', views.accept_project_request, name='accept_project_request'),
    path('projects/teams/request/<int:pk>/reject/', views.reject_project_request, name='reject_project_request'),
    path('projects/teams/request/<int:pk>/cancel/', views.cancel_project_request, name='cancel_project_request'),
]
