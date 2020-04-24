from django.urls import path
from base.views import(
    home,
    companypage,
)

app_name='base'

urlpatterns = [
    path('<int:company_id>/', companypage, name="companypage" ),
    path('', home, name="home" ),
]
