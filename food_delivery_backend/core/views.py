from rest_framework import viewsets, permissions
from .models import Restaurant, MenuItem, Order
from .serializers import RestaurantSerializer, MenuItemSerializer, OrderSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from firebase_admin import db

# Authentication should be handled by Firebase middleware
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        status = request.data.get('status')
        if status:
            # Update status in Firebase Realtime Database
            ref = db.reference(f"orders/{order.id}")
            ref.update({"status": status})
            order.status = status
            order.save()
            return Response({"status": "Order status updated"})
        return Response({"error": "Invalid status"}, status=400)
