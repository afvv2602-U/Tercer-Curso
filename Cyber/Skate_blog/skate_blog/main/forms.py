from django import forms
from .models import Comentarios,CustomUserSB
from django.utils.safestring import SafeText
import re

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('texto',) 

class SubscriberForm(forms.Form):
    tarjeta_de_credito = forms.CharField(label=SafeText('<i class="fas fa-user"></i> Tarjeta de crédito * '), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tarjeta de crédito', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    dni = forms.CharField(label=SafeText('<i class="fas fa-user"></i> DNI * '), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'DNI', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

class RegisterForm(forms.Form):

    username = forms.CharField(label=SafeText('<i class="fas fa-user"></i> Nombre de usuario * '), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    email = forms.EmailField(label=SafeText('<i class="fas fa-envelope"></i> Correo electrónico * '), widget=forms.EmailInput(attrs={
                                'class': 'form-control', 'placeholder': 'Correo electrónico', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    first_name = forms.CharField(label=SafeText('<i class="fas fa-user"></i> Nombre * '), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    last_name = forms.CharField(label=SafeText('<i class="fas fa-user"></i> Apellido * '), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Apellido', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    password1 = forms.CharField(
        label=SafeText('<i class="fas fa-lock"></i> Contraseña * '),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'required': 'required'}),
        error_messages={'required': 'El campo es obligatorio'})

    password2 = forms.CharField(label=SafeText('<i class="fas fa-lock"></i> Confirmar contraseña * '), widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    address = forms.CharField(label=SafeText('<i class="fas fa-home"></i> Dirección'), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Dirección'}), required=False)

    city = forms.CharField(label=SafeText('<i class="fas fa-map-marker-alt"></i> Ciudad * '), widget=forms.TextInput(attrs={
                           'class': 'form-control', 'placeholder': 'Ciudad', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    cp = forms.CharField(label=SafeText('<i class="fas fa-map-marker-alt"></i> Código postal * '), widget=forms.TextInput(attrs={
                            'class': 'form-control', 'placeholder': 'Código postal', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})
    
    country = forms.CharField(label=SafeText('<i class="fas fa-map-marker-alt"></i> País * '), widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'País', 'required': 'required'}), error_messages={'required': 'El campo es obligatorio'})

    GENDER_CHOICES = [
        ('male', 'Masculino'),
        ('female', 'Femenino'),
        ('other', 'Otro'),
    ]
    
    genre = forms.ChoiceField(
        label=SafeText('<i class="fas fa-venus-mars"></i> Género * '),
        choices=GENDER_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control', 'required': 'required'}),
        error_messages={'required': 'El campo es obligatorio'}
    )

    profile_image = forms.ImageField(
        label=SafeText('<i class="fas fa-camera"></i> Foto de perfil'),
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )

    about_me = forms.CharField(
        label=SafeText('<i class="fas fa-info"></i> Acerca de mí'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuéntanos algo sobre ti'}),
        required=False
    )

    accept_politics = forms.BooleanField(
        label=SafeText('<i class="fas fa-check"></i> Acepto la política de privacidad "'), 
        widget=forms.CheckboxInput(attrs={'required': 'required', 'class': 'custom-checkbox'}),
        error_messages={'required': 'El campo es obligatorio'}
    ) 
    

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')

        # Comprueba que la contraseña tiene al menos un carácter especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError('La contraseña debe tener al menos un carácter especial.')

        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Si necesitas una validación adicional para el correo, puedes agregarla aquí.
        # Por defecto, Django ya verifica que sea un correo válido.
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
      
class PostSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUserSB
        fields = [
            'username', 'genero', 'direccion', 'ciudad', 'codigo_postal',
            'pais', 'profile_image', 'about_me'
        ]

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

    # Exclude email and password fields from the form
    def clean_email(self):
        return self.instance.email

    def clean_password(self):
        return self.instance.password