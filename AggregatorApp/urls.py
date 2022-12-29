# =============================================
from django.conf import settings
from django.conf.urls.static import static
# =============================================
from django.contrib import admin
from django.urls import path, include
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HeadlinesView.as_view(), name='home')
]
