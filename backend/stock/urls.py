from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategorieViewSet, MaterielViewSet, MouvementViewSet, InventaireViewSet

router = DefaultRouter()
router.register(r'categories', CategorieViewSet)
router.register(r'materiels', MaterielViewSet)
router.register(r'mouvements', MouvementViewSet)
router.register(r'inventaires', InventaireViewSet)

urlpatterns = [
    path('', include(router.urls)),
]