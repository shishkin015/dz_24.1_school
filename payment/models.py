from django.db import models

from group.models import Well, Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES =[
        ('cash', 'наличные'),
        ('bank_transfer', 'перевод на счет'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE, related_name='payment')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')
    well = models.ForeignKey(Well, on_delete=models.SET_NULL, verbose_name='курс', **NULLABLE, related_name='payment')
    lesson = models.ForeignKey(Lesson,on_delete=models.SET_NULL, verbose_name='урок', **NULLABLE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='способ оплаты')

    def __str__(self):
        return f"Payment for {self.well} or {self.lesson} by {self.user.username}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
