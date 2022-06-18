from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListTodo

router = DefaultRouter()
router.register("todos", ListTodo, basename="todos")

urlpatterns = [
    # path('', ListTodo.as_view()),
    # path('<int:pk>/', DetailTodo.as_view()),
]

urlpatterns += router.urls
