from django.db import models
from django.contrib.auth.models import User

# Model representing a math question [Model reprezentujący pytanie matematyczne]
class MathQuestion(models.Model):
    # Question text displayed to the user [Tekst pytania wyświetlany użytkownikowi]
    question_text = models.CharField(max_length=255)
    
    # Correct numerical answer [Prawidłowa odpowiedź numeryczna]
    answer = models.FloatField()
    
    # Difficulty level [Poziom trudności]
    difficulty = models.CharField(
        max_length=10, 
        choices=[('Easy', 'Easy [Łatwy]'), ('Hard', 'Hard [Trudny]')]
    )

    def __str__(self):
        return self.question_text

# Model to track user quiz scores [Model do śledzenia wyników quizu użytkownika]
class UserScore(models.Model):
    # Link to the Django user model [Powiązanie z modelem użytkownika Django]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Final score achieved [Osiągnięty wynik końcowy]
    score = models.IntegerField()
    
    # Timestamp when the quiz was completed [Data i czas ukończenia quizu]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score} points [punkty]"