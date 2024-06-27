$(document).ready(function() {
  $("#formulario1").validate({
    rules: {
      txtEmail: {
        required: true,
        email: true,
      },
      txtContrasena: {
        required: true,
        minlength: 5,
      },
      txtRepetirContrasena: {
        required: true,
        equalTo: "#id_txtContrasena",
      },
      txtnumero: {
        required: true,
        maxlength: 9, 
      }
    }, 
    messages: {
      txtEmail: {
        required: "Ingrese email!!!",
        email: "No cumple formato",
      },
      txtContrasena: {
        required: "Ingrese Password!!!",
        minlength: "Min. 5 caract",
      },
      txtRepetirContrasena: {
        required: "Repita el Password!!",
        equalTo: "Deben ser iguales!!!!",
      },
      txtnumero:{
        required: "Ingrese numero",
        maxlength: "El máximo es 9",
      }
    } 
  });
});
