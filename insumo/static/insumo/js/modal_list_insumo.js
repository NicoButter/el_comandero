$('#detalleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var nombre = button.data('nombre');
    var categoria = button.data('categoria');
    var costo = button.data('costo');
    var tipo = button.data('tipo');
    var imagen = button.data('imagen');
    var descripcion = button.data('descripcion');
    var cantidad = button.data('cantidad');
    var unidad = button.data('unidad');
    
    $('#modal-nombre').text(nombre);
    $('#modal-categoria').text(categoria);
    $('#modal-costo').text('$' + costo);
    $('#modal-tipo').text(tipo);
    $('#modal-imagen').attr('src', imagen);
    $('#modal-descripcion').text(descripcion);
    $('#modal-cantidad').text(cantidad);
    $('#modal-unidad').text(unidad);
});