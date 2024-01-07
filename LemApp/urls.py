from django.urls import path
from LemApp import views
urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:dataid>/',views.edit_category,name="edit_category"),
    path('Update_category/<int:dataid>/',views.Update_category,name="Update_category"),
    path('remv_category/<int:dataid>/',views.remv_category,name="remv_category"),
    path('product_page/',views.product_page,name="product_page"),
    path('save_product/',views.save_product,name="save_product"),
    path('display_product/',views.display_product,name="display_product"),
    path('edit_product/<int:pro_id>/',views.edit_product,name="edit_product"),
    path('Update_product/<int:dataid>/',views.Update_product,name="Update_product"),
    path('remv_product/<int:dataid>/',views.remv_product,name="remv_product"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('display_contact/',views.display_contact,name="display_contact"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact")

]