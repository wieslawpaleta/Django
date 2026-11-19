from django.shortcuts import render, redirect, get_object_or_404  # Imports render for templates and redirect to send users to another page after saving (Importuje render do szablonów oraz redirect do wysyłania użytkowników na inną stronę po zapisaniu)
from .models import Word  # Imports the Word model (Importuje model Word)
from .forms import WordForm  # Imports our newly created WordForm class (Importuje naszą nowo utworzoną klasę WordForm)

def word_list(view_request):  # Defines the existing word list view function (Definiuje istniejącą funkcję widoku listy słówek)
    all_words = Word.objects.all()  # Queries database for all words (Odpytuje bazę danych o wszystkie słówka)
    context_dictionary = {'words': all_words}  # Packs words into context dictionary (Pakuje słówka do słownika kontekstu)
    return render(view_request, 'vocabulary/word_list.html', context_dictionary)  # Renders the word list template (Renderuje szablon listy słówek)

def add_word(view_request):  # Defines a new view function named add_word to handle creating a new flashcard (Definiuje nową funkcję widoku o nazwie add_word do obsługi tworzenia nowej fiszki)
    if view_request.method == 'POST':  # Checks if the browser sent data via HTTP POST (user submitted the form) (Sprawdza, czy przeglądarka wysłała dane metodą HTTP POST - użytkownik przesłał formularz)
        form = WordForm(view_request.POST)  # Creates a form instance filled with the data submitted by the user (Tworzy instancję formularza wypełnioną danymi przesłanymi przez użytkownika)
        if form.is_valid():  # Checks if all submitted data passes validation checks (Sprawdza, czy wszystkie przesłane dane przechodzą testy walidacji)
            form.save()  # Saves the new word directly into the database table (Zapisuje nowe słowo bezpośrednio w tabeli bazy danych)
            return redirect('word_list')  # Redirects the user back to the main word list page (Przekierowuje użytkownika z powrotem do głównej strony listy słówek)
    else:  # Executes if the request method is GET (the user just opened the empty form page) (Wykonuje się, jeśli metodą żądania jest GET - użytkownik właśnie otworzył stronę pustego formularza)
        form = WordForm()  # Creates a blank, empty form instance (Tworzy czystą, pustą instancję formularza)
    
    context_dictionary = {'form': form}  # Packs the form into a context dictionary (Pakuje formularz do słownika kontekstu)
    return render(view_request, 'vocabulary/word_form.html', context_dictionary)  # Renders the HTML template containing the form and returns it (Renderuje szablon HTML zawierający formularz i go zwraca)

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