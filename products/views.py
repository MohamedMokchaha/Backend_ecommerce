from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        in_stock = request.query_params.get('in_stock', None)
        if in_stock is not None:
            if in_stock == 'true':
                products = self.queryset.filter(stock__gt=0)
            elif in_stock == 'false':
                products = self.queryset.filter(stock=0)
            else:
                return Response({"detail": "Valeur 'in_stock' incorrecte."}, status=400)
        else:
            products = self.queryset

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
