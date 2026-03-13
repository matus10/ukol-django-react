from django.db import models

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    personal_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} - {self.account_number}"

class Balance(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='balances')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    principal_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_amount = models.DecimalField(max_digits=15, decimal_places=2)
    fee_amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    snapshot_date = models.DateField()
    
    def __str__(self):
        return f"{self.account.client.first_name} {self.account.client.last_name} : {self.amount}"
    
class TransactionType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='transactions')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT)
    transaction_date = models.DateTimeField()

    
    def __str__(self):
        return f"{self.account.account_number} - {self.transaction_type} - {self.amount}"