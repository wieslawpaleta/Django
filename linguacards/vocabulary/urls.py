from django.urls import path  # Imports path function (Importuje funkcję path)
from .views import word_list, add_word, update_word, delete_word, study_mode, toggle_learned  # Imports all view functions (Importuje wszystkie funkcje widoków)

urlpatterns = [  # Defines URL routing list (Definiuje listę routingu URL)
    path('', word_list, name='word_list'),  # Route for main word list page (Ścieżka dla głównej strony listy słówek)
    path('add/', add_word, name='add_word'),  # Route for adding a new word (Ścieżka do dodawania nowego słówka)
    path('update/<int:word_pk>/', update_word, name='update_word'),  # Route for editing a specific word using its integer ID (Ścieżka do edycji konkretnego słówka za pomocą jego ID całkowitego)
    path('delete/<int:word_pk>/', delete_word, name='delete_word'),  # Route for deleting a specific word using its integer ID (Ścieżka do usuwania konkretnego słówka za pomocą jego ID całkowitego)
    path('study/', study_mode, name='study_mode'),  # Maps '/study/' URL to the study_mode view, naming it study_mode (Mapuje adres URL '/study/' na widok study_mode, nadając mu nazwę study_mode)
    path('toggle/<int:word_pk>/', toggle_learned, name='toggle_learned'),  # Maps '/toggle/<id>/' to toggle_learned view (Mapuje ścieżkę '/toggle/<id>/' na widok toggle_learned)
]