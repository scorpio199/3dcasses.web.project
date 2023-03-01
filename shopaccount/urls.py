from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_view/<data>', views.create_view, name='create_view'),
    path('list_view/', views.list_view, name='list_view'),
    path('detail_view/<id>/<data>', views.detail_view, name='detail_view'),
    path('update_view/<id>/<data>', views.update_view, name='update_view'),
    path('delete_item/<id>', views.delete_item, name='delete_item'),    

    # API data
    path('list_marketplace/', views.list_marketplace, name='list_marketplace'),
    path('list_transaction/<start_date>/<end_date>', views.list_transaction, name='list_transaction'),
    path('list_detail/<id>/<data>/<start_date>/<end_date>', views.list_detail, name='list_detail')
    
] 

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)