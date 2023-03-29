function flatCellPosition(grid, cellGridPosition) {
    return cellGridPosition[0] * grid[cellGridPosition[0]].length + cellGridPosition[1];
}

function translateStates(generation) {
    return generation.flat().map(cell => ( cell === 'Dead' ? 0 : 1 ));
}

function flatNeighboursPositions(cellIndex, boundary) {
    if (boundary === 0) {
	return new Set([cellIndex - 1, cellIndex + 1]);
    }
    
    return new Set([
	cellIndex - (boundary + 2), cellIndex - (boundary + 1), cellIndex - boundary,
	cellIndex - 1, cellIndex + 1,
	cellIndex + boundary, cellIndex + (boundary + 1), cellIndex + (boundary + 2)
    ]);
}

function compareArrays(array, otherArray) {
    return array[0] === otherArray[0] && array[1] === otherArray[1];
}

const isCorner = function(grid, cellCoordinates) {
    const rows = grid.length;
    const columns = grid[0].length;

    if (compareArrays(cellCoordinates, [0, 0]) || compareArrays(cellCoordinates, [0, columns-1]) || compareArrays(cellCoordinates, [rows-1, 0]) || compareArrays(cellCoordinates, [rows-1, columns-1])) {
	return true;
    }

    return false;
}

const cornerPosition = function (grid, cellCoordinates) {
    const rows = grid.length;
    const columns = grid[0].length;
    
    if (compareArrays(cellCoordinates, [0, 0])) {
	return "Top Left";
    }

    if (compareArrays(cellCoordinates, [0, columns-1])) {
	return "Top Right";
    }

    if (compareArrays(cellCoordinates, [rows-1, 0])) {
	return "Bottom Left";
    }

    if (compareArrays(cellCoordinates, [rows-1, columns-1])) {
	return "Bottom Right";
    }

    return "is not a corner";
}

const cornerNeighbours = function (grid, cornerCoordinates) {
    const rows = grid.length;
    const columns = grid[0].length;
    const maxFlatIndex = (rows * columns) - 1;
    
    switch (cornerPosition(grid, cornerCoordinates)) {
	case "Top Left":
	    return [1, grid[0].length, grid[0].length + 1];
	case "Top Right":
	    return [grid[0].length - 2, 2 * (grid[0].length - 1), 2 * grid[0].length - 1];
	case "Bottom Left":
	    return [
		maxFlatIndex - grid[0].length + 2,
		maxFlatIndex - 2 * grid[0].length + 2,
		maxFlatIndex - 2 * grid[0].length + 1,
	    ];
	case "Bottom Right":
	    return [maxFlatIndex - 1, maxFlatIndex - grid[0].length, maxFlatIndex - grid[0].length - 1];
	}
}

const totalNeighbours = function(generation, cellCoordinates) {
    if (isCorner(generation, cellCoordinates)) {
	return cornerNeighbours(generation, cellCoordinates);
    } else {
	return flatNeighboursPositions(flatCellPosition(generation, cellCoordinates), generation[0].length-1);
    }
}

const neighboursAlive = function (generation, cellCoordinates) {
    let result = 0;
    
    const statesValues = translateStates(generation);

    totalNeighbours(generation, cellCoordinates).forEach(neighbour => (
	statesValues[neighbour] === undefined ? 0 : result += statesValues[neighbour])
		      );

    return result;
}

const deadBecomesAlive = function(currentState, neighboursAliveCount) {
    return currentState === 'Dead' && neighboursAliveCount === 3;
}

const liveBecomesDead = function(currentState, neighboursAliveCount) {
    return currentState === 'Alive' && (neighboursAliveCount < 2 || neighboursAliveCount > 3);
}

function setNextGenerationState(currentGeneration, cellCoordinates) {
    const currentState = currentGeneration[cellCoordinates[0]][cellCoordinates[1]];
    const neighboursAliveCount = neighboursAlive(currentGeneration, cellCoordinates);
    
    if (deadBecomesAlive(currentState, neighboursAliveCount)) {
	return 'Alive';
    }

    if (liveBecomesDead(currentState, neighboursAliveCount)) {
	return 'Dead';
    }

    return currentState;
}

export {neighboursAlive, setNextGenerationState};
