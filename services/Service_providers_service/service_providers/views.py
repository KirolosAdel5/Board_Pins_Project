from rest_framework import generics,viewsets
from .models import ServiceCategory, ServiceProviderType, ServiceProviderSpecification, ServiceProvider, Tag, ServiceProviderSpecificationValue, ServiceProviderImage, ServiceProviderReview, SocialLink, ServiceProviderProduct
from .serializers import ServiceCategorySerializer, ServiceProviderTypeSerializer, ServiceProviderSpecificationSerializer, ServiceProviderSerializer, TagSerializer, ServiceProviderSpecificationValueSerializer, ServiceProviderImageSerializer, ServiceProviderReviewSerializer, SocialLinkSerializer, ServiceProviderProductSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
import requests
from .permissions import IsStaffOrReadOnly
class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.filter(parent=None)
    serializer_class = ServiceCategorySerializer
    permission_classes = [IsStaffOrReadOnly]


class CurrentUserView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')

        response = requests.get('http://127.0.0.1:8001/api/userinfo/', headers={'Authorization': auth_header})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            current_user = response.json()
            return JsonResponse(current_user)
        else:
            return JsonResponse({'error': 'Failed to fetch current user'}, status=response.status_code)
