from django.shortcuts import render ,redirect
from django.http import HttpResponse
from  .models import ToDoList , Item 
from  django.contrib.auth.forms import UserCreationForm
#to provide some msgs 
from django.contrib import messages 
#defien two views for the register and the login  
from .forms import CreateUserForm
from  django.contrib.auth import authenticate , logout ,login as logs
from  django.contrib.auth.decorators import login_required
import openai
from openai.api_resources import Completion
import os
from dotenv import load_dotenv

load_dotenv()
#get the key 

OPENAI_KEY ="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"

openai.api_key = OPENAI_KEY



@login_required(login_url='main/login.html')
def chatbot(request):
    if request.method == 'POST':
        # get the message from the user
        message = request.POST.get('message')

        # get the conversation history from the session, or create a new one
        history = request.session.get('history', [])

        # add the user's message to the conversation history
        history.append({'user': message})

        # call OpenAI's GPT-3 to generate a response
        response = Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )

        # get the generated response from OpenAI's API
        bot_message = response.choices[0].text.strip()

        # add the bot's response to the conversation history
        history.append({'bot': bot_message})

        # save the conversation history in the session
        request.session['history'] = history

        # render the chatbot template with the user's message, the bot's response, and the conversation history
        return render(request, 'main/home.html', {'user_message': message, 'bot_message': bot_message, 'history': history})

    else:
        # clear the conversation history from the session
        request.session.pop('history', None)

        return render(request, 'main/home.html')




def register(request):
    if request.method == 'POST':

        if request.POST.get('Register') == 'true':
            # Button is clicked
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user_name = request.POST.get('username')
                # add success message to the session
                # redirect to the login page
                return render(request, 'main/succeful.html')
    else:
        form = CreateUserForm()
    return render(request, 'main/register.html', {'form': form})



#restricted
@login_required(login_url='main/login.html')
def check ( request): 
    return render(request , 'main/succeful.html')


def login(request):
    if request.method == 'POST':
        if request.POST.get('login') == 'true':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logs(request, user)
                return render(request, 'main/succeful.html')
             
    
    return render(request , 'main/login.html')


def logout_page(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            logout(request)
            return redirect('http://127.0.0.1:8000/login',request=request)
    return render(request, 'main/register.html')


@login_required(login_url='main/login.html')
def home(request): 
    return render(request, 'main/home.html')



