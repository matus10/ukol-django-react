from rest_framework import serializers
from .models import Client, Account, Balance, Transaction, TransactionType

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id_client', 'first_name', 'last_name', 'email', 'phone', 'address', 'created_at']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'client', 'account_number', 'currency', 'created_at']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['id', 'account', 'amount', 'principal_amount', 'interest_amount', 'fee_amount', 'created_at', 'snapshot_date']

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'transaction_type', 'transaction_date']

