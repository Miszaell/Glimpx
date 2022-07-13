from apps.users.authentication_mixins import Authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import viewsets
from apps.health.api.serializers import PhysicalExpSerializer, ClinicalExpSerializer, FamilyBkgSerializer, AnamnesisSerializer
class PhysicalViewSet(viewsets.ModelViewSet):
    serializer_class=PhysicalExpSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        physical_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": physical_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        record = self.get_queryset(pk)
        if record:
            record_serializer = PhysicalExpSerializer(record)
            return Response(record_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            record_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if record_serializer.is_valid():
                record_serializer.save()
                return Response({'message':'record actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':record_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        record = self.get_queryset().filter(id=pk).first() # get instance        
        if record:
            record.state = False
            record.save()
            return Response({'message':'Record eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

class ClinicalViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicalExpSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        physical_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": physical_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        record = self.get_queryset(pk)
        if record:
            record_serializer = ClinicalExpSerializer(record)
            return Response(record_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            record_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if record_serializer.is_valid():
                record_serializer.save()
                return Response({'message':'record actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':record_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        record = self.get_queryset().filter(id=pk).first() # get instance        
        if record:
            record.state = False
            record.save()
            return Response({'message':'Record eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


class FamilyViewSet(viewsets.ModelViewSet):
    serializer_class = FamilyBkgSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        physical_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": physical_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        record = self.get_queryset(pk)
        if record:
            record_serializer = FamilyBkgSerializer(record)
            return Response(record_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            record_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if record_serializer.is_valid():
                record_serializer.save()
                return Response({'message':'record actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':record_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        record = self.get_queryset().filter(id=pk).first() # get instance        
        if record:
            record.state = False
            record.save()
            return Response({'message':'Record eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
