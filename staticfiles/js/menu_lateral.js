// Mostrar el contenido y cerrar el menú en móviles
function mostrarElemento(id) {
    document.querySelectorAll('.elemento').forEach(elemento => {
        elemento.classList.remove('mostrar');
    });
    document.getElementById(id).classList.add('mostrar');

    // Ocultar menú en móviles tras seleccionar una opción
    if (window.innerWidth <= 768) {
        document.getElementById('menu_elemento').style.left = "-25";
    }
}

function toggleMenu() {
    const menu_elemento = document.getElementById('menu_elemento');

    if (window.innerWidth <= 768) {
        menu_elemento.classList.toggle('menu-abierto');
    } else {
        const elementoContainer = document.getElementById('elemento-container');
        if (menu_elemento.classList.contains('menu-abierto')) {
            menu_elemento.classList.remove('menu-abierto');
            elementoContainer.classList.remove('menu-abierto');
        } else {
            menu_elemento.classList.add('menu-abierto');
            elementoContainer.classList.add('menu-abierto');
        }
    }
}


// Reinicio del estado del menú al cambiar el tamaño de pantalla
window.addEventListener('resize', () => {
    const menu_elemento = document.getElementById('menu_elemento');
    const elementoContainer = document.getElementById('elemento-container');

    if (window.innerWidth > 768) {
        menu_elemento.style.left = ''; // Limpia el valor para que use la clase CSS
        menu_elemento.classList.remove('menu-abierto');
        elementoContainer.classList.remove('menu-abierto');
    } else {
        menu_elemento.style.left = "-25"; // Se asegura que esté oculto en móviles
    }
});

