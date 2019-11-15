from django.urls import include, path
from rest_framework import routers
from .views import TodoApiList, TodoApiDetail


router = routers.DefaultRouter()
router.register('', TodoApiList)

urlpatterns = [
    path('v1/', include(router.urls)),

]
