from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='books')

# urlpatterns = [
#     path('', views.book_list, name='booksMain'),
#     path('<int:pk>', views.book_detail, name="bookDetail"),
# ]

urlpatterns = router.urls