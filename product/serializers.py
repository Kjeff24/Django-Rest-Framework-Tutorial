from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    # including an arbitrary field, then pop from validate_data before creating or updating
    # email = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(validators=[validators.uniques_product_title, validators.validate_title_no_hello])
    # let name to be title
    # name = serializers.CharField(source='title', read_only=True) 
    
    class Meta:
        model = Product
        fields = ['owner', 'url', 'edit_url', 'pk', 'title', 'content', 'price', 'sale_price', 'my_discount']
    
        
    
    # def create(self, validated_data):
    #     email = validated_data.pop('email')
    #     return super().create(validated_data)
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)
        
    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        print(request)
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None