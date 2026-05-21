from django.contrib import messages
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            messages.success(
                request,
                f'Thanks, {name}! We received your message and will reply soon.',
            )
            return redirect('contact')

        messages.error(request, 'Please fill in all fields before sending.')

    return render(request, 'contact.html')


def showcase(request):
    return render(request, 'showcase.html')
