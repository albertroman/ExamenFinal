from django.shortcuts import render
from .forms import ingresarlibro

def IngresarLibro(request):
    if request.method == "POST":
        form = ingresarlibro(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/ingresarPrestamo.html', {'form': form})
    else:
        form=ingresarlibro()
    return render(request, 'blog/ingresarPrestamo.html', {'form': form})
