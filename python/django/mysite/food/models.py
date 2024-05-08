from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.miagrillandbar.com/wp-content/uploads/2020/04/dish-image-no.jpg")