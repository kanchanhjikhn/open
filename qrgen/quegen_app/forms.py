from django import forms
import openai

class OpenAIForm(forms.Form):
    text_data = forms.CharField(label='Enter your question')

    def generate_openai_response(self):
        # Get user input from the form
        user_question = self.cleaned_data['text_data']

        # Set your OpenAI API key here
        openai.api_key = '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'

        # Call the OpenAI API to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",  # You might want to check for the latest engine
            prompt=user_question,
            max_tokens=150  # Adjust as needed
        )

        # Extract the generated answer
        generated_answer = response.choices[0].text.strip()

        return generated_answer
