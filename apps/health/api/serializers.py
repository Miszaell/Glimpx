from pyexpat import model
from rest_framework import serializers
from apps.health.models import PhysicalExploration, ClinicalExploration, FamilyBackground, Anamnesis
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

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
        exclude = ('state', 'created_date', 'deleted_date')
        
    def get_user(self, pk):
        user=User.objects.filter(id=pk).first()
        data=UserSerializer(user)
        return data.data
        
    def get_phys(self, pk):
        physical=PhysicalExploration.objects.filter(id=pk).first()
        data=PhysicalExpSerializer(physical)
        return data.data
        
    def get_cli(self, pk):
        clinical=ClinicalExploration.objects.filter(id=pk).first()
        data=ClinicalExpSerializer(clinical)
        return data.data
        
    def get_fam(self, pk):
        family=FamilyBackground.objects.filter(id=pk).first()
        data=FamilyBkgSerializer(family)
        return data.data
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'modified_date': instance.modified_date,
            'username': instance.user.__str__(),
            'user': self.get_user(instance.user.id),
            'physical_exp': self.get_phys(instance.physical_exp.id),
            'clinical_exp': self.get_cli(instance.clinical_exp.id),
            'family_bkg': self.get_fam(instance.family_bkg.id),
        }
