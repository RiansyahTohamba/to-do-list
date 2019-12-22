from lists.models import List, Item
from lists.forms import DUPLICATE_ITEM_ERROR
from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueTogetherValidator


class ItemSerializer(serializers.ModelSerializer):
    text = serializers.CharField(
        allow_blank=False
    )

    class Meta:
        model = Item
        fields = ('id', 'list', 'text','deadline','is_finish')
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=('list', 'text'),
                message=DUPLICATE_ITEM_ERROR
            )
        ]



class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, source='not_finished')

    class Meta:
        model = List
        fields = ('id', 'items',)



class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer



class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()



router = routers.SimpleRouter()
router.register(r'lists', ListViewSet)
router.register(r'items', ItemViewSet)
