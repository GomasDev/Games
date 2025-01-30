const tablero = document.getElementById("tablero");
const mensaje = document.getElementById("textovictoria");
const reiniciar = document.getElementById("botonReiniciar");
let jugador_actual = "X";
let estado_tablero = ["", "", "", "", "", "", "", "", ""];
let gameActivo = true;

// Función para verificar si hay un ganador
function verificar_ganador() {
    const ganador = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];
    for (const combo of ganador) {
        const [a, b, c] = combo;
        if (estado_tablero[a] && estado_tablero[a] === estado_tablero[b] && estado_tablero[a] === estado_tablero[c]) {
            return estado_tablero[a];
        }
    }
    if (estado_tablero.every(celda => celda !== "")) {
        return "Empate";
    }
    return null;
}

// Manejar el clic en las celdas
function click(event) {
    const indice_celdas = event.target.dataset.index;
    if (estado_tablero[indice_celdas] === "" && gameActivo) {
        estado_tablero[indice_celdas] = jugador_actual;
        event.target.textContent = jugador_actual; // Mostrar símbolo en el botón
        const ganador = verificar_ganador();
        if (ganador) {
            gameActivo = false;
            mensaje.style.visibility = "visible"; // Hace visible el mensaje
            if (ganador === "Empate") {
                mensaje.textContent = "Empate";
            } else {
                mensaje.textContent = `¡${ganador} ha ganado!`;
            }
        } else {
            jugador_actual = jugador_actual === "X" ? "O" : "X"; // Cambiar de jugador
        }
    }
}

// Función para crear el tablero
function crearTablero() {
    tablero.innerHTML = ''; // Limpiar el contenido del tablero actual
    for (let i = 0; i < 9; i++) {
        const celda = document.createElement("button");
        celda.classList.add("celda");
        celda.dataset.index = i;
        celda.addEventListener("click", click);
        tablero.appendChild(celda); // Añadir el botón al tablero
    }
}

// Función para reiniciar el juego
function reiniciarJuego() {
    // Limpiar el contenido del tablero
    const celdas = document.querySelectorAll('#tablero button');
    
    if (!celdas || celdas.length === 0) {
        console.error('No se encontraron celdas en el tablero.');
        return; // Salir de la función si no se encuentran las celdas
    }

    // Limpiar el contenido de cada celda
    celdas.forEach(celda => {
        celda.textContent = '';  // Limpiamos el texto de las celdas visibles
        celda.disabled = false;  // Rehabilitar los botones por si se deshabilitaron al ganar
    });

    // Reiniciar las variables del juego
    jugador_actual = "X";  // Volver a asignar al jugador 'X' como el jugador inicial
    estado_tablero = ["", "", "", "", "", "", "", "", ""];  // Reiniciar el estado del tablero
    gameActivo = true;  // Marcar el juego como activo de nuevo

    // Ocultar mensaje de victoria o empate
    mensaje.style.visibility = "hidden";
    mensaje.textContent = '';  // Borrar el contenido del mensaje, por si hubo alguna victoria previa
}

// Crear el tablero inicialmente
crearTablero();

// Añadir el evento de reinicio al botón de reiniciar
reiniciar.addEventListener("click", reiniciarJuego);