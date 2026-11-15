from django import forms  # Imports Django's forms module to build web forms (Importuje moduł formularzy Django do budowy formularzy internetowych)
from .models import Word  # Imports our Word model so the form knows which database table fields to use (Importuje nasz model Word, aby formularz wiedział, których pól tabeli bazy danych użyć)

class WordForm(forms.ModelForm):  # Defines a new form class named WordForm that inherits from Django's ModelForm (Definiuje nową klasę formularza o nazwie WordForm, która dziedziczy po klasie ModelForm z Django)
    class Meta:  # Inner Meta class used to provide configuration metadata to the ModelForm (Wewnętrzna klasa Meta służąca do dostarczenia metadanych konfiguracyjnych dla ModelForm)
        model = Word  # Specifies that this form is tied to the Word database model (Określa, że ten formularz jest powiązany z modelem bazy danych Word)
        fields = ['foreign_word', 'translation', 'language']  # Lists the model fields we want to show and edit in the HTML form (Wymienia pola modelu, które chcemy pokazać i edytować w formularzu HTML)