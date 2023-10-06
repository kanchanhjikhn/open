# chatapp/views.py
from django.shortcuts import render
from .forms import ChatForm
from .models import Topic
import openai


def ask_question(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = get_chatgpt3_response(question)

            # Save to the database
            chat_instance = Topic(question=question, answer=answer)
            chat_instance.save()

            return render(request, 'success.html', {'question': question, 'answer': answer})
    else:
        form = ChatForm()

    return render(request, 'ask_question.html', {'form': form})
def ask_topic(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = get_chatgpt3_response(question)

            # Save to the database
            chat_instance = Topic(question=question, answer=answer)
            chat_instance.save()

            return render(request, 'successtopic.html', {'question': question, 'answer': answer})
    else:
        form = ChatForm()

    return render(request, 'ask_topic.html', {'form': form})


def get_chatgpt3_response(input_text):
    # Your implementation here
    openai.api_key = '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'

    # Make a request to ChatGPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=2000,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
