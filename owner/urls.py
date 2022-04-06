from django.urls import path
from owner import views

urlpatterns = [

    path("mobiles/add", views.AddMobileView.as_view(), name="add_mobile"),
    path("mobiles/all", views.MobileListView.as_view(), name="list_mobiles"),
    path("mobile/<int:pk>", views.MobileDetailView.as_view(), name="mobile_detail"),
    path("mobile/delete/<int:id>", views.MobileDeleteView.as_view(), name="delete_mobile"),
    path("mobile/edit/<int:id>", views.MobileEditView.as_view(), name="edit_mobile"),
    path("dashboard", views.DashBoardView.as_view(), name="dashboard"),
    path("orders/detail/<int:id>", views.OrderDetailView.as_view(), name="order_detail"),
    path("logout", views.signout, name="logout")

]
