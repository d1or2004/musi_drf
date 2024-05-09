from django.urls import path, include
from .views import LandingAPIView, ArtistAPIView, AlbumAPIView, SongAPIView, ArtistCreateAPIView, ArtistUpdateAPIView, \
    ArtistDeleteAPIView, AlbumDetailAPIView, SongDetailAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', viewset=SongDetailAPIView)

urlpatterns = [
    path('landing/', LandingAPIView.as_view(), name='landing'),
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('album/', AlbumAPIView.as_view(), name='album'),
    path('song/', SongAPIView.as_view(), name='song'),
    path('', include(router.urls)),
    path('artist/create/', ArtistCreateAPIView.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', ArtistUpdateAPIView.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', ArtistDeleteAPIView.as_view(), name='artist_delete'),
    path('album/<int:pk>/', AlbumDetailAPIView.as_view(), name='album'),

]
