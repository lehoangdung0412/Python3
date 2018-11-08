from django.urls import path, include
from django.contrib import admin
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
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('shop.urls')),
    path('api/v1/', include(router.urls)),
]