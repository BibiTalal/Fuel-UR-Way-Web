"""webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home, name="home"),
    path("signup/",create_user,name="create-user"),
    path("signout/",signout_user,name="signout"),
    path("signin/",signin_user,name="signin"),
    path("orders/",get_Orders,name="order-list"),
    path("order/<int:order_id>/", get_order, name="order-detail"),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path("done/<int:done_id>/",done_booking,name="done"),
    path("confirm/<int:order_id>/",confirm_order,name="confirm"),
    path("profile/update/",profile_update,name="profile-update"),
    path("password/change/", ChangePasswordView.as_view(), name="change-password"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
