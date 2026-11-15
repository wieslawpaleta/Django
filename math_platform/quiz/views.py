from django.shortcuts import render, redirect
from .models import MathQuestion, UserScore
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# View handling the math quiz page [Widok obsługujący stronę quizu matematycznego]
def quiz_view(request):
    # Fetch all questions from the database [Pobierz wszystkie pytania z bazy danych]
    questions = MathQuestion.objects.all()

    if request.method == 'POST':
        score = 0

        # Loop through questions to check user answers [Pętla po pytaniach w celu sprawdzenia odpowiedzi użytkownika]
        for q in questions:
            user_answer = request.POST.get(f'question_{q.id}')
            if user_answer and float(user_answer) == q.answer:
                score += 1

        # Save score if the user is logged in [Zapisz wynik, jeśli użytkownik jest zalogowany]
        if request.user.is_authenticated:
            UserScore.objects.create(user=request.user, score=score)

        # Render the result template with the final score [Wyrenderuj szablon wyniku z ostatecznym wynikiem]
        return render(request, 'quiz/result.html', {'score': score})

    # Render the quiz page with questions [Wyrenderuj stronę quizu z pytaniami]
    return render(request, 'quiz/quiz.html', {'questions': questions})

# User registration view [Widok rejestracji użytkownika]
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Save the new user to database [Zapisz nowego użytkownika w bazie danych]
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in. [Konto utworzone dla {username}! Możesz się teraz zalogować.]')
            return redirect('login') # Redirect to login page after success [Przekieruj do strony logowania po sukcesie]
    else:
        form = UserCreationForm()
    
    return render(request, 'quiz/register.html', {'form': form})