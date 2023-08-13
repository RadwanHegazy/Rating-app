from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete



class Product (models.Model) :
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    price = models.PositiveIntegerField(default=0)
    averge_starts = models.FloatField(null=True,blank=True,validators=[MaxValueValidator(5)])

    def __str__(self) : 
        return f'{self.title}'


class Star (models.Model) : 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    star = models.FloatField(validators=[MaxValueValidator(5),MinValueValidator(0)])

    def __str__(self) : 
        return f'{self.user} -> {self.product}'

    class Meta :
        unique_together = (('user','product'),)
        index_together = (('user','product'),)


@receiver(post_save, sender = Star)
def CalculateAverageOnCreate ( created, instance,**args) :
    if created : 
        product = instance.product

        get_all_stars = Star.objects.filter( product = product )
        star_ranges = 0
        stars = []

        for i in get_all_stars : 
            star_ranges = star_ranges + 1
            stars.append(i.star)
        
        stars = sum(stars)


        product.averge_starts = stars / star_ranges
        product.save()




@receiver(post_delete, sender = Star)
def CalculateAverageOnDelete (instance,**args) :
    
    product = instance.product
    startOfUser = instance.star

    get_all_stars = Star.objects.filter( product = product )
    star_ranges = 0
    stars = []

    for i in get_all_stars :

        if i != instance :  
            star_ranges = star_ranges + 1
            stars.append(i.star)
    

    stars = sum(stars)

    try :
        product.averge_starts = stars / star_ranges
    except ZeroDivisionError :
        product.averge_starts = None

    product.save()
