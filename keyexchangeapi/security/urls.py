from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ChannelViewSet, SecretExchangeView, KeyGenerationView

router = DefaultRouter()
router.register(r'channels', ChannelViewSet)

urlpatterns = [
    path('channels/', views.ChannelListCreateAPIView.as_view(), name='channel-list-create'),
    path('channels/<int:pk>/', views.ChannelDetailAPIView.as_view(), name='channel-detail'),
    path('channels/<int:pk>/accept/', views.ChannelAcceptAPIView.as_view(), name='channel-accept'),
    path('channels/<int:pk>/exchange/', views.SecretExchangeAPIView.as_view(), name='secret-exchange'),
    path('channels/<int:pk>/generate-key/', views.KeyGenerationAPIView.as_view(), name='key-generation'),
]
