from django.contrib import admin
from apps.health.models import PhysicalExploration, ClinicalExploration, FamilyBackground, Anamnesis

admin.site.register(PhysicalExploration)
admin.site.register(ClinicalExploration)
admin.site.register(FamilyBackground)
admin.site.register(Anamnesis)
