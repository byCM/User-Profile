from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import views

app_name = "accounts"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', "accounts")), name='accounts'),
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/email/', views.change_email, name='change_email'),
    path('profile/edit/password/', views.change_password, name='change_password')
]

urlpatterns += staticfiles_urlpatterns()
