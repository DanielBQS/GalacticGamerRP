// validation-realtime.js

// Expresiones regulares y campos
const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,60}$/, // Letras y espacios, pueden llevar acentos.
    correo: /^[a-zA-Z0-9_.+-]+@gmail\.com$/, // Correo que termine en @gmail.com
    usuario: /^[a-zA-Z0-9\_\-]{4,20}$/, // Letras, números, guion y guion_bajo
    password: /^.{4,20}$/, // 4 a 20 dígitos.
    direccion: /^[a-zA-Z0-9\s\-\#\/\.]{1,100}$/ // Letras, números, espacios, guiones, almohadillas, barras y puntos
};

const campos = {
    Nombre: false,
    correo: false,
    Usuario: false,
    password: false,
    direccion: false
};

// Función para validar el campo "nombre" en tiempo real
function validarNombreRealTime() {
    const inputNombre = document.getElementById('nombre');

    if (expresiones.nombre.test(inputNombre.value)) {
        document.getElementById('grupo__Nombre').classList.remove("formulario__grupo-incorrecto");
        document.getElementById('grupo__Nombre').classList.add("formulario__grupo-correcto");
        document.querySelector('#grupo__Nombre i').classList.add("fa-check-circle");
        document.querySelector('#grupo__Nombre i').classList.remove("fa-times-circle");
        document.querySelector('#grupo__Nombre .formulario__input-error').classList.remove("formulario__input-error-activo");
        campos.Nombre = true;
    } else {
        document.getElementById('grupo__Nombre').classList.add("formulario__grupo-incorrecto");
        document.getElementById('grupo__Nombre').classList.remove("formulario__grupo-correcto");
        document.querySelector('#grupo__Nombre i').classList.add("fa-times-circle");
        document.querySelector('#grupo__Nombre i').classList.remove("fa-check-circle");
        document.querySelector('#grupo__Nombre .formulario__input-error').classList.add("formulario__input-error-activo");
        campos.Nombre = false;
    }
}
// Validación de la fecha de nacimiento (mínimo 10 años antes)
const inputFechaNacimiento = document.getElementById('fecha_nacimiento');

inputFechaNacimiento.addEventListener('blur', () => {
    const fechaNacimiento = new Date(inputFechaNacimiento.value);
    const fechaActual = new Date();
    fechaActual.setFullYear(fechaActual.getFullYear() - 10); // Restar 10 años a la fecha actual

    if (fechaNacimiento > fechaActual) {
        document.getElementById('grupo__FechaNacimiento').classList.add('formulario__grupo-incorrecto');
        document.getElementById('grupo__FechaNacimiento').classList.remove('formulario__grupo-correcto');
        document.querySelector('#grupo__FechaNacimiento i').classList.add('fa-times-circle');
        document.querySelector('#grupo__FechaNacimiento i').classList.remove('fa-check-circle');
        document.querySelector('#grupo__FechaNacimiento .formulario__input-error').classList.add('formulario__input-error-activo');
        campos.FechaNacimiento = false;
    } else {
        document.getElementById('grupo__FechaNacimiento').classList.remove('formulario__grupo-incorrecto');
        document.getElementById('grupo__FechaNacimiento').classList.add('formulario__grupo-correcto');
        document.querySelector('#grupo__FechaNacimiento i').classList.add('fa-check-circle');
        document.querySelector('#grupo__FechaNacimiento i').classList.remove('fa-times-circle');
        document.querySelector('#grupo__FechaNacimiento .formulario__input-error').classList.remove('formulario__input-error-activo');
        campos.FechaNacimiento = true;
    }
});
// Función para validar el campo "correo" en tiempo real
function validarCorreoRealTime() {
    const inputCorreo = document.getElementById('correo');

    if (expresiones.correo.test(inputCorreo.value)) {
        document.getElementById('grupo__Correo').classList.remove("formulario__grupo-incorrecto");
        document.getElementById('grupo__Correo').classList.add("formulario__grupo-correcto");
        document.querySelector('#grupo__Correo i').classList.add("fa-check-circle");
        document.querySelector('#grupo__Correo i').classList.remove("fa-times-circle");
        document.querySelector('#grupo__Correo .formulario__input-error').classList.remove("formulario__input-error-activo");
        campos.correo = true;
    } else {
        document.getElementById('grupo__Correo').classList.add("formulario__grupo-incorrecto");
        document.getElementById('grupo__Correo').classList.remove("formulario__grupo-correcto");
        document.querySelector('#grupo__Correo i').classList.add("fa-times-circle");
        document.querySelector('#grupo__Correo i').classList.remove("fa-check-circle");
        document.querySelector('#grupo__Correo .formulario__input-error').classList.add("formulario__input-error-activo");
        campos.correo = false;
    }
}
// Función para validar el campo "dirección" en tiempo real
function validarDireccionRealTime() {
    const inputDireccion = document.getElementById('direccion');

    if (expresiones.direccion.test(inputDireccion.value)) {
        document.getElementById('grupo__Direccion').classList.remove("formulario__grupo-incorrecto");
        document.getElementById('grupo__Direccion').classList.add("formulario__grupo-correcto");
        document.querySelector('#grupo__Direccion i').classList.add("fa-check-circle");
        document.querySelector('#grupo__Direccion i').classList.remove("fa-times-circle");
        document.querySelector('#grupo__Direccion .formulario__input-error').classList.remove("formulario__input-error-activo");
        campos.direccion = true;
    } else {
        document.getElementById('grupo__Direccion').classList.add("formulario__grupo-incorrecto");
        document.getElementById('grupo__Direccion').classList.remove("formulario__grupo-correcto");
        document.querySelector('#grupo__Direccion i').classList.add("fa-times-circle");
        document.querySelector('#grupo__Direccion i').classList.remove("fa-check-circle");
        document.querySelector('#grupo__Direccion .formulario__input-error').classList.add("formulario__input-error-activo");
        campos.direccion = false;
    }
}
// Función para validar el campo "usuario" en tiempo real
function validarUsuarioRealTime() {
    const inputUsuario = document.getElementById('usuario');

    if (expresiones.usuario.test(inputUsuario.value)) {
        document.getElementById('grupo__Usuario').classList.remove("formulario__grupo-incorrecto");
        document.getElementById('grupo__Usuario').classList.add("formulario__grupo-correcto");
        document.querySelector('#grupo__Usuario i').classList.add("fa-check-circle");
        document.querySelector('#grupo__Usuario i').classList.remove("fa-times-circle");
        document.querySelector('#grupo__Usuario .formulario__input-error').classList.remove("formulario__input-error-activo");
        campos.Usuario = true;
    } else {
        document.getElementById('grupo__Usuario').classList.add("formulario__grupo-incorrecto");
        document.getElementById('grupo__Usuario').classList.remove("formulario__grupo-correcto");
        document.querySelector('#grupo__Usuario i').classList.add("fa-times-circle");
        document.querySelector('#grupo__Usuario i').classList.remove("fa-check-circle");
        document.querySelector('#grupo__Usuario .formulario__input-error').classList.add("formulario__input-error-activo");
        campos.Usuario = false;
    }
}

// Función para validar el campo "password" en tiempo real
function validarContraseñaRealTime(input) {
    const contraseña = input.value.trim();

    if (contraseña.length >= 4 && contraseña.length <= 20) {
        document.getElementById('grupo__Contraseña').classList.remove("formulario__grupo-incorrecto");
        document.getElementById('grupo__Contraseña').classList.add("formulario__grupo-correcto");
        document.querySelector('#grupo__Contraseña i').classList.add("fa-check-circle");
        document.querySelector('#grupo__Contraseña i').classList.remove("fa-times-circle");
        document.querySelector('#grupo__Contraseña .formulario__input-error').classList.remove("formulario__input-error-activo");
        campos.password = true;
    } else {
        document.getElementById('grupo__Contraseña').classList.add("formulario__grupo-incorrecto");
        document.getElementById('grupo__Contraseña').classList.remove("formulario__grupo-correcto");
        document.querySelector('#grupo__Contraseña i').classList.add("fa-times-circle");
        document.querySelector('#grupo__Contraseña i').classList.remove("fa-check-circle");
        document.querySelector('#grupo__Contraseña .formulario__input-error').classList.add("formulario__input-error-activo");
        campos.password = false;
    }
}


// Event listeners para validar el campo en tiempo real
const inputNombre = document.getElementById('nombre');
inputNombre.addEventListener('keyup', validarNombreRealTime);
inputNombre.addEventListener('blur', validarNombreRealTime);

const inputCorreo = document.getElementById('correo');
inputCorreo.addEventListener('keyup', validarCorreoRealTime);
inputCorreo.addEventListener('blur', validarCorreoRealTime);

const inputDireccion = document.getElementById('direccion');
inputDireccion.addEventListener('keyup', validarDireccionRealTime);
inputDireccion.addEventListener('blur', validarDireccionRealTime);

const inputUsuario = document.getElementById('usuario');
inputUsuario.addEventListener('keyup', validarUsuarioRealTime);
inputUsuario.addEventListener('blur', validarUsuarioRealTime);

const inputPassword = document.getElementById('password');
inputPassword.addEventListener('keyup', () => {
    validarContraseñaRealTime(inputPassword);
});
inputPassword.addEventListener('blur', () => {
    validarContraseñaRealTime(inputPassword);

});

//Validar que todos los campos esten vien diligenciados//

const btnRegistrarse = document.getElementById("btnRegistrarse");
const mensajeError = document.getElementById("mensajeError");

btnRegistrarse.addEventListener("click", (e) => {
    e.preventDefault(); // Prevenir envío automático del formulario

    // Validación manual de campos vacíos
    const inputsArray = Array.from(inputs);
    const emptyFields = inputsArray.filter(input => input.value.trim() === '');

    if (emptyFields.length > 0) {
        mensajeError.textContent = "Por favor, completa todos los campos.";
        return; // Detener el proceso si hay campos vacíos
    } else {
        mensajeError.textContent = ""; // Limpiar mensaje de error si no hay campos vacíos
    }

    // Realizar validación manual antes de permitir el envío
    const allFieldsValid = Object.values(campos).every(valor => valor === true);

    if (allFieldsValid) {
        formulario.submit(); // Envía el formulario si todos los campos son válidos
    } else {
        console.log("Por favor, completa correctamente todos los campos.");
    }
})