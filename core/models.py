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
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse("country_detail", kwargs={"pk": self.pk})
    
     

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
        return f'{self.name}'
    
class SubSector(models.Model):
    sub_id = models.IntegerField(unique=True)  # Required, maps to the JSON id
    name = models.CharField(max_length=256,default='Autre')  # Required unique=True
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
        return f'{self.name}'

class BusinessActivity(models.Model):

    QUESTION1 = _("Quand souhaitez-vous débuter votre activité ?")
    QUESTION2 = _('Avez-vous déjà exercé une activité non-salariée ?')

    MICRO = 'micro'
    AUTRE = 'autre'
    NON = 'non'

    BUSINESS_CHOICES = (
        (NON, _("Non")),
        (MICRO, _("Oui, micro-entreprise / entrepreneur individuel")),
        (AUTRE, _("Oui, EURL, SARL, SASU, SAS, etc.")),
    )

    activity_type = models.CharField(
        max_length=20,
        choices=BUSINESS_CHOICES,
        default=NON,
        verbose_name=_("Avez-vous déjà exercé une activité non-salariée ?")
    )
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL,null=True, default=BUSINESS_CHOICES[0][0], verbose_name=_("Domaine d'activité"))
    when_to_start = models.DateField(default=date.today, null=True,verbose_name=QUESTION1)
    commercial_name = models.CharField(max_length=256, blank=True, null=True)
    
    def __str__(self):
        return self.QUESTION2

class BusinessAddress(models.Model):
    street_address = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=20, db_index=True, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, default='France')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"
        indexes = [
            models.Index(fields=['postal_code', 'city']),
        ]

    def __str__(self):
        return self.generate_full_address()

    def generate_full_address(self):
        address_parts = []
        if self.street_address:
            address_parts.append(self.street_address)
        if self.postal_code and self.city:
            address_parts.append(f"{self.postal_code} {self.city}")
        if self.country:
            address_parts.append(str(self.country))
        return ", ".join(address_parts)

    def formatted_address(self):
        return self.generate_full_address()