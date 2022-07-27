from apps.promotions.models import Promotion, PromotionFiles
from apps.users.authentication_mixins import Authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import viewsets
from apps.promotions.api.serializaers import PromotionSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    parser_classes = (JSONParser, MultiPartParser)
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        product_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": product_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        files = request.FILES.getlist('file_content')
        if files:
            request.data.pop('file_content')
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                promos = Promotion.objects.get(id=serializer.data['id'])
                uploaded_files = []
                
                for file in files:
                    content = PromotionFiles.objects.create(media=file)
                    uploaded_files.append(content)
                promos.file_content.add(*uploaded_files)
                context = serializer.data
                context["file_content"] = [file.id for file in uploaded_files]
                return Response({'message': 'Promocion creado correctamente!'}, status=status.HTTP_201_CREATED)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
            return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = PromotionSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Promocion con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message': 'Promocion actualizada correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()  # get instance
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Promocion eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una Promocion con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
