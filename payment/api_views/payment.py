from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from group.permissions import IsModerator, IsModerOrOwner
from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('well', 'lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
    permission_classes = [IsModerator, IsModerOrOwner]
