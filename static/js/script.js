//Ejecutar funciones
document.getElementById("btn_iniciarSesion").addEventListener("click", iniciarSesion);
document.getElementById("btn_Registrarse").addEventListener("click", register);
window.addEventListener("resize", anchoPagina);
const formulario=document.getElementById("formulario__Register");
const inputs = document.querySelectorAll("#formulario__Register input");
//Validacion de campos 



//Declaracion de las variables
var contenedor_login_register= document.querySelector(".contenedor__Login-registrer");
var formulario_login= document.querySelector(".formulario__login");
var formulario_Register= document.querySelector(".formulario__Register");
var caja_trasera_login= document.querySelector(".caja__trasera-login");
var caja_trasera_register= document.querySelector(".caja__trasera-register");
//Parte en la que hace la funcion de mover de un lado o otro con responsive

function anchoPagina(){
    if(window.innerWidth > 850){
        caja_trasera_login.style.display= "block";
        caja_trasera_register.style.display= "block";
    }else{
        caja_trasera_register.style.display="block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.display = "none";
        formulario_login.style.display= "block";
        formulario_Register.style.display= "none";
        contenedor_login_register.style.left= "0px";

    }
}

anchoPagina();


function iniciarSesion(){
    if(window.innerWidth >850)
    {
        formulario_Register.style.display = "none";
        contenedor_login_register.style.left ="10px";
        formulario_login.style.display="block";
        caja_trasera_register.style.opacity = "1";
        caja_trasera_login.style.opacity ="0";
    }
    else{
            formulario_Register.style.display = "none";
            contenedor_login_register.style.left ="0px";
            formulario_login.style.display="block";
            caja_trasera_register.style.display = "block";
            caja_trasera_login.style.display ="none";
        }
}


function register(){
    if(window.innerWidth > 850)
     {
        formulario_Register.style.display = "block";
        contenedor_login_register.style.left ="410px";
        formulario_login.style.display="none";
        caja_trasera_register.style.opacity = "0";
        caja_trasera_login.style.opacity ="1";
     }
    else{
        formulario_Register.style.display = "block";
        contenedor_login_register.style.left ="0px";
        formulario_login.style.display="none";
        caja_trasera_register.style.display = "none";
        caja_trasera_login.style.display ="block";
        caja_trasera_login.style.opacity = "1"; 
    }
}
