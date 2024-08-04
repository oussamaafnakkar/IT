from django.urls import path
from .views import ITServiceList, ITServiceDetail

urlpatterns = [
    path('it-services/', ITServiceList.as_view(), name='itservice_list'),
    path('it-services/<int:pk>/', ITServiceDetail.as_view(), name='itservice_detail'),
]
