"""FoodPantry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from checkout import views as checkout_views
from dashboard import views as dashboard_views
from impact_measurement import views as impact_measurement_views
from inventory import views as inventory_views
from provider import views as provider_views
from dashboard import views as dashboard_views
from waste_reduction import views as waste_reduction_views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'inventory', inventory_views.InventoryViewSet)
router.register(r'checkout', checkout_views.CheckoutViewSet)
router.register(r'provider', provider_views.ProviderViewSet)
router.register(r'user', provider_views.UserViewSet)
router.register(r'wastage', waste_reduction_views.WastageViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.dashboard, name='dashboard'),
    path('about/', dashboard_views.about, name='about'),


    path('checkout/', checkout_views.checkout_view, name='checkout_view'),

    path('impact/', impact_measurement_views.impact_measurement, name='impact'),


    path('inventory/', inventory_views.inventory_view, name='inventory_view'),
    path('update/<str:pk>/', inventory_views.update, name='update'),
    path('remove/', inventory_views.remove, name='remove'),

    path('login/', dashboard_views.user_login, name='user_login'),
    path('logout/', dashboard_views.user_logout, name='logout'),
    path('join/', dashboard_views.join, name='join'),

    path('provider/', provider_views.provider_view, name='provider_view'),
    path('update_pro/<str:pk>/', provider_views.update_pro, name='update_pro'),
    path('remove_pro/', provider_views.remove_pro, name='remove_pro'),
    path('provider_details/<str:pk>/', provider_views.details, name='provider_details'),

    path('waste/', waste_reduction_views.waste_reduction, name='waste'),
    path('waste_remove/', waste_reduction_views.waste_remove, name='waste_remove'),

    path('api/v1/', include(router.urls)),
    path('api-auth/v1/', include('rest_framework.urls',namespace='rest_framework')),
]
