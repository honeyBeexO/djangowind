from django.utils.translation import gettext_lazy as _ # type: ignore
from django.urls import reverse # type: ignore
from django.db import models # type: ignore
import uuid
from django.conf import settings # type: ignore


from datetime import date

class Country(models.Model):
    name = models.CharField(max_length=256,blank=True)
    code = models.SmallIntegerField(null=True)
    alpha_two_code = models.CharField(max_length=2,null=True)
    alpha_three_code = models.CharField(max_length=3,null=True)
    
    def __str__(self):
        return f'{self.name} {self.code} {self.alpha_three_code}'
     

class Sector(models.Model):
    # Define type choices if there are known types
    TYPE_CHOICES = [
        ('commercial', 'Commercial'),
        ('non-commercial', 'Non-Commercial'),
        # Add other types as needed
    ]

    sub_id = models.IntegerField(unique=True, null=False, verbose_name="Sub ID",default=0)
    name = models.CharField(max_length=256, null=False, unique=True, verbose_name="Name", default='Autre')
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    connector_activity_id = models.CharField(max_length=16, null=True, blank=True, verbose_name="Connector Activity ID")
    has_children = models.BooleanField(default=False, verbose_name="Has Children")
    to_be_reviewed = models.BooleanField(default=False, verbose_name="To Be Reviewed")
    type = models.CharField(max_length=64, choices=TYPE_CHOICES, null=True, blank=True, verbose_name="Type")
    jqpa = models.CharField(max_length=64, null=True, blank=True, verbose_name="JQPA")
    post_payment = models.SmallIntegerField(null=True, blank=True, verbose_name="Post Payment")
    
    class Meta:
        indexes = [
            models.Index(fields=['sub_id']),
            models.Index(fields=['name']),
        ]
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __str__(self):
        return f'sub_id: {self.sub_id}, name: {self.name}, id: {self.id}'
    
class SubSector(models.Model):
    sub_id = models.IntegerField(unique=True)  # Required, maps to the JSON id
    name = models.CharField(max_length=256, unique=True)  # Required
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        Sector,  # Points to the Activity model for parent
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='subsectors'
    )
    connector_activity_id = models.CharField(max_length=16, null=True, blank=True)
    has_children = models.BooleanField(default=False,null=True)
    to_be_reviewed = models.BooleanField(default=False)
    type = models.CharField(max_length=64,blank=True,null=True)
    jqpa = models.BooleanField(default=False,null=True)
    post_payment = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        parent_sub_id = self.parent.sub_id if self.parent else 'None'
        return f'id: {self.sub_id}\nname: {self.name}\nparent_sub_id: {self.parent.sub_id}'