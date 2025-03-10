document.addEventListener("DOMContentLoaded", function () {
    let cards = document.querySelectorAll(".cards");
    let index = 0;
    const intervalTime = 7000;
    let resetTimeout; // Variable para el timeout del reinicio inmediato

    function rotateCards() {
        let angle = 0;
        cards.forEach((card, i) => {
            if (i < index) {
                card.classList.add("away");
                card.style.transform = `translateX(70vh) translateY(-20vh) rotate(90deg)`;
                setTimeout(() => {
                    card.style.opacity = "0";
                    card.style.pointerEvents = "none"; // Deshabilita la interacción
                }, 500); // Retraso antes de desaparecer (ajústalo si es necesario)
            } else {
                card.classList.remove("away");
                card.style.transform = `rotate(${angle}deg)`;
                card.style.opacity = "1";
                card.style.pointerEvents = "auto"; // Reactiva la interacción
                angle -= 10;
                card.style.zIndex = cards.length - i;
            }
        });

        // Verificar si todas las cartas han desaparecido
        if (index === cards.length) {
            clearTimeout(resetTimeout); // Limpiar cualquier timeout previo
            resetTimeout = setTimeout(() => {
                index = 0; // Reiniciar el índice de las cartas
                rotateCards(); // Restablecer el deck inmediatamente
            }, 1000); // 1 segundo de espera antes de reiniciar
        }
    }

    // Iniciar la animación cada 7 segundos
    setInterval(() => {
        if (index < cards.length) {
            index = (index + 1) % (cards.length + 1);
            rotateCards();
        }
    }, intervalTime);

    // Inicializar la posición de las cartas
    rotateCards();
});
