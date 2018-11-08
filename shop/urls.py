from django.urls import path, include
from rest_framework import routers
from shop import views


router = routers.SimpleRouter(trailing_slash=False)
router.register('customers', views.CustomerViewSet)
router.register('products', views.ProductViewSet)
router.register('delivery', views.DeliveryAddViewSet)
router.register('orders', views.OrderViewSet)
router.register('order_items', views.OrderItemViewSet)
router.register('categories', views.CategoryViewSet)
router.register('login', views.LoginViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]