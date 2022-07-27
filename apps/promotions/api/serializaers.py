from rest_framework import serializers
from apps.promotions.models import Promotion
from apps.promotions.models import PromotionFiles

class PromotionFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionFiles
        exclude = ('state','created_date','modified_date','deleted_date')
    
class PromotionSerializer(serializers.ModelSerializer):
    file_content = PromotionFileSerializer(read_only=True, many=True)
    class Meta:
        model = Promotion
        exclude = ('state','created_date','modified_date','deleted_date')
        extra_kwargs = {
            "file_content": {
                "required": False,
            }
        }
