# main/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import  logout
from .models import Post,Comentarios,CustomUserSB
from .forms import RegisterForm, SubscriberForm,PostSearchForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditProfileForm

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

def register(request):
    form = RegisterForm()
    message = ""

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = CustomUserSB()
                user.username = form.cleaned_data["username"]
                user.email = form.cleaned_data["email"]
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                user.set_password(form.cleaned_data["password1"])

                if not form.cleaned_data["address"]:
                    user.direccion = None
                else:
                    user.direccion = form.cleaned_data["address"]

                user.pais = form.cleaned_data["country"]
                user.codigo_postal = form.cleaned_data["cp"]
                user.ciudad = form.cleaned_data["city"]
                user.genero = form.cleaned_data["genre"]

                user.profile_image = form.cleaned_data["profile_image"]
                user.about_me = form.cleaned_data["about_me"]

                """ if not form.cleaned_data["accept_politics"]:
                    user.accept_politics = False
                else:
                    user.accept_politics = True """

                user.is_active = True
                user.save()

                form = RegisterForm()
                messages.success(
                    request, "La operación se ha realizado con éxito.")

                # Redirige a la vista de inicio de sesión
                return redirect("login")

            except IntegrityError as e:
                message = "Error, username or email already exists"
            except Exception as e:
                message = str(e)
        else:
            message = "Error, formulario no válido"

    context = {
        "form": form,
        "message": message
    }

    return render(request, "registration/register.html", context=context)

@login_required
def subscribe(request):
    form = SubscriberForm()
    message = ""
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            try:
                user = request.user
                if user.suscripcion == True:
                    message = "La cuenta ya está suscrita"
                else:
                    user.tarjeta_de_credito = form.cleaned_data["tarjeta_de_credito"]
                    user.dni = form.cleaned_data["dni"]

                    user.suscripcion = True
                    user.save()

                    form = SubscriberForm() 
                    messages.success(
                        request, "La operación se ha realizado con éxito.")

                    return redirect('index')

            except IntegrityError as e:
                message = "Error, username or email already exists"
            except Exception as e:
                message = str(e)
        else:
            message = "Error, formulario no válido"

    context = {
        "form": form,
        "message": message
    }

    return render(request, "registration/subscribe.html", context=context)

def index(request):
    premium_posts = Post.objects.filter(suscripcion=True)[:4]  # Obtener los primeros 4 posts premium
    non_premium_posts = Post.objects.filter(suscripcion=False)[:4]  # Obtener los primeros 4 posts no premium
    
    context = {
        'premium_posts': premium_posts,
        'non_premium_posts': non_premium_posts
    }  # Concatenar las dos listas de posts
    
    return render(request, 'index.html', context=context)

def about_us(request):
    return render(request, 'about_us.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

""" def listar_publicaciones(request):
    user = request.user
    if user.suscripcion:
        publicaciones = Post.objects.all()
    else:
        publicaciones=Post.objects.filter(suscripcion= False)
    
    return render(request, 'listar_publicaciones.html', {'publicaciones': publicaciones}) """

@login_required
def ver_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Post, pk=publicacion_id)
    comentarios = Comentarios.objects.filter(Publicacion=publicacion)
    if not request.user.suscripcion:
            return redirect('subscribe')
    
    return render(request, 'ver_publicacion.html', {'publicacion': publicacion, 'comentarios': comentarios})

@login_required
def agregar_comentario(request, publicacion_id):
    if request.method == 'POST':
        texto = request.POST['texto']
        publicacion = get_object_or_404(Post, pk=publicacion_id)  # Verifica si la publicación existe
        usuario = request.user
        comentario = Comentarios(Publicacion=publicacion, usuario=usuario, texto=texto)  # Asegúrate de que los nombres de los campos sean correctos
        comentario.save()
    return redirect('ver_publicacion', publicacion_id=publicacion_id)

@login_required
def post_search(request):
    if request.method == 'GET':
        form = PostSearchForm(request.GET)
        if form.is_valid():  # Check if the form is valid before accessing cleaned_data
            query = form.cleaned_data.get('query')
            # Apply filtering based on user input (query) and other criteria
            if query:
                posts = Post.objects.filter(titulo__icontains=query)
            else:
                posts = Post.objects.all()
        else:
            # Handle the case when the form is not valid
            posts = Post.objects.all()  # You can provide a default queryset here
    else:
        form = PostSearchForm()
        user = request.user

        if user.suscripcion:
            posts = Post.objects.all()
        else:
            posts=Post.objects.filter(suscripcion= False)

        

    return render(request, 'posts.html', {'form': form, 'posts': posts})

def politics(request):
    return render(request, 'politica_privacidad.html')




