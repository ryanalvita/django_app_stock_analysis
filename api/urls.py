from django.urls import path

from . import views

urlpatterns = [
    path(
        "v1/<str:stock>/<str:report_type>/<str:statement_type>",
        views.get_stock_data,
        name="get_stock_data",
    ),
]
