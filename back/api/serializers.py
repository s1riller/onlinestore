from djoser.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, generics
from .models import User, SkinType, Answer, UserTestResult, Medicine, CategoryProduct, ImageProduct, Order, OrderItem
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from versatileimagefield.serializers import VersatileImageFieldSerializer


class CustomUserSerializer(UserSerializer):
    birth_date = serializers.DateField()

    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name',
                  'birth_date')  # Добавьте поля, которые хотите запросить при регистрации

    def create(self, validated_data):
        # Извлекаем и удаляем пароль из validated_data
        password = validated_data.pop('password', None)

        # Создаем пользователя без пароля
        user = super(CustomUserSerializer, self).create(validated_data)

        # Устанавливаем зашифрованный пароль
        if password:
            user.set_password(password)
            user.save()

        return user


class SkinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinType
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'text', 'img']


class UserTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTestResult
        fields = '__all__'


class UserTestResultListView(generics.ListCreateAPIView):
    queryset = UserTestResult.objects.all()
    serializer_class = UserTestResultSerializer


class UserResul(serializers.ModelSerializer):
    class Meta:
        model = UserTestResult
        fields = '__all__'


class RatingSerializer(serializers.Serializer):
    testId = serializers.IntegerField()
    rating = serializers.IntegerField()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = ['id', 'name']


class ProductImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),  # 'url' - это способ получить исходное изображение
            # ('thumbnail', 'thumbnail__100x100'),  # Создать миниатюру 100x100
            # ('medium_square_crop', 'crop__400x400'),  # Обрезать изображение до 400x400
            # ('small_square_crop', 'crop__50x50'),  # Обрезать изображение до 50x50
        ]
    )

    class Meta:
        model = ImageProduct
        fields = ['title', 'image', 'medicine']


class MedicineSerializer(serializers.ModelSerializer):
    # images = ProductImageSerializer(many=True, read_only=True)
    img = Base64ImageField(required=False)

    class Meta:
        model = Medicine
        fields = ['id', 'name', 'description', 'treats', 'price', 'category', 'img']


class OrderItemSerializer(serializers.ModelSerializer):
    product = MedicineSerializer()

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'full_name', 'email', 'phone', 'address', 'postal_code', 'delivery_date',
                  'delivery_instructions', 'total_price', 'delivery_fee', 'status', 'order_items']


class UserReadSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'birth_date', 'avatar_url', 'last_login')

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        if obj.avatar and hasattr(obj.avatar, 'url'):
            return request.build_absolute_uri(obj.avatar.url)
        return None


class OrderReadItemSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ('product', 'avatar_url', 'quantity')

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        if obj.product.img and hasattr(obj.product.img, 'url'):
            return request.build_absolute_uri(obj.product.img.url)
        return None


class SoldProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_description = serializers.CharField(source='product.description')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)
    product_category = serializers.CharField(source='product.category.name')
    sale_date = serializers.DateTimeField(source='order.created_at')
    product_image_url = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_description', 'product_price', 'product_category', 'quantity', 'sale_date', 'product_image_url']

    def get_product_image_url(self, obj):
        request = self.context.get('request')
        if obj.product.img and hasattr(obj.product.img, 'url'):
            return request.build_absolute_uri(obj.product.img.url)
        return None