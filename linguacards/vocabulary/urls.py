from django.urls import path  # Imports the path function (Importuje funkcję path)
from .views import word_list, add_word  # Imports both word_list and add_word view functions from views.py (Importuje obie funkcje widoków word_list i add_word z pliku views.py)

urlpatterns = [  # Defines URL routing list (Definiuje listę routingu URL)
    path('', word_list, name='word_list'),  # Maps the root URL to the word_list view (Mapuje główny adres URL na widok word_list)
    path('add/', add_word, name='add_word'),  # Maps the '/add/' URL path to our add_word view, naming it add_word (Mapuje ścieżkę URL '/add/' do naszego widoku add_word, nadając jej nazwę add_word)
]