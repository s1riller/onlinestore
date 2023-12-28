from datetime import datetime

from django.shortcuts import render
from rest_framework import generics, parsers, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import SkinType, Question, Answer, UserTestResult, Medicine
from django.db.models import Sum, Count, Avg
from .serializers import *
import json
import base64
import io
from django.core.files.base import ContentFile


# Create your views here.
def profile_view(request):
    return render(request, 'api/profile.html')


class SkinTypeList(generics.ListCreateAPIView):
    queryset = SkinType.objects.all()
    serializer_class = SkinTypeSerializer


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            'id': user.id,  # Добавляем идентификатор пользователя
            'birth_date': user.birth_date,  # Добавляем идентификатор пользователя
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
            'is_admin': user.is_staff,
        }
        return Response(data)

    def put(self, request):
        user = request.user
        data = request.data

        # Обновляем данные пользователя, если они предоставлены в запросе
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.birth_date = data.get('birth_date', user.birth_date)

        # Сохраняем изменения
        user.save()

        return Response({
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birth_date': user.birth_date,
        }, status=status.HTTP_200_OK)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        data = []
        for question in questions:
            answers = Answer.objects.filter(question=question)
            serializer = AnswerSerializer(answers, many=True)
            data.append({
                'id': question.id,
                'question': question.text,
                'answers': serializer.data
            })
        return Response(data)


class UserTestResultView(APIView):
    def post(self, request, format=None):
        serializer = UserTestResultSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicineListView(generics.ListAPIView):
    serializer_class = MedicineSerializer

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        medicines = Medicine.objects.all()
        return medicines

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        serializer = self.get_serializer(data=request.data)
        if CategoryProduct.objects.filter(name=name).exists():
            return Response({'error': 'Товар с таким названием уже существует'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTestResultList(generics.ListAPIView):
    serializer_class = UserTestResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Получите объекты UserTestResult текущего пользователя (по токену доступа)
        user = self.request.user
        return UserTestResult.objects.filter(user=user.id)


class UserTestResultDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTestResult.objects.all()
    serializer_class = UserTestResultSerializer


class CustomUserCreateView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateRecomendationView(APIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RateRecomendationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            test_id = serializer.validated_data['testId']
            rating = serializer.validated_data['rating']

            try:
                test_result = UserTestResult.objects.get(id=test_id)
            except UserTestResult.DoesNotExist:
                return Response({'message': 'Test result not found'}, status=status.HTTP_404_NOT_FOUND)

            test_result.rate = rating
            test_result.save()

            # Сериализуем объект test_result и отправляем его в ответе
            serialized_test_result = UserTestResultSerializer(test_result)

            return Response({'message': 'Rating saved successfully', 'test_result': serialized_test_result.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        return Answer.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        return CategoryProduct.objects.all()

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        serializer = self.get_serializer(data=request.data)
        if CategoryProduct.objects.filter(name=name).exists():
            return Response({'error': 'Категория с таким названием уже существует'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        return Order.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Получите данные о заказанных товарах из запроса
            print(request.data)
            order_items_data = request.data.get('order_items')

            # Создайте заказ
            order = serializer.save()
            print(order_items_data)
            # Добавьте товары в заказ с указанием количества
            for item_data in order_items_data:
                product_id = item_data.get('product')
                quantity = item_data.get('quantity')
                product = Medicine.objects.get(pk=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderSummaryReport(APIView):

    def get(self, request):

        # Получите дату первого заказа
        first_order_date = Order.objects.earliest('created_at').created_at

        # Получите дату последнего заказа
        last_order_date = Order.objects.latest('created_at').created_at

        response = {
            'first_date': first_order_date.strftime('%Y-%m-%d %H:%M:%S'),  # Форматируйте дату, если нужно
            'last_date': last_order_date.strftime('%Y-%m-%d %H:%M:%S'),  # Форматируйте дату, если нужно
        }

        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):

        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')

        if not start_date:
            return Response({'error': 'start_date not specified'}, status=status.HTTP_400_BAD_REQUEST)

        if not end_date:
            return Response({'error': 'end_date not specified'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Преобразуйте дату из строки в объект datetime
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return Response({'error': 'Invalid date format. Use YYYY-MM-DD'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Получите суммарную стоимость всех заказов за указанный период
        total_sales = Order.objects.filter(
            created_at__gte=start_date, created_at__lte=end_date
        ).aggregate(total_sales=Sum('total_price'))['total_sales']

        # Получите количество заказов за указанный период
        total_orders = Order.objects.filter(
            created_at__gte=start_date, created_at__lte=end_date
        ).count()

        # Получите средний размер заказа за указанный период
        average_order_size = Order.objects.filter(
            created_at__gte=start_date, created_at__lte=end_date
        ).aggregate(average_order_size=Avg('total_price'))['average_order_size']

        orders = Order.objects.filter(
            created_at__gte=start_date, created_at__lte=end_date
        )

        serialized_orders = OrderSerializer(orders, many=True)

        # Верните отчет в формате JSON
        report_data = {
            'start_date': start_date.strftime('%Y-%m-%d'),
            'end_date': end_date.strftime('%Y-%m-%d'),
            'total_sales': total_sales or 0,
            'total_orders': total_orders,
            'average_order_size': average_order_size or 0,
            'orders': serialized_orders.data,
        }

        return Response(report_data, status=status.HTTP_200_OK)


class SalesReportByCategory(APIView):

    def get(self, request, *args, **kwargs):
        # Группировка по категориям и расчет сумм и количества
        category_sales = OrderItem.objects.values('product__category__name') \
            .annotate(total_sales=Sum('product__price', field='product__price * quantity'),
                      total_quantity=Sum('quantity'),
                      count=Count('id')) \
            .order_by('product__category')

        # Форматирование данных для ответа
        report_data = [{'category': entry['product__category__name'],
                        'total_sales': entry['total_sales'],
                        'total_quantity': entry['total_quantity'],
                        'count': entry['count']} for entry in category_sales]

        return Response(report_data)


class AverageOrderValuePerUser(APIView):

    def get(self, request, *args, **kwargs):
        # Группировка заказов по пользователям и расчет среднего значения суммы заказов
        average_order_value = Order.objects.values('user__username') \
            .annotate(average_order_value=Avg('total_price')) \
            .order_by('user')

        # Форматирование данных для ответа
        report_data = [{
            'user': entry['user__username'],
            'average_order_value': entry['average_order_value']
        } for entry in average_order_value]

        return Response(report_data)


class UserTestResultsReport(APIView):
    """
    Отчет о результатах пользовательских тестов и предпочтениях.
    """

    def get(self, request, format=None):
        # Получаем все результаты тестов
        test_results = UserTestResult.objects.all()

        # Статистика по предпочтениям пользователя
        preference_stats = test_results.values('answers').annotate(
            total=Count('id'),
            average_rate=Avg('rate')
        )

        # Собираем данные для отчета
        report_data = {
            'preference_stats': list(preference_stats),
            'total_tests': test_results.count()
        }

        return Response(report_data, status=status.HTTP_200_OK)


class CustomerBehaviorReport(APIView):
    """
    Отчет о поведении покупателей.
    """

    def get(self, request, format=None):
        # Общее количество заказов
        total_orders = Order.objects.count()

        # Средний чек
        average_order_value = Order.objects.aggregate(Avg('total_price'))['total_price__avg'] or 0

        # Топ продуктов по продажам
        top_products = OrderItem.objects.values('product__name').annotate(
            total_sold=Sum('quantity')
        ).order_by('-total_sold')[:10]

        # Активность покупателей
        customer_activity = User.objects.annotate(
            total_orders=Count('orders')
        ).order_by('-total_orders')[:10]

        # Собираем данные для отчета
        report_data = {
            'total_orders': total_orders,
            'average_order_value': average_order_value,
            'top_products': list(top_products),
            'customer_activity': list(customer_activity.values('username', 'total_orders')),
        }

        return Response(report_data, status=status.HTTP_200_OK)


class FinancialReportAPIView(APIView):
    def get(self, request):
        # Получение параметров фильтрации (если они есть)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        # Фильтрация заказов по дате (если указаны даты)
        if start_date and end_date:
            orders = Order.objects.filter(created_at__date__gte=start_date, created_at__date__lte=end_date)
        else:
            orders = Order.objects.all()

        # Расчет финансовых показателей
        total_sales = orders.aggregate(Sum('total_price'))['total_price__sum'] or 0
        total_delivery_fees = orders.aggregate(Sum('delivery_fee'))['delivery_fee__sum'] or 0
        average_order_value = orders.aggregate(Avg('total_price'))['total_price__avg'] or 0
        total_orders = orders.count()

        # Формирование ответа
        report = {
            'total_sales': total_sales,
            'total_delivery_fees': total_delivery_fees,
            'average_order_value': average_order_value,
            'total_orders': total_orders
        }

        return Response(report, status=status.HTTP_200_OK)


class UsersReportAPIView(APIView):
    serializer_class = CustomUserSerializer
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        users = User.objects.all()
        serializer = UserReadSerializer(users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)




class SoldProductsAPIView(APIView):
    def get(self, request, format=None):
        sold_items = OrderItem.objects.all()
        # Pass 'request' in the serializer context
        serializer = SoldProductSerializer(sold_items, many=True, context={'request': request})
        return Response(serializer.data)