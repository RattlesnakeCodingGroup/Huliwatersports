from django.urls import path

from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView, EstimateView, EmailView, Info, ItemSizeDetailView,
)
from django.contrib.auth.decorators import login_required


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('products/<slug>/', ItemSizeDetailView.as_view(), name='productsize'),

    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('estimate/', login_required(EstimateView.as_view()), name= 'estimate' ),
    path('<int:pk>/email/', login_required(EmailView.as_view()), name= 'email'),
    path('info/', views.Info, name = 'Info'),
    path('paypal/', views.paypal, name='paypal'),
    path('eraser/',views.eraser, name = 'eraser'),
    path('success/', views.success, name= 'suxx'),

]
