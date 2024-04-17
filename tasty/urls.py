
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasty.common.urls')),
    path('profile/',include('tasty.accounts.urls')),
    path('recipe/',include('tasty.recipes.urls')),

]
