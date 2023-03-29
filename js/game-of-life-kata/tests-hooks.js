function newGridWithDeadCells(gridSize) {
    if (gridSize[0] === 1) {
	return [...Array(gridSize[1])].map(() => ( 'Dead' ));
    }
    
    return [...Array(gridSize[0])].map(() => ( [] )).map(() => ( [...Array(gridSize[1])].map(() => ( 'Dead' )) ));
}

function newTestGrid(positionsCellsAlive, gridSize) {
    let result = newGridWithDeadCells(gridSize);

    switch (typeof result[0]) {
    case "string":
	for (let position of positionsCellsAlive) {
	    result[position[1]] = 'Alive';
	}
	break;
    case "object":
	for (let position of positionsCellsAlive) {
	    result[position[0]][position[1]] = 'Alive';
	}
	break;
    }

    return result;
}

export {newGridWithDeadCells, newTestGrid};
