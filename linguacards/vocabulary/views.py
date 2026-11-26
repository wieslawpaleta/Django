import random # Imports Python's built-in random module so we can pick random flashcards (Importuje wbudowany moduł random z Pythona, aby móc losować fiszki)
from django.db.models import Q 
from django.shortcuts import render, redirect, get_object_or_404  # Imports get_object_or_404 to fetch a database item or return an HTTP 404 error if it does not exist (Importuje get_object_or_404 do pobrania elementu bazy danych lub zwrócenia błędu HTTP 404, jeśli nie istnieje)
from .models import Word  # Imports our Word model (Importuje nasz model Word)
from .forms import WordForm  # Imports our WordForm class (Importuje naszą klasę WordForm)

def word_list(view_request):  # Defines the word list view function (Definiuje funkcję widoku listy słówek)
    search_query = view_request.GET.get('search', '').strip()  # Gets 'search' query param from URL, defaults to empty string, and removes leading/trailing spaces (Pobiera parametr 'search' z URL, domyślnie pusty tekst i usuwa spacje na początku/końcu)
    selected_language = view_request.GET.get('language', '').strip()  # Gets 'language' query param from URL, defaults to empty string (Pobiera parametr 'language' z URL, domyślnie pusty tekst)

    words_queryset = Word.objects.all()  # Starts with all Word records from the database (Zaczyna od wszystkich rekordów Word z bazy danych)

    if search_query:  # Checks if the user entered any search text (Sprawdza, czy użytkownik wpisał jakikolwiek tekst do wyszukania)
        words_queryset = words_queryset.filter(  # Filters the queryset to matching records (Filtruje zapytanie do pasujących rekordów)
            Q(foreign_word__icontains=search_query) | Q(translation__icontains=search_query)  # Matches if search_query appears case-insensitively in foreign_word OR translation (Pasuje, jeśli search_query występuje bez względu na wielkość liter w foreign_word LUB translation)
        )  # Closes filter call (Zamyka wywołanie filter)

    if selected_language:  # Checks if a specific language filter was selected (Sprawdza, czy wybrano konkretny filtr języka)
        words_queryset = words_queryset.filter(language__iexact=selected_language)  # Filters words where language matches selected_language ignoring case (Filtruje słówka, których język zgadza się z selected_language bez względu na wielkość liter)

    available_languages = (  # Prepares a sorted list of unique languages present in the database (Przygotowuje posortowaną listę unikalnych języków obecnych w bazie danych)
        Word.objects.order_by('language')  # Sorts records alphabetically by language column (Sortuje rekordy alfabetycznie po kolumnie language)
        .values_list('language', flat=True)  # Extracts only the 'language' column values as a flat list (Wyciąga tylko wartości kolumny 'language' jako płaską listę)
        .distinct()  # Removes duplicate language names (Usuwa powtarzające się nazwy języków)
    )  # Closes query chain (Zamyka łańcuch zapytania)

    context_dictionary = {  # Creates context dictionary to pass data to the HTML template (Tworzy słownik kontekstu do przekazania danych do szablonu HTML)
        'words': words_queryset,  # Filtered list of flashcards to display (Przefiltrowana lista fiszek do wyświetlenia)
        'languages': available_languages,  # Unique languages for the dropdown filter (Unikalne języki do listy rozwijanej filtra)
        'search_query': search_query,  # Keeps the searched text so it stays visible in the input box (Zachowuje wyszukany tekst, aby pozostał widoczny w polu wyszukiwania)
        'selected_language': selected_language,  # Keeps the chosen language so the dropdown remembers it (Zachowuje wybrany język, aby lista rozwijana go pamiętała)
    }  # Closes context dictionary (Zamyka słownik kontekstu)

    return render(view_request, 'vocabulary/word_list.html', context_dictionary)  # Renders word_list.html with context data (Renderuje word_list.html z danymi kontekstu)

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

def study_mode(view_request):  # Defines a new view function named study_mode for practicing flashcards (Definiuje nową funkcję widoku o nazwie study_mode do ćwiczenia fiszek)
    words_list = list(Word.objects.all())  # Converts the database QuerySet into a Python list so random.choice() can pick from it (Konwertuje QuerySet z bazy danych na zwykłą listę Pythona, aby random.choice() mogło z niej losować)
    random_word = random.choice(words_list) if words_list else None  # Picks one random word if the list is not empty, otherwise sets None (Losuje jedno słowo, jeśli lista nie jest pusta, w przeciwnym razie ustawia None)
    context_dictionary = {'word': random_word}  # Packs the selected random word into the context dictionary (Pakuje wylosowane słowo do słownika kontekstu)
    return render(view_request, 'vocabulary/study_mode.html', context_dictionary)  # Renders the study_mode HTML template and returns the response (Renderuje szablon HTML study_mode i zwraca odpowiedź)