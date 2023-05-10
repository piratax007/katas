function getNewDirection(currentDirection, rotateDirection) {
    switch (rotateDirection) {
    case 'L':
        return ['W', 'N', 'E', 'S'][calculateIndex(-1)];
    case 'R':
        return ['W', 'N', 'E', 'S'][calculateIndex(1)];
    }

    function calculateIndex(shift) {
        if (['W', 'N', 'E', 'S'].indexOf(currentDirection) + shift < 0) {
            return 3;
        }

        if (['W', 'N', 'E', 'S'].indexOf(currentDirection) + shift > 3) {
            return 0;
        }

        return ['W', 'N', 'E', 'S'].indexOf(currentDirection) + shift
    }
}

function validateEdges(gridSize, newPosition) {
    if (newPosition[0] < 0 || newPosition[0] > gridSize[0] || newPosition[1] < 0 || newPosition[1] > gridSize[1]) {
        return false;
    }

    return true;
}

function setNewPosition(gridSize, currentPosition, moveDirection) {
    if (validateEdges(gridSize, calculateNewPositionCoordinates(currentPosition, moveDirection))){
        return calculateNewPositionCoordinates(currentPosition, moveDirection);
    }

    throw new Error('edge reached');

    function calculateNewPositionCoordinates(currentPosition, moveDirection) {
        switch (moveDirection) {
        case 'N':
            return [currentPosition[0], currentPosition[1] + 1];
        case 'S':
            return [currentPosition[0], currentPosition[1] - 1];
        case 'W':
            return [currentPosition[0] - 1, currentPosition[1]];
        case 'E':
            return [currentPosition[0] + 1, currentPosition[1]];
        }
    }
}

function moveRover(gridSize, currentPosition, currentDirection, listOfMovements) {
    if (listOfMovements.length > 0) {
        console.log(`BLAHHHH ${listOfMovements.substring(1)}`);
        moveRover(gridSize, currentPosition, getNewDirection(currentDirection, listOfMovements.split("").shift()), listOfMovements.substring(1));
    }

    console.log(`BLEEEEE ${currentPosition[0]} ${currentPosition[1]} ${currentDirection}`);

        return `${currentPosition[0]} ${currentPosition[1]} ${currentDirection}`;
    
}

export {getNewDirection, validateEdges, setNewPosition, moveRover};
