from rest_framework import serializers
from .models import ServiceCategory, ServiceProviderType, ServiceProviderSpecification, ServiceProvider, Tag, ServiceProviderSpecificationValue, ServiceProviderImage, ServiceProviderReview, SocialLink, ServiceProviderProduct
from rest_framework_recursive.fields import RecursiveField

class ServiceCategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = '__all__'


    def get_children(self, instance):
        children_queryset = ServiceCategory.objects.filter(parent=instance)
        children_serializer = self.__class__(children_queryset, many=True)
        return children_serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        children_data = representation.pop('children', None)
        if children_data:
            representation['Children'] = children_data
        return representation

class ServiceProviderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviderType
        fields = '__all__'

class ServiceProviderSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviderSpecification
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ServiceProviderSpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviderSpecificationValue
        fields = '__all__'

class ServiceProviderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviderImage
        fields = '__all__'

class ServiceProviderReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviderReview
        fields = '__all__'

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

class ServiceProviderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProviderProduct
        fields = '__all__'
        
class ServiceProviderSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer()
    service_provider_type = ServiceProviderTypeSerializer()
    tags = TagSerializer(many=True)
    specification_values = ServiceProviderSpecificationValueSerializer(many=True)
    service_provider_images = ServiceProviderImageSerializer(many=True)
    service_provider_reviews = ServiceProviderReviewSerializer(many=True)
    social_links = SocialLinkSerializer(many=True)
    products = ServiceProviderProductSerializer(many=True)

    class Meta:
        model = ServiceProvider
        fields = '__all__'

