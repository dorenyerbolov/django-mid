from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Стоимость')
    description = models.TextField(max_length=1024, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        abstract = True

    def __str(self):
        return f'{self.name}'


class Book(BookJournalBase):
    num_pages = models.IntegerField(null=True, blank=True, verbose_name='Количество страниц')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    BULLET = 1
    FOOD = 2
    TRAVEL = 3
    SPORT = 4

    TYPE_CHOICES = (
        (BULLET, 'Bullet'),
        (FOOD, 'Food'),
        (TRAVEL, 'Travel'),
        (SPORT, 'Sport')
    )

    type = models.CharField(max_length=30, null=True, blank=True, choices=TYPE_CHOICES, verbose_name='Тип')
    publisher = models.CharField(max_length=255, null=True, blank=True, verbose_name='Издетель')

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
