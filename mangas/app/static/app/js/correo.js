document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.querySelector('.formulario');
    const emailInput = document.getElementById('exampleInputEmail1');

    formulario.addEventListener('submit', function (event) {
        event.preventDefault();
        const email = emailInput.value.trim();

        if (validarCorreo(email)) {
           
            console.log('Correo válido:', email);
            
        } else {
            
            console.error('Correo no válido');
        }
    });

    function validarCorreo(correo) {
        
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(correo);
    }
});
