from django.urls import path, include
from .views import PostBook, RetrieveBook

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', PostBook.as_view(), name='all_books'),
    path('<int:pk>', RetrieveBook.as_view(), name='book_detils'),
]
