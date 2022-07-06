from rest_framework import serializers
from apps.products.models import Material, Medicine


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'quantity': instance.quantity,
            'uom': instance.uom
        }


class MaterialRetrieveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Material
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class MedicineSerializer(serializers.Serializer):

    class Meta:
        model = Medicine
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def create(self, validated_data):
        medicine = Medicine(**validated_data)
        medicine.save()
        return medicine
