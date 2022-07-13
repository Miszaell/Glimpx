from pyexpat import model
from rest_framework import serializers
from apps.health.models import PhysicalExploration, ClinicalExploration, FamilyBackground, Anamnesis

class PhysicalExpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=PhysicalExploration
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class ClinicalExpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ClinicalExploration
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class FamilyBkgSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=FamilyBackground
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class AnamnesisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Anamnesis
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
