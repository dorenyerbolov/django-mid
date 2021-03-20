from rest_framework import viewsets

from main.models import Book, Journal
from main.permissions import IsAdminUserOrReadOnly
from main.serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAdminUserOrReadOnly,)


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
