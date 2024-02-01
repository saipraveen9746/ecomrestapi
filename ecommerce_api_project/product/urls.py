
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet,CartViewSet,ProductDetailview,add_to_cart


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('cart', CartViewSet, basename='cart')
router.register('carts', CartViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('carts/<int:pk>/list_cart_items/', CartViewSet.as_view({'get': 'list_cart_items'}), name='cart-list-items'),
    path('product-detail/<int:pk>/',ProductDetailview.as_view(),name='detail'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart')
    
]
