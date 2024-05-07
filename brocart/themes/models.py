from django.db import models

# Theme model

class Theme (models.Model) :

    banner = models.ImageField(upload_to = 'themes/')
    caption = models.TextField()