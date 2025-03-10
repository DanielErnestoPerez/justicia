// Obtener elementos
const newMessageButton = document.getElementById('newMessageButton');
const newMessagePopup = document.getElementById('newMessagePopup');
const closePopup = document.getElementById('closePopup');

// Mostrar ventana emergente cuando se hace clic en "New"
newMessageButton.addEventListener('click', (e) => {
    e.preventDefault(); // Prevenir acción predeterminada
    newMessagePopup.style.display = 'flex'; // Mostrar popup
});

// Cerrar ventana emergente
closePopup.addEventListener('click', () => {
    newMessagePopup.style.display = 'none'; // Ocultar popup
});

// Cerrar ventana al hacer clic fuera de ella
window.addEventListener('click', (e) => {
    if (e.target === newMessagePopup) {
        newMessagePopup.style.display = 'none';
    }
});
