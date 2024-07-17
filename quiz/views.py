import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Question
from .forms import EmailForm

logger = logging.getLogger(__name__)

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz/question_list.html', {'questions': questions})

def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    return render(request, 'quiz/question_detail.html', {'question': question})

def take_quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_option = request.POST.get(str(question.id))
            if selected_option == question.correct_answer:
                score += 1
        request.session['score'] = score
        request.session['total'] = questions.count()
        return redirect('quiz_result')
    return render(request, 'quiz/take_quiz.html', {'questions': questions})



from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import EmailForm
import logging

logger = logging.getLogger(__name__)

def quiz_result(request):
    score = request.session.get('score')
    total = request.session.get('total')
    answers = request.session.get('answers', [])  # Foydalanuvchining javoblarini olamiz

    if score is None or total is None or answers is None:
        return redirect('take_quiz')

    email_sent = False
    passed = score > 2

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            subject = 'Quiz Results'
            if passed:
                message = f'Congratulations {user_name}! You passed the quiz with a score of {score} out of {total}.'
            else:
                message = f'{user_name}, you scored {score} out of {total}. Keep trying to improve your score!'

            message += f'\nUser answers: {answers}'

            to_email = 'orallxannajmatdinova@gmail.com'
            email = EmailMessage(
                subject,
                message,
                'your_email@example.com',  # Sizning email manzilingiz
                [to_email]
            )
            try:
                email.send(fail_silently=False)
                logger.info(f"Email sent from your_email@example.com to {to_email}")
                email_sent = True
            except Exception as e:
                logger.error(f"Error sending email: {e}")
        else:
            logger.debug("Form is not valid")
    else:
        form = EmailForm()

    return render(request, 'quiz/quiz_result.html', {
        'form': form,
        'score': score,
        'total': total,
        'email_sent': email_sent,
        'passed': passed
    })
