from django.contrib import admin
from django.urls import path, include
from .views import *
from .serializers import UserTestResultListView

from import_export.admin import ImportMixin

urlpatterns = [
    path('profile', UserInfoView.as_view(), name="profile"),
    path('skintypes/', SkinTypeList.as_view(), name='skintype-list'),
    path('questions/', QuestionView.as_view()),
    path('answers/', AnswerListView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('order/',OrderView.as_view()),

    path('report/Summary',OrderSummaryReport.as_view()),
    path('report/Users',UsersReportAPIView.as_view()),
    path('report/SalesReportByCategory',SalesReportByCategory.as_view()),
    path('report/AverageOrderValuePerUser',AverageOrderValuePerUser.as_view()),
    path('report/UserTestResultsReport',UserTestResultsReport.as_view()),
    path('report/CustomerBehaviorReport',CustomerBehaviorReport.as_view()),
    path('report/FinancialReportAPIView',FinancialReportAPIView.as_view()),
    path('report/SoldProducts', SoldProductsAPIView.as_view()),

    path('user_test_results/', UserTestResultView.as_view(), name='user-test-results'),
    path('usertestresults/', UserTestResultListView.as_view(), name='usertestresult-list'),
    path('medicines/', MedicineListView.as_view(), name='medicine-list'),
    path('usertestresults2/', UserTestResultList.as_view(), name='usertestresult-list'),
    # path('usertestresults/<int:pk>/', UserTestResultDetail.as_view(), name='usertestresult-detail'),
    path('registeruser/', CustomUserCreateView.as_view(), name='user-create'),
    path('rate_recomendation/', RateRecomendationView.as_view(), name='user-create'),
]
