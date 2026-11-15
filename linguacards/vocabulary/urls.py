from django.urls import path # Imports the path function to map URL patterns to view functions (Importuje funkcję path do mapowania  wzorców URL na funkcje widoków)
from .views import word_list # Imports our word_list view function from the local views file (Importuje naszą funkcję widoku word_list z lokalnego pliku widoków)

urlpatterns = [ # Defines a list of URL patterns for this application (Definiuje listę wzorców URL dla tej aplikacji) 
    path('', word_list, name='word_list'), # Maps the root URL of the app to the word_list view, naming it word_list (Mapuje główny adres URL aplikacji na widok word_list, nadając mu nazwę word_list)
]