const car = document.getElementById('car');
const obstacle = document.getElementById('obstacle');
const gameContainer = document.getElementById('gameContainer');

let carPosition = 50; // Percentual da posição do carro na tela
let obstaclePosition = -50; // Começa fora da tela
let isGameOver = false;

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
        carPosition -= 10;
        if (carPosition < 0) carPosition = 0;
        car.style.left = `${carPosition}%`;
    } else if (event.key === 'ArrowRight') {
        carPosition += 10;
        if (carPosition > 100) carPosition = 100;
        car.style.left = `${carPosition}%`;
    }
});

function moveObstacle() {
    if (isGameOver) return;
    
    obstaclePosition += 5;
    if (obstaclePosition > 100) {
        obstaclePosition = -50; // Reseta a posição do obstáculo
    }
    
    obstacle.style.bottom = `${obstaclePosition}%`;
    
    // Verificar colisão
    const carRect = car.getBoundingClientRect();
    const obstacleRect = obstacle.getBoundingClientRect();
    
    if (
        carRect.left < obstacleRect.right &&
        carRect.right > obstacleRect.left &&
        carRect.top < obstacleRect.bottom &&
        carRect.bottom > obstacleRect.top
    ) {
        alert('Game Over!');
        isGameOver = true;
        return;
    }
    
    requestAnimationFrame(moveObstacle);
}

moveObstacle();
