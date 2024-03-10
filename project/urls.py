# from project.purchase import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project.purchase.views import PurchaseRequestViewSet



router = DefaultRouter()


router.register(r'purchaserequest', PurchaseRequestViewSet, basename='purchaserequest')  





urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

#company urls
#     path('getcmp/', views.get_cmp),
#     path('postcmp/', views.add_cmp),
#     path('updatecmp/<int:pk>/', views.update_cmp),
#     path('deletecmp/<int:pk>/', views.delete_cmp),


# #department urls
#     path('getdp/', views.get_dp),
#     path('postdp/', views.add_dp),
#     path('updatedp/<int:pk>/', views.update_dp),
#     path('deletedp/<int:pk>/', views.delete_dp),


# #user urls
#     path('getuser/', views.get_user),
#     path('postuser/', views.add_user),
#     path('updateuser/<int:pk>/', views.update_user),
#     path('deleteuser/<int:pk>/', views.delete_user),



# #item urls
#     path('getitem/', views.get_item),
#     path('postitem/', views.add_item),
#     path('updateitem/<int:pk>/', views.update_item),
#     path('deleteitem/<int:pk>/', views.delete_item),


# #type urls
#     path('gettype/', views.get_type),
#     path('posttype/', views.add_type),
#     path('updatetype/<int:pk>/', views.update_type),
#     path('deletetype/<int:pk>/', views.delete_type),


# #urgency urls
#     path('geturgency/', views.get_urgency),
#     path('posturgency/', views.add_urgency),
#     path('updateurgency/<int:pk>/', views.update_urgency),
#     path('deleteurgency/<int:pk>/', views.delete_urgency),


# #approver urls
#     path('getapprover/', views.get_approver),
#     path('postapprover/', views.add_approver),
#     path('updateapprover/<int:pk>/', views.update_approver),
#     path('deleteapprover/<int:pk>/', views.delete_approver),


# #ac urls
#     path('getac/', views.get_ac),
#     path('postac/', views.add_ac),
#     path('updateac/<int:pk>/', views.update_ac),
#     path('deleteac/<int:pk>/', views.delete_ac),


# #purchasereq urls
#     path('getpurchasereq/', views.get_purchasereq),
#     path('purchasereqnew/', views.newpurchasereq),
#     path('updatepurchasereq/<int:pk>/', views.update_purchasereq),
#     path('deletepurchasereq/<int:pk>/', views.delete_purchasereq),



# #purchaseitem urls
#     path('getpurchaseitem/', views.get_purchaseitem),
#     path('postpurchaseitem/', views.add_purchaseitem),
#     path('updatepurchaseitem/<int:pk>/', views.update_purchaseitem),
#     path('deletepurchaseitem/<int:pk>/', views.delete_purchaseitem),



# #approverreq req urls
#     path('getappreq/', views.get_appreq),
#     path('postappreq/', views.add_appreq),
#     path('updateappreq/<int:pk>/', views.update_appreq),
#     path('deleteappreq/<int:pk>/', views.delete_appreq),




















]


