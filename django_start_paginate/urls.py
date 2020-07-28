from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [

	path('admin/', admin.site.urls),
	path('<pk>/', views.product_detail, name='detail'),
	# path('api/v1/post/', include(('restpost.urls', 'restpost'), namespace='restpost')),
]
