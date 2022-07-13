from django.db import models
from apps.base.models import BaseModel
from enum import Enum


# class MaterialUOM(Enum):
#     pz = "Piezas"
#     gr = "Gramos"
#     ml = "Mililitros"
class Medicine(BaseModel):
    distinctive_denmination=models.CharField(max_length=250)
    generic_denomination=models.CharField(max_length=250)
    pharmaceutical_denomination=models.CharField(max_length=250)
    drug_concentration=models.CharField(max_length=250)
    formula=models.CharField(max_length=250)
    route_administration=models.CharField(max_length=250)
    precautions=models.CharField(max_length=250)
    quantity=models.DecimalField(max_digits=5, decimal_places=2)
    uom=models.CharField(max_length=250)
    
    class Meta:
        """Meta definition for Medicine."""

        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'

    def __str__(self):
        """Unicode representation of Product."""
        return self.distinctive_denmination
class Material(BaseModel):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    quantity=models.DecimalField(max_digits=5, decimal_places=2)
    uom=models.CharField(max_length=50)
# uom=models.CharField(max_length=50, choices=[(tag, tag.value) for tag in MaterialUOM])
    
    class Meta:
        """Meta definition for Material."""

        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        """Unicode representation of Material."""
        return self.name

    
class Stock(BaseModel):
    product=models.ForeignKey(Medicine, on_delete=models.CASCADE)
    material=models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'

    def __str__(self):
        """Unicode representation of Stock."""
        return self.product
