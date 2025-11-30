from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MediaItem(models.Model):
    CATEGORY_CHOICES = (
        ('movie', 'Movie'),
        ('series', 'Series'),
        ('anime', 'Anime'),
        ('animation', 'Animation'),
    )
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='movie')
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    ) 
    watched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:                                 
        ordering = ['-rating', 'title']
        verbose_name = 'Media Item'
        verbose_name_plural = 'Media Items'

    def __str__(self):
        rating_display = f"{self.rating}/10" if self.rating else "Not rated"
        return f"{self.title} — {self.get_category_display()} ({rating_display})"