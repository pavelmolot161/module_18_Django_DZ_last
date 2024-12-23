
### - работало с костылями
# from django.contrib import admin
# from django.urls import path
#
# ### - 18.12.24 (+)
# from task4 import views
#
# urlpatterns = [
#
#     path('menu_task/', views.menu_task),                               ### - (+)
#     path('platform_task/', views.platform_task),                       ### - (+)
#     path('games_task/',views.games_task),                              ### - (+)
#     path('cart_task/',views.cart_task),                                ### - (+)
# ]

#___________________________________________________________________________________________________________

### - НЕ ИСПОЛЬЗОВАТЬ ДЛЯ ПРИМЕРА

# from django.contrib import admin
# from django.urls import path, include ### - (+)


# #from task3.views import platform_task, games_task, cart_task             ### - 18.12.24 task3 переехал в task4
# from task4.views import platform_task, games_task, cart_task, menu_task
# from django.views.generic import TemplateView
#
# urlpatterns = [
#     path('', platform_task),
#     path('admin/', admin.site.urls),                             ### - (+)
#     path('menu', menu_task),                                     ### - (+)
#     path('platform', platform_task),
#     path('games', games_task),
#     path('cart', cart_task),
# ]
