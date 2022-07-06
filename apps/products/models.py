from django.db import models
from apps.base.models import BaseModel
class Medicine(BaseModel):
    distinctive_denmination=models.CharField(max_length=250)
    generic_denomination=models.CharField(max_length=250)
    pharmaceutical_denomination=models.CharField(max_length=250)
    drug_concentration=models.CharField(max_length=250)
    formula=models.CharField(max_length=250)
    route_administration=models.CharField(max_length=250)
    precautions=models.CharField(max_length=250)
    quantity=models.IntegerField()
    uom=models.CharField(max_length=250)
    
    
class Material(BaseModel):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    quantity=models.IntegerField()
    uom=models.CharField(max_length=250)
    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

    
class Stock(BaseModel):
    product=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    material=models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity=models.IntegerField()