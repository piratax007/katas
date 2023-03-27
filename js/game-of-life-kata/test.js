import { assert } from "chai";
import { neighboursAlive } from "./code.js";

describe('suite test kata: game of life - next generation', function() {
    describe('Test neighboursAlive: Given a grid of states and a cell coordinates returns the number of neigbours alive', function() {
	it('A cell with three neighbours alive', function() {
	    const grid = [
		['Dead', 'Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Alive', 'Dead'],
		['Dead', 'Alive', 'Alive', 'Dead'],
		['Dead', 'Dead', 'Dead', 'Dead'],
	    ];
	    const cellCoordinates = [2, 2];
	    let expected = 3;
	    assert.equal(neighboursAlive(grid, cellCoordinates) , expected, 'must be equal to 3');
	});
	
	it('A cell with two neighbours alive', function() {
	    const grid = [
		['Dead', 'Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Alive', 'Dead'],
		['Dead', 'Alive', 'Alive', 'Dead'],
		['Dead', 'Dead', 'Dead', 'Dead'],
	    ];
	    const cellCoordinates = [3, 2];
	    let expected = 2;
	    assert.equal(neighboursAlive(grid, cellCoordinates) , expected, 'must be equal to 2');
	});	
    });
});

function newGridWithDeadCells(size) {
    if (size[0] === 1) {
	return [...Array(size[1])].map(() => ( 'Dead' ));
    }
    
    return [...Array(size[0])].map(() => ( [] )).map(() => ( [...Array(size[1])].map(() => ( 'Dead' )) ));
}

describe('Suite test: test hooks', function() {
    describe('Test changeCellsToAlive returns a grid with specific cells with state Alive', function() {
	
    });
    
    describe('Test newGridWithDeadCell returns a grid of dead cell with the given size', function() {
	it('A square grid of size four', function() {
	    const expected = [
		['Dead', 'Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Dead', 'Dead'],
	    ];
	    assert.deepEqual(newGridWithDeadCells([4, 4]), expected, 'must be a grid of dead cell with size 4x4');
	});

	it('A column grid with four entries', function() {
	    const expected = [
		['Dead'],
		['Dead'],
		['Dead'],
		['Dead'],
	    ];
	    assert.deepEqual(newGridWithDeadCells([4, 1]), expected, 'must be a column grid with four entries');
	});

	it('A row grid with five entries', function() {
	    const expected = ['Dead', 'Dead', 'Dead', 'Dead', 'Dead'];
	    assert.deepEqual(newGridWithDeadCells([1, 5]), expected, 'must be a row grid with five entries');
	});

	it('A rectangular grid of size 3x2', function() {
	    const expected = [
		['Dead', 'Dead'],
		['Dead', 'Dead'],
		['Dead', 'Dead'],
	    ];
	    assert.deepEqual(newGridWithDeadCells([3, 2]), expected, 'must be a rectangular grid of dead cell with size 3x2');
	});

	it('A rectangular grid of size 2x3', function() {
	    const expected = [
		['Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Dead'],
	    ];
	    assert.deepEqual(newGridWithDeadCells([2, 3]), expected, 'must be a rectangular grid of dead cell with size 2x3');
	});
    });
});
