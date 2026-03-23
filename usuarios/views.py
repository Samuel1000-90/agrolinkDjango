from django.shortcuts import render , redirect
from .models import Usuario,Cliente,Productor,Asesor,Administrador,Transportista

#  Esto Es Navegacion
def inicio_usuarios(request):
    return render(request,'usuarios/login.html')


def mostrar_registro_usuarios(request):
    return render(request,'usuarios/register.html')



    



# Esto Son Metodos 

def login(request):
    if request.method=='POST':
        cedula = request.POST.get("txt_documento")
        contrasena = request.POST.get("txt_clave")

        usuario = Usuario.objects.filter(cedula = cedula,contrasena = contrasena).first()

        if usuario is not None:
           return redirect('inicio.html')
        else: 
            return redirect('register.html')




def registrar_usuario(request):
    if request.method == 'POST':

        # 🔹 datos base
        nombre = request.POST.get("txt_nombre")
        apellido = request.POST.get("txt_apellido")
        documento = request.POST.get("txt_documento")  
        nombreUsuario = request.POST.get("txt_nombreUsuario")
        correo = request.POST.get("txt_correo")
        contrasena = request.POST.get("txt_contrasena")
        telefono = request.POST.get("txt_telefono")
        ciudad = request.POST.get("txt_ciudad")
        departamento = request.POST.get("txt_departamento")
        direccion = request.POST.get("txt_direccion")
        rol = request.POST.get("role")

        # 🔥 1. CREAR USUARIO (OBLIGATORIO)
        usuario = Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            nombre_usuario=nombreUsuario,
            telefono=telefono,
            departamento=departamento,
            ciudad=ciudad,
            correo=correo,
            contrasena_usuario=contrasena,
            direccion=direccion,
            cedula=documento,
            rol=rol
        )

        # 🔥 2. CREAR SEGÚN ROL
        if rol == "CLIENTE":
            Cliente.objects.create(
                id_usuario=usuario,
                preferencias=request.POST.get("txt_preferencias")
            )

        elif rol == "PRODUCTOR":
            Productor.objects.create(
                id_usuario=usuario,
                tipo_cultivo=request.POST.get("txt_tipoCultivo")
            )

        elif rol == "TRANSPORTISTA":
            Transportista.objects.create(
                id_usuario=usuario,
                zonas_entrega=request.POST.get("txt_zonasEntrega")
            )

        elif rol == "SERVICIO":
            Asesor.objects.create(
                id_usuario=usuario,
                tipo_asesoria=request.POST.get("txt_tipoAsesoria")
            )

    return redirect('mostrar_lista_persona')