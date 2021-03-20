from rest_framework.routers import SimpleRouter

from main.views import BookViewSet, JournalViewSet

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')
router.register('journals', JournalViewSet, basename='journals')

urlpatterns = router.urls
