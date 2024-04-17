from django.urls import path

from tasty.common.views import IndexView

urlpatterns=[
    path('',IndexView.as_view(), name='index' )
]