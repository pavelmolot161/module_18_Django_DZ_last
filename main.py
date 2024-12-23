
### - 13.12.24

## - Эта команда вернет на один уровень выше в адресной строке:
#                                                            >>> cd ..

### - 1) установка Django: - (.venv) PS D:\module_18_Django> >>> pip install django

### - 2) Убедимся, что установка Django прошла успешно (не обязательно):
#                            (.venv) PS D:\module_18_Django> >>> python

### - 3) узнаем версию Django:                                    >>> django.get_version()   ??? - не сработало

### - 4) Создание проекта: -      (.venv) PS D:\module_18_Django> >>> django-admin startproject UrbanDjango

### - 5) создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:
#                                 (.venv) PS D:\module_18_Django> >>> cd UrbanDjango
#                     (.venv) PS D:\module_18_Django\UrbanDjango> >>> python manage.py migrate

### - 6) ЗАПУСK серверa разработки, (выполнив команду из корневого каталога проекта):
#                     (.venv) PS D:\module_18_Django\UrbanDjango> >>> python manage.py runserver

### - 7) Создание приложения:
#                     (.venv) PS D:\module_18_Django\UrbanDjango> >>> python manage.py startapp example1

### - 8) Создание файла зависимостей:
#             (.venv) PS D:\module_18_Django_DZ\UrbanDjango> >>> pip freeze > requirements.txt
#     8.a) вывод зависимостей в консоль:
#                                                            >>> pip freeze

'''Выполнен 1 пункт выполнен, 2 пункт выполнен, 3 пункт - не сработал, 4 пункт выполнен,
            7 пункт выполнен - создано 3 приложения с названиями 'example1', 'example2', 'example3'
            8 пункт выполнен - создан файл зависимостей requirements.txt.
            8 пункт выполнен сработал.
           '''

### - 15.12.24
### - 9) Создали приложение - task2

### - 10) Создали папку templates и в ней папку second_task:
##        - создаем 2 HTML шаблона - class_template.html, func_template.html

### - 11) В приложении task2 в файле views.py добавили:
##                   def func_temp(request):
#                       return render(request, "func_template.html")
#
#                    class class_temp(TemplateView):
#                       template_name = "class_template.html"

### - 12) В папке task файле settings.py:
#             в строке TEMPLATES = [] дополняем значение 'DIRS': [] == 'DIRS': [BASE_DIR / "templates"],
#             в строке INSTALLED_APPS = [] в конце дописываем имя нашего приложения 'app'

### - 13) Внесены дополнения в файл urls.py директории UrbanDjango:
                        # from UrbanDjango.task2.views import func_temp, class_temp
                        # urlpatterns = [
                        #     path('admin/', admin.site.urls),
                        #     path('', func_temp),
                        #     path('index/', class_temp.as_view())]



import django


#########################################################################################################

### - 13.12.24
### - Эта команда вернет на один уровень выше в адресной строке:
#                                                            >>> cd ..

### - 1) установка Django: - (.venv) PS D:\module_18_Django> >>> pip install django

### - 2) Убедимся, что установка Django прошла успешно (не обязательно):
#                            (.venv) PS D:\module_18_Django> >>> python

### - 3) узнаем версию Django:                               >>> django.get_version()

### - 4) Создание проекта: - (.venv) PS D:\module_18_Django> >>> django-admin startproject mysite

### - 5) создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:
#                            (.venv) PS D:\module_18_Django> >>> cd mysite
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py migrate

### - 6) ЗАПУСK серверa разработки:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py runserver

### - 7) Создание приложения:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py startapp app

### - 8) Создание файла зависимостей:
#             (.venv) PS D:\module_18_Django_DZ\UrbanDjango> >>> pip freeze > requirements.txt
#     8.a) вывод зависимостей в консоль:
#                                                            >>> pip freeze

### - 14.12.24
### - 9) В папке migrations в файле vievs.py создаем функцию:
                                                                # def index(request):
                                                                #     return render(request, "index.html")
### - 10) В папке mysite файле settings.py:
#             в строке TEMPLATES = [] дополняем значение 'DIRS': [] == 'DIRS': [BASE_DIR / "templates"],
#             в строке INSTALLED_APPS = [] в конце дописываем имя нашего приложения 'app'

### - 11) Создание папки templates и файла в ней index.html:
## Определение адреса в этом файле - urban https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami

### - 12) Внесение дополнений в папку mysite файл urls.py:
#                                 from mysite.app.views import index    ### - +
#                                 urlpatterns = [
#                                     path('admin/', admin.site.urls),
#                                     path('', index),                  ### - +
# ]

### - 15.12.24
### - поменял структуру проэкта и убрал вложенность папок проекта mysite, сделал все в ручную перепаскиванием
## соответственно поменялся путь запуска, но в чем была проблема я так и не понял.

### - 13) Внесение дополнений в папку mysite файл urls.py:
#                                 from app.views import index           ### - ++ импорт как в лекции
#                                 urlpatterns = [
#                                     path('admin/', admin.site.urls),
#                                     path('', index),                  ### - +

### - 14) ЗАПУСK НОВЫЙ серверa разработки, (выполнив команду из корневого каталога проекта):
#                     (.venv) PS D:\module_18_Django> >>> python manage.py runserver

### - 15) Создан новый файл HTML в папке templates c названием index2

### - 16) Создание класса в файле views.py папки app - class index2(TemplateView)

### - 17) В файл urls.py папки mysite добален импорт from app.views import index, + index2



























##############################################################################################################

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
