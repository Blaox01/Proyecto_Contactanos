from django.shortcuts import render
from .forms import ContactForm

# def index(request):
#    return render(request,'Test_02.html')

#def contacto(request):
 #   if request.method == 'POST':
  #      form = ContactForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       mensaje_exito = "Su contacto fue guardado, nos comunicaremos pronto!"
   # else:
    #    form = ContactForm()
   # return render(request, 'Test_02.html', {'form': form})

def contacto(request):
    mensaje_exito = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje_exito = '¡Datos guardados correctamente!'
            return render(request, 'Test_02.html', {'form': ContactForm(), 'mensaje_exito': mensaje_exito})
    else:
        form = ContactForm()

    return render(request, 'Test_02.html', {'form': form, 'mensaje_exito': mensaje_exito})