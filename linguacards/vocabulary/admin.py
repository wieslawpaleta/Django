from django.contrib import admin # Imports Django's built-in admin module to manage admin panel settings (Importuje wbudowany moduł admina Django do zarządzania ustawieniami panelu administracyjnego)
from .models import Word # Imports our Word model from the current app's models.py file (Importuje nasz model Word z pliku models.py bieżącej aplikacji)

# Register your models here.
admin.site.register(Word) # Registers the Word model so it becomes visible and manageable inside the Django admin interface (Rejestruje model Word, dzięki czemu staje się widoczny i zarządzalny w interfejsie administratora Django)
