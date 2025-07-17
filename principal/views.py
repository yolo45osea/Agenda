from datetime import date, datetime, time
from pyexpat.errors import messages
import time
from venv import logger
from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from principal.forms import CustomPasswordResetForm, RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from principal.models import Eventos
from django.contrib.auth.models import User
from user_agents import parse

# Create your views here.

#produccion
host =https://agenda-zuyf.onrender.com/
#desarrollo
#host = 'http://127.0.0.1:8000/'



def mail(request):

    subject = f'Tareas'
    from_email = 'ferremas69@gmail.com'
    
    #to = [correo for correo in correos]
    to = ['benj.romeroc@duocuc.cl']

    text_content = f'Hola, ya hiciste tus tareas?'
    html_content = f'''
    <p>Hola, ya hiciste tus tareas?.</p>
    <p>si no hiciste tus tareas, este es el momento de hacerlas.</p>
    <a href="{host}">click aqui</a>
    '''

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()




def get_user_info(request):
    # Obtener IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

    # Obtener User-Agent
    user_agent_str = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(user_agent_str)

    return {
        'ip': ip,
        'navegador': f"{user_agent.browser.family}",
        'sistema_operativo': f"{user_agent.os.family} {user_agent.os.version_string}",
        'dispositivo': (
            'Mobile' if user_agent.is_mobile else
            'Tablet' if user_agent.is_tablet else
            'PC' if user_agent.is_pc else
            'Otro'
        )
    }

def index(request):
    mensaje = None
    login_form=''
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('administrador')

    if request.method == "POST":

        # FORMULARIO LOGIN
        if 'login_form' in request.POST:
            post_data = request.POST.copy()
            username = post_data.get('username', '')
            username = username.replace(" ", "_")
            post_data['username'] =username
            login_form = AuthenticationForm(request, data=post_data)
            print(f"form: {login_form}")
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)

        elif 'registro_form' in request.POST:
            post_data = request.POST.copy()  # copiar para poder modificar
            username = post_data.get('username', '')
            username = username.replace(" ", "_")  # reemplaza espacios por guiones bajos
            post_data['username'] = username

            

            registro_form = RegistroForm(post_data)  # usa los datos modificados
            if registro_form.is_valid():
                user = registro_form.save()
                
                login(request, user)
                #git_commit("registro usuario")
                return redirect('index')
            else:
                logger.error(f"Error al registrar usuario. Errores del formulario: {registro_form.errors.as_json()}")
                mensaje = "Error al registrar el usuario."
    return render(request, "index.html", {'mensaje':mensaje, 'login_form':login_form})

@login_required
def administrador(request):
    return render(request, "administrador.html")

def alerta_accesos(request):
    return render(request, "alerta_accesos.html")

def jefe_maestranza(request):
    return render(request, "jefe_maestranza.html")

def mantenimiento_activo(request):
    return render(request, "mantenimiento_activo.html")

def operador(request):
    return render(request, "operador.html")

def nosotros(request):
    return render(request, "nosotros.html")

def contacto(request):
    return render(request, "contacto.html")

def servicio(request):
    return render(request, "servicio.html")

def mecanicos(request):
    return render(request, "mecanicos.html")

def registro_movimientos(request):
    return render(request, "registro_movimientos.html")


def calendario(request):
    usuario = request.user
    eventos_qs = Eventos.objects.filter(usuario=usuario)
    eventos = [model_to_dict(e, fields=['nombre', 'fecha', 'descripcion', 'tipo']) for e in eventos_qs]
    return render(request, "calendario.html", {'eventos':eventos})

def registro_evento(request):
    hoy = date.today().isoformat()
    usuario = request.user
    eventos = Eventos.objects.filter(usuario=usuario)
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')

        Eventos.objects.create(
            tipo = tipo,
            nombre = nombre,
            descripcion = descripcion,
            fecha = fecha,
            usuario = usuario
        )
        return redirect('registro_evento')
    return render(request, "registro_evento.html", {'eventos':eventos, 'hoy':hoy})

def organizador(request):
    return render(request, "organizador.html")


def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def sendmail(request):
    try:
        mail(request)
        return HttpResponse("Correo enviado correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al enviar correo: {str(e)}", status=500)
        
