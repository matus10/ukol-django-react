from django.urls import path, include
from .views.client_views import ClientViewSet
from .views.account_views import AccountViewSet
from .views.balance_views import BalanceViewSet
from .views.transaction_views import TransactionViewSet
from .views.transaction_type_views import TransactionTypeViewSet
from rest_framework.routers import DefaultRouter

class CustomRouter(DefaultRouter):
    def __init__(self):
        super().__init__()
        self.trailing_slash = '/?'

router = CustomRouter()
router.register(r'clients', ClientViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'balances', BalanceViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'transaction-types', TransactionTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]