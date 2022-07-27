from django.db import models
from matplotlib import image
from apps.base.models import BaseModel

class PromotionFiles(BaseModel):
    media = models.FileField(upload_to='promos/')
    
    
class Promotion(BaseModel):
    title=models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    startTime=models.DateField(blank=True, null=True)
    endTime = models.DateField(blank=True, null=True)
    file_content=models.ManyToManyField(PromotionFiles, related_name='file_content', blank=True, null=True)
    
    class Meta:
        """Meta definition for Promotion."""

        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        """Unicode representation of Promotion."""
        return self.title