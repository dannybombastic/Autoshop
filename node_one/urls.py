from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from  . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet) 
router.register(r'groups', views.GroupViewSet)
router.register(r'point', views.CordenatesMembersViewSet)
 

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)), 
     
]