from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('home',views.home),
    path('viewall',views.viewall,name='viewall'),
    path('addproduct',views.AddProduct,name='addproduct'),
    path('addcategory',views.AddCategory,name='addcategory'),
    path('adminpage',views.AdminPage),
    path('allproducts',views.AllProducts,name='allproducts'),
    path('editproduct/<int:pk>',views.EditProduct.as_view(),name='editproduct'),
    path('deleteproduct/<int:pk>',views.DeleteProduct.as_view(),name='deleteproduct'),
    path('details/<int:id>',views.details,name='details'),
    path('register',views.reg,name='reg'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('profile/<int:id>',views.UserProfile,name='profile'),
    path('editprofile/<int:pk>',views.EditProfile.as_view(),name='editprofile'),
    path('users',views.UserListView.as_view(),name='users'),
    path('createuser',views.UserCreateView.as_view(),name='createuser'),
    path('deleteuser/<int:pk>',views.UserDeleteView.as_view(),name='userdelete'),
    path('kart/<int:id>',views.kart,name='kart'),
    path('addtokart/<int:id>/<int:price>/<name>/<rating>/<int:offer>',views.add_to_cart,name='addtokart'),
    path('removeproduct/<int:id>',views.remove_from_cart,name='removeproduct'),
    path('addinventory',views.AddInventory,name='addinventory'),
    path('inventorylist',views.InventoryListView.as_view(),name='listinventory'),
    path('checkout',views.checkout,name='checkout'),
    path('deliveryboy',views.DeliveryBoy,name='deliveryboy'),
    path('deliveryboylist',views.DeliveryBoyList,name='deliveryboylist')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)