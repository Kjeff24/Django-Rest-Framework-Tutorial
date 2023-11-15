from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from product.models import Product
from product.serializers import ProductSerializer

# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({"Invalid": "not good data"}, status=400)