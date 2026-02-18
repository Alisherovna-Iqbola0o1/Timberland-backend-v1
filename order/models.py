from django.db import models
from product.models import Product
from user.models import User, UserAddress


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} | {self.product} | {self.quantity}"


class OrderPayment(models.TextChoices):
    CASH = "cash", "Naqd"
    CLICK = "click", "CLICK orqali"
    PAYME = "payme", "PAYME orqali"
    CART = "cart", "Karta orqali"
    OTHER = "other", "Boshqa"


class OrderStatus(models.TextChoices):
    NEW = "new", "Yangi"
    WAITING = "waiting", "Kutulmoqda"
    IN_PROGRESS = "in_progress", "Jarayonda"
    WAITING_PAYMENT = "waiting_payment", "Tolovni kutmoqda"
    DELIVERING = "delivering", "Yetkazilmoqda"
    DELIVERED = "delivered", "Yetkazildi"
    COMPLETED = "completed", "Yakunlandi"
    CANCELLED_BY_CUSTOMER = "cancelled_by_customer", "Xaridor bekor qildi"
    CANCELLED_BY_SELLER = "cancelled_by_seller", "Sotuvchi bekor qildi"


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    payment_type = models.CharField(max_length=50, choices=OrderPayment.choices, default=OrderPayment.CASH)
    status = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} | {self.user} | {self.status}"


class OrderItems(models.Model):
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_order.user} | {self.product} | {self.quantity}"
