from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')), #caminho para home
    path('admin/', admin.site.urls),
    path('core/', include('core.urls', namespace='core')),
    
]

