$(document).ready(function(){
   
    $.ajax({
        url: 'https://api.shipit.cl/v/regions',
        type: 'GET',
        success: function(data){
          
            data.forEach(function(region){
                $('#lista-regiones').append($('<option>', {
                    value: region.name,
                    text: region.name
                }));
            });
        },
        error: function(xhr, status, error){
            console.error('Error al obtener las regiones:', error);
        }
    });
});
``
