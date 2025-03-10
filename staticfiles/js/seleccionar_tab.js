function setSelectedTab(event) {
    // Eliminar la clase 'selected' de todas las pestañas
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => tab.classList.remove('selected'));

    // Añadir la clase 'selected' a la pestaña clickeada
    event.target.classList.add('selected');
}