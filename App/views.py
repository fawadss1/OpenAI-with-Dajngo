from django.shortcuts import render
import pyttsx3
import openai


def generate_text(request):
    context = {}
    if request.method == "POST":
        query = request.POST.get("query")
        openai.api_key = "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"
        completions = openai.Completion.create(engine="text-davinci-002", prompt=query, max_tokens=1024, n=1,
                                               stop=None, temperature=0.5)
        message = completions.choices[0].text
        context = {'message': message.strip()}
    return render(request, 'index.html', context)
