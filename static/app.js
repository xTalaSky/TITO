/*Código para el boton tipo hamburguesa en disposivos móviles*/

document.addEventListener('DOMContentLoaded', function() {
    const detailsElement = document.querySelector('.cuadro details');

    detailsElement.addEventListener('mouseleave', function() {
        detailsElement.removeAttribute('open');
    });
});

/*funcion de boton de marcas*/
function toggleDropdown() {
    const dropdownContent = document.getElementById('dropdownContent');
    if (dropdownContent.style.display === 'block') {
        dropdownContent.style.display = 'none';
    } else {
        dropdownContent.style.display = 'block';
    }
}

/*Código para hacer funcionar el formulario */

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Simulate form submission and response
    const nombre = document.querySelector('input[name="nombre"]').value;
    const correo = document.querySelector('input[name="correo"]').value;
    const mensaje = document.querySelector('textarea[name="mensaje"]').value;

    if (nombre && correo && mensaje) {
        // Simulate a successful submission
        showFlashMessage('Mensaje enviado correctamente', 'success');
        this.reset(); // Reset the form fields
    } else {
        // Simulate an error (e.g., invalid email)
        showFlashMessage('Correo electrónico no existente', 'danger');
    }
});

function showFlashMessage(message, category) {
    const flashContainer = document.getElementById('flash-messages');
    const flashMessage = document.createElement('div');
    flashMessage.className = `alert ${category}`;
    flashMessage.textContent = message;

    flashContainer.appendChild(flashMessage);

   
    setTimeout(() => {
        flashMessage.remove();
    }, 5000);
}