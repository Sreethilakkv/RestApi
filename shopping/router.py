from customerapi.viewsets import CustomerViewset, ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer',CustomerViewset)
router.register('product',ProductViewset)