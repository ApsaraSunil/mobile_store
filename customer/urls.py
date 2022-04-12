from django.urls import path
from customer import views

urlpatterns = [

    path("accounts/register", views.SignupView.as_view(), name="signup"),
    path("", views.SigninView.as_view(), name="signin"),
    path("home", views.CustomerIndex.as_view(), name="cust_home"),
    path("accounts/password/reset", views.PasswordResetView.as_view(), name="password_reset"),
    path("mobile/detail/<int:id>", views.MobileDetailView.as_view(), name="mobile_detail"),
    path("carts/item/add/<int:id>", views.add_to_cart, name="add_to_cart"),
    path("carts/all", views.ViewMyCart.as_view(), name="view_my_cart"),
    path("cart/remove/<int:id>", views.remove_cart_item, name="remove_cart_item"),
    path("order/add/<int:p_id>/<int:c_id>", views.OrderCreateView.as_view(), name="order_create"),
    path("orders/all", views.OrderListView.as_view(), name="list_orders"),
    path("order/cancel/<int:id>", views.cancel_order, name="cancel_order"),
    path("profile/add", views.ProfileView.as_view(), name="profile"),
    path("my_profile", views.MyProfileView.as_view(), name="my_profile"),
    path("orders/feedback/add/<int:id>", views.FeedbackView.as_view(), name="feedback"),
    path("accounts/logout", views.signout, name="signout")

]
