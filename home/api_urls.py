from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('filter_products/', ProductFilterViewSet.as_view(), name='filter_products'),
    path('order_products/', ProductFilterViewSet.as_view(), name='order_products'),
]