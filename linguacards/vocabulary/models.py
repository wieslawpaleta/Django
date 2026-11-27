from django.db import models  # Imports Django's database module so we can use built-in field types to build database tables (Importuje moduł bazy danych Django, abyśmy mogli używać wbudowanych typów pól do budowy tabel w bazie danych)

class Word(models.Model):  # Defines a new database table class named Word that inherits from Django's Model class (Definiuje nową klasę tabeli bazy danych o nazwie Word, która dziedziczy po klasie Model z Django)
    foreign_word = models.CharField(max_length=100)  # Creates a text column for the foreign word, allowing up to 100 characters (Tworzy kolumnę tekstową na obce słowo, pozwalającą na maksymalnie 100 znaków)
    translation = models.CharField(max_length=100)  # Creates a text column for the native translation, allowing up to 100 characters (Tworzy kolumnę tekstową na tłumaczenie ojczyste, pozwalającą na maksymalnie 100 znaków)
    language = models.CharField(max_length=50)  # Creates a text column for the language name (e.g., Spanish, German), up to 50 characters (Tworzy kolumnę tekstową na nazwę języka np. hiszpański, niemiecki, do 50 znaków)
    is_learned = models.BooleanField(default=False) # Stores whether the word is learned (True/False), defaulting to False for new words (Przechowuje informację, czy słowo jest nauczone True/False, domyślnie False dla nowych słów)
    created_at = models.DateTimeField(auto_now_add=True)  # Creates a date/time column that automatically records when the word was created (Tworzy kolumnę daty/czasu, która automatycznie zapisuje moment utworzenia słówka)

    def __str__(self):  # Defines a special Python method to determine how a single Word object is displayed as text (Definiuje specjalną metodę Pythona określającą, jak pojedynczy obiekt Word jest wyświetlany jako tekst)
        return f"{self.foreign_word} - {self.translation}"  # Returns a neat combined string of the foreign word and its translation (Zwraca ładny, połączony tekst obcego słowa i jego tłumaczenia)