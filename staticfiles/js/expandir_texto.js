document.addEventListener('DOMContentLoaded', function() {
    const toggleButtons = document.querySelectorAll('.toggle-text');
    
    toggleButtons.forEach(function(toggleButton) {
        const commentText = toggleButton.previousElementSibling;

        if (commentText.scrollHeight > commentText.clientHeight) {
            toggleButton.style.display = 'inline';  // Mostrar "ver más" si el texto está truncado
        }

        toggleButton.addEventListener('click', function() {
            commentText.classList.toggle('full-text');  // Alterna entre truncado y completo
            if (commentText.classList.contains('full-text')) {
                toggleButton.innerText = 'Ver menos';
            } else {
                toggleButton.innerText = 'Ver más';
            }
        });
    });
});
