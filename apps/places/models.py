from django.db import models
from cloudinary.models import CloudinaryField 
from apps.categories.models import Category
# Create your models here. 

class Place(models.Model): 

    MY_CHOICES = (
        ('Private and Luxury', 'Private and Luxury'),
        ('Full-day Tours', 'Full-day Tours'),
        ('Day trips', 'Day trips'),
        ('Forest', 'Forest'),
        ('Favorites', 'Favorites'),
    )

    class Meta(object):
        db_table = 'place' 


    name = models.CharField('Name', max_length = 50, db_index=True, null=False, blank=False) 

    description = models.CharField('Description', max_length= 500, db_index=True, null=False, blank=False)

    time_to_travel = models.CharField('Time_to_travel', max_length=20, null=False, blank= False)

    google_map_link = models.CharField('Google_map_link', max_length=500, null=False, blank=False)

    created_at = models.DateTimeField('created_at', null=False, blank=False, auto_now_add=True)

    updated_at = models.DateTimeField('updated_at', null=False, blank=False, auto_now_add=True) 

    image = CloudinaryField('image', blank=False) 

    place_type = models.CharField('Place Type', max_length=50, blank=False, choices = MY_CHOICES) 

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name