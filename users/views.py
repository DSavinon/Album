from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get("username")
            messages.success(
                request, f'Bienvenido {usuario}, tu cuenta ha sido registrada'
            )
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/registrarse.html', context)
