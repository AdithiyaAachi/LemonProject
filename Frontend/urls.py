from django.urls import path
from Frontend import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/',views.productpage,name="productpage"),
    path('product_filtered/<cat_name>/',views.product_filtered,name="product_filtered"),
    path('single_product/<int:proid>/',views.single_product,name="single_product"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('registerpage/',views.registerpage,name="registerpage"),
    path('register_save/',views.register_save,name="register_save"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cartdelete/<int:pro_id>/',views.cartdelete,name="cartdelete"),
    path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
    path('yourorder/',views.yourorder,name="yourorder"),

]