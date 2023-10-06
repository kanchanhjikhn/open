# chatapp/views.py
from django.shortcuts import render
from .forms import ChatForm
import openai

def ask_question(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = get_chatgpt3_response(question)

            # Save to the database
            chat_instance = Chat(question=question, answer=answer)
            chat_instance.save()

            return render(request, 'chatapp/success.html', {'question': question, 'answer': answer})
    else:
        form = ChatForm()

    return render(request, 'chatapp/ask_question.html', {'form': form})

def get_chatgpt3_response(question):
    # Use your OpenAI API key
    openai.api_key = 'your_api_key_here'

    # Make a request to ChatGPT-3
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=question,
        max_tokens=150,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
