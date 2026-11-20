from django.shortcuts import render, redirect, get_object_or_404  # Imports get_object_or_404 to fetch a database item or return an HTTP 404 error if it does not exist (Importuje get_object_or_404 do pobrania elementu bazy danych lub zwrócenia błędu HTTP 404, jeśli nie istnieje)
from .models import Word  # Imports our Word model (Importuje nasz model Word)
from .forms import WordForm  # Imports our WordForm class (Importuje naszą klasę WordForm)

def word_list(view_request):  # Defines the list view function (Definiuje funkcję widoku listy)
    all_words = Word.objects.all()  # Fetches all words from database (Pobiera wszystkie słówka z bazy danych)
    context_dictionary = {'words': all_words}  # Packs words into context dictionary (Pakuje słówka do słownika kontekstu)
    return render(view_request, 'vocabulary/word_list.html', context_dictionary)  # Renders word list template (Renderuje szablon listy słówek)

def add_word(view_request):  # Defines the add word view function (Definiuje funkcję widoku dodawania słówka)
    if view_request.method == 'POST':  # Checks if form was submitted (Sprawdza, czy formularz został przesłany)
        form = WordForm(view_request.POST)  # Creates form with posted data (Tworzy formularz z przesłanymi danymi)
        if form.is_valid():  # Checks if data is valid (Sprawdza, czy dane są poprawne)
            form.save()  # Saves new word to database (Zapisuje nowe słowo do bazy danych)
            return redirect('word_list')  # Redirects to list page (Przekierowuje do strony listy)
    else:
        form = WordForm()  # Creates empty form (Tworzy pusty formularz)
    
    context_dictionary = {'form': form}  # Packs form into context (Pakuje formularz do kontekstu)
    return render(view_request, 'vocabulary/word_form.html', context_dictionary)  # Renders form template (Renderuje szablon formularza)

def update_word(view_request, word_pk):  # Defines a view function to edit a word, taking its unique ID (pk) as an argument (Definiuje funkcję widoku do edycji słówka, przyjmując jego unikalne ID (pk) jako argument)
    word_item = get_object_or_404(Word, pk=word_pk)  # Fetches the specific word by primary key or shows 404 error page if missing (Pobiera konkretne słowo po kluczu głównym lub pokazuje stronę błędu 404, jeśli go brakuje)
    if view_request.method == 'POST':  # Checks if the user submitted updated data (Sprawdza, czy użytkownik przesłał zaktualizowane dane)
        form = WordForm(view_request.POST, instance=word_item)  # Creates form with submitted data attached to the existing word instance (Tworzy formularz z przesłanymi danymi przypisanymi do istniejącej instancji słówka)
        if form.is_valid():  # Checks if the updated data is valid (Sprawdza, czy zaktualizowane dane są poprawne)
            form.save()  # Overwrites and saves changes to the database record (Nadpisuje i zapisuje zmiany w rekordu bazy danych)
            return redirect('word_list')  # Redirects back to the main word list page (Przekierowuje z powrotem do głównej strony listy słówek)
    else:
        form = WordForm(instance=word_item)  # Creates form pre-filled with the existing word's data for editing (Tworzy formularz wstępnie wypełniony danymi istniejącego słówka do edycji)
    
    context_dictionary = {'form': form, 'word': word_item}  # Packs form and word item into context dictionary (Pakuje formularz i element słówka do słownika kontekstu)
    return render(view_request, 'vocabulary/word_form.html', context_dictionary)  # Renders the shared form template (Renderuje współdzielony szablon formularza)

def delete_word(view_request, word_pk):  # Defines a view function to delete a word using its primary key (Definiuje funkcję widoku do usuwania słówka za pomocą jego klucza głównego)
    word_item = get_object_or_404(Word, pk=word_pk)  # Fetches the word or returns 404 error (Pobiera słówko lub zwraca błąd 404)
    if view_request.method == 'POST':  # Checks if the user confirmed deletion by submitting the confirmation form (Sprawdza, czy użytkownik potwierdził usunięcie, wysyłając formularz potwierdzenia)
        word_item.delete()  # Deletes this specific record from the database table (Usuwa ten konkretny rekord z tabeli bazy danych)
        return redirect('word_list')  # Redirects back to the word list page (Przekierowuje z powrotem do strony listy słówek)
    
    context_dictionary = {'word': word_item}  # Packs word item into context for confirmation display (Pakuje element słówka do kontekstu w celu wyświetlenia potwierdzenia)
    return render(view_request, 'vocabulary/word_confirm_delete.html', context_dictionary)  # Renders the delete confirmation HTML template (Renderuje szablon HTML potwierdzenia usunięcia)