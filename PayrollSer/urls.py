# PayrollSer/urls.py
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('apis/', include('apis.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        # User management API routes
]
