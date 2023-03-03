from django.db import models

class TvShow(models.Model):

    GENRE = (
        ('Horror', 'Ужасы'),
        ('Melodramme', 'Мелодрамма'),
        ('Anime', "Anime"),
        ('Comedy', 'Комедия')

    )

    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма')
    image = models.ImageField('Фото', upload_to='')
    trailer = models.URLField('Ссылка с ютуба')
    quantity = models.PositiveIntegerField('Колличество серий')
    genre = models.CharField(max_length=100, choices=GENRE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Commet_TV(models.Model):
    RATING_CHOISES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    choise_show = models.ForeignKey(TvShow, on_delete=models.CASCADE,
                                    related_name='comment_object')
    name = models.CharField('Введите ваше имя', max_length=100)
    text = models.TextField('Ваш коммент')
    rating = models.CharField('Поставьте оценку', max_length=100, choices=RATING_CHOISES)






