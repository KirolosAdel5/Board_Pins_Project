from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import (
    ServiceCategoryViewSet,
    CurrentUserView,
    )

router = DefaultRouter()
router.register(r'categories', ServiceCategoryViewSet, basename='categories')


urlpatterns = [
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
    
    path('', include(router.urls)),

]

