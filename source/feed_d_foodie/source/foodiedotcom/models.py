from __future__ import unicode_literals
from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    restro_name = models.CharField(max_length=500, null=True)
    cuisines = models.CharField(max_length=500, null=True)
    avg_cost_for_two = models.IntegerField()
    currency = models.CharField(max_length=500, null=True)
    has_table_booking = models.CharField(max_length=500, null=True)
    has_online_delivery = models.CharField(max_length=500, null=True)
    rating = models.FloatField(default=0)
    rating_color = models.CharField(max_length=500, null=True)
    rating_text = models.CharField(max_length=500, null=True)
    votes = models.IntegerField()

    class Meta:
        db_table = 'tbl_restaurant_info'

class RestaurantExtraInfo(models.Model):
    restro = models.ForeignKey(Restaurant, db_column='restaurant_id', related_name='restro_extra_map_restro_id')
    country_code = models.IntegerField()
    city = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=500, null=True)
    locality = models.CharField(max_length=500, null=True)
    locality_verbose = models.CharField(max_length=500, null=True)
    x = models.FloatField(default=0)
    y = models.FloatField(default=0)

    class Meta:
        db_table = 'tbl_restaurant_extra_info'
