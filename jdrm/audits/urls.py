from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='page2'),
    path('<int:pk>', views.Audit.as_view(), name='audit'),
    path('create', views.CreateAudit.as_view(), name='new_audit')
]
