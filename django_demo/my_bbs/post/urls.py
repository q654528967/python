from django.urls import path
from django.urls import register_converter
from .views import MonthConverter
from django.urls import re_path
from . import views

register_converter(MonthConverter, 'mth')

urlpatterns = [
    path('hello/', views.FirstView.as_view(), name='hello'),
    path('dynamic/', views.dynamic_hello, name='dynamic'),
    re_path('re_dynamic/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/', views.dynamic_hello, name='dynamic'
            ),
    path('topic_list/', views.topic_list_view, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail_view, name='pid'),
    path('topic_comment/', views.add_comment_to_topic_view, name='topic_comment')
]

