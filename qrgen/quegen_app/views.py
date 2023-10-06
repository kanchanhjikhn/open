from django.shortcuts import render
from .forms import OpenAIForm

def openai_view(request):
    if request.method == 'POST':
        form = OpenAIForm(request.POST)
        if form.is_valid():
            # Generate OpenAI response
            generated_answer = form.generate_openai_response()

            return render(request, 'result.html', {'form': form, 'generated_answer': generated_answer})

    else:
        form = OpenAIForm()

    return render(request, 'generate.html', {'form': form})