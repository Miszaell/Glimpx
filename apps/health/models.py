from django.db import models
from apps.base.models import BaseModel
from apps.users.models import User
class PhysicalExploration(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    temperature=models.DecimalField(max_digits=5, decimal_places=2)
    pulse=models.DecimalField(max_digits=5, decimal_places=2)
    heart_rate=models.DecimalField(max_digits=5, decimal_places=2)
    breathing_rate=models.DecimalField(max_digits=5, decimal_places=2)
    weight=models.DecimalField(max_digits=5, decimal_places=2)
    height=models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        """Meta definition for Physical Exploration."""

        verbose_name = 'Physical Exploration'
        verbose_name_plural = 'Physical Explorations'

    def __str__(self):
        """Unicode representation of Physical Exploration."""
        return self.user.name
    
class ClinicalExploration(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    contagious_infections_desease=models.TextField()
    chronic_degenerative_disease=models.TextField()
    traums=models.TextField()
    allergic=models.TextField()
    surgical=models.TextField()
    previous_hospitalizations=models.TextField()
    transfusions=models.TextField()
    drugs_addiction_alcoholism=models.TextField()
    
    class Meta:
        """Meta definition for Clinical Exploration."""

        verbose_name = 'Clinical Exploration'
        verbose_name_plural = 'Clinical Explorations'

    def __str__(self):
        """Unicode representation of Clinical Exploration."""
        return self.user.name
    
class FamilyBackground(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neoplasm=models.TextField()
    chronic_degenerative_diseases=models.TextField()
    metabolic_endocrine_diseases=models.TextField()
    
    class Meta:
        """Meta definition for Family Background."""

        verbose_name = 'Family Background'
        verbose_name_plural = 'Family Backgrounds'

    def __str__(self):
        """Unicode representation of Family Background."""
        return self.user.name
    
class Anamnesis(BaseModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    physical_exp=models.ForeignKey(PhysicalExploration, on_delete=models.CASCADE)
    clinical_exp=models.ForeignKey(ClinicalExploration, on_delete=models.CASCADE)
    family_bkg=models.ForeignKey(FamilyBackground, on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for Anamnesis."""

        verbose_name = 'Anamnesis'
        verbose_name_plural = 'Anamnesiss'

    def __str__(self):
        """Unicode representation of Anamnesis."""
        return self.user.name