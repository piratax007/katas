import { assert } from "chai";
import { neighboursAlive, setNextGenerationState } from "./code.js";
import { newGridWithDeadCells, newTestGrid } from "./tests-hooks.js";

describe('Test suite kata: game of life - next generation', function() {
    describe('Test neighboursAlive: Given a grid of states and a cell coordinates returns the number of neigbours alive', function() {
	it('A cell output of the edges has at most eight neighbours alive', function() {
	    let generation = newTestGrid([[1, 2], [2, 1], [2, 2]], [4, 4]);
	    assert.equal(neighboursAlive(generation, [1, 1]) , 3, 'The cell (1, 1) has three neigbours alive');

	    generation = newTestGrid([[1, 2], [2, 1], [2, 2]], [4, 4]);
	    assert.equal(neighboursAlive(generation, [2, 2]), 2, 'The cell (2, 2) has two neighbours alive');
	});

	it('A cell on a edge has at most five neighbours alive', function () {
	    let generation = newTestGrid([[0, 0], [0, 1], [1, 1], [2, 0], [2, 1]], [4, 4]);
	    assert.equal(neighboursAlive(generation, [1, 0]), 5, 'The cell (1, 0) has all their neighbours alive');

	    generation = newTestGrid([[0, 1], [0, 3], [1, 3], [2, 1], [3, 3]], [4, 4]);
	    assert.equal(neighboursAlive(generation, [0, 2]), 3, 'The cell (0, 2) has three neighbours alive');

	    generation = newTestGrid([[2, 4]], [3, 6]);
	    assert.equal(neighboursAlive(generation, [1, 5]), 1, 'The cell (1, 5) has just one neighbour alive');

	    generation = newTestGrid([[1, 1], [1, 3], [1, 5], [2, 5], [0, 0]], [3, 6]);
	    assert.equal(neighboursAlive(generation, [2, 2]), 2, 'The cell (2, 2) has two neighbours alive');

	    generation = newTestGrid([[0, 0], [0, 2], [0, 3], [0, 4]], [1, 7]);
	    assert.equal(neighboursAlive(generation, [0, 3]), 2, 'The cell (0, 3) has two neighbours alive');

	    generation = newTestGrid([[0, 0], [4, 0], [5, 0]], [6, 1]);
	    assert.equal(neighboursAlive(generation, [4, 0]), 1, 'The cell (4, 0) has one neighbour alive');

	    generation = newTestGrid([[0, 1], [1, 1], [2, 0], [3, 1]], [4, 2]);
	    assert.equal(neighboursAlive(generation, [1, 1]), 2, 'The cell (1, 1) has two neighbours alive');

	    generation = newTestGrid([[0, 0], [0, 3], [1, 2], [1, 4]], [2, 5]);
	    assert.equal(neighboursAlive(generation, [1, 3]), 3, 'The cell (1, 3) has three neighbours alive');
	});

	it('A cell on a corner has at most three neighbours alive', function () {
	    let generation = newTestGrid([[0, 0], [0, 1], [1, 0], [1, 1]], [2, 2]);
	    assert.equal(neighboursAlive(generation, [0, 1]), 3, 'The cell (0, 1) has three neighbours alive');

	    generation = newTestGrid([], [3, 5]);
	    assert.equal(neighboursAlive(generation, [0, 0]), 0, 'The cell (0, 0) has no neighbours alive');

	    generation = newTestGrid([[2, 0], [2, 1], [3, 1], [1, 1]], [4, 2]);
	    assert.equal(neighboursAlive(generation, [3, 0]), 3, 'The cell (3, 0) has all their neighbours alive');

    	    generation = newTestGrid([[2, 0], [2, 1], [2, 2], [3, 1], [1, 1]], [4, 4]);
	    assert.equal(neighboursAlive(generation, [3, 3]), 1, 'The cell (3, 3) has one neighbour alive');
	});

	it('A grid with just one cell has no neighbours alive', function() {
	    let generation = newTestGrid([[0, 0]], [1, 1]);
	    assert.equal(neighboursAlive(generation, [0, 0]), 0, 'The cell (0, 0) has no neighbours alive');
	});
    });

    describe('Test setNextGenerationState returns the state of a cell in the next generation', function() {
	it('A cell with fewer than two live neighbours will be dead by underpopulabtion', function() {
	    let generation = newTestGrid([[1, 1], [2, 0], [2, 1], [2, 2], [3, 1], [3, 3]], [4, 4]);
	    assert.equal(setNextGenerationState(generation, [3, 3]), 'Dead', 'The cell (3, 3) will be dead in the next generation');

	    generation = newTestGrid([], [3, 5]);
	    assert.equal(setNextGenerationState(generation, [0, 0]), 'Dead', 'The cell (0, 0) will be dead in the next generation');

	    generation = newTestGrid([[2, 4]], [3, 6]);
	    assert.equal(setNextGenerationState(generation, [1, 5]), 'Dead', 'The cell (1, 5) will be dead in the next generation');
	});

	it('A cell with more than three live neighbours will be dead by overcrowding', function() {
	    let generation = newTestGrid([[0, 0], [0, 1], [1, 1], [2, 0], [2, 1]], [4, 4]);
	    assert.equal(setNextGenerationState(generation, [1, 0]), 'Dead', 'The cell (1, 0) will be dead in the next generation because has five neighbours alive');

	    generation = newTestGrid([[0, 4], [1, 2], [1, 3], [3, 1], [3, 3], [4, 0]], [5, 5]);
	    assert.equal(setNextGenerationState(generation, [2, 2]), 'Dead', 'The cell (2, 2), will be dead because has four neighbours alive');
	});

	it('A live cell with two or three live neighbours will be live in the next generation', function() {
	    let generation = newTestGrid([[1, 1], [1, 3], [1, 5], [2, 2], [2, 5], [0, 0]], [3, 6]);
	    assert.equal(generation[2][2], 'Alive', 'The cell (2, 2) should be alive');
	    assert.equal(setNextGenerationState(generation, [2, 2]), 'Alive', 'The cell (2, 2) will be alive because has two neighbours alive');

	    generation = newTestGrid([[1, 1], [1, 3], [1, 5], [2, 5], [0, 0]], [3, 6]);
	    assert.equal(generation[2][2], 'Dead', 'The cell (2, 2) is dead');
	    assert.equal(setNextGenerationState(generation, [2, 2]), 'Dead', 'The cell (2, 2) will be dead because has two neighbours alive');
	});

	it('A dead cell with exactly three live neighbours becomes a live cell', function() {
	    let generation = newTestGrid([[1, 2], [2, 1], [2, 2]], [4, 4]);
	    assert.equal(generation[1][1], 'Dead', 'The cell (1, 1) should be dead');
	    assert.equal(setNextGenerationState(generation, [1, 1]) , 'Alive', 'The cell (1, 1) will be alive because has three neigbours alive');
	});
    });
});

describe('Test suite: tests hooks', function() {
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

    describe('Test newTestGrid returns a grid with specific cells with state Alive', function() {
	it('Cell (0, 1) from a row grid of size 1x4, is alive', function() {
	    const expected = ['Dead', 'Alive', 'Dead', 'Dead'];
	    assert.deepEqual(newTestGrid([[0, 1]], [1, 4]), expected, 'The cell (0, 1) must be alive');
	});

	it('Cells (0, 1) and (0, 2) from a row grid of size 1x4, are alive', function() {
	    const expected = ['Dead', 'Alive', 'Alive', 'Dead'];
	    assert.deepEqual(newTestGrid([[0, 1], [0, 2]], [1, 4]), expected, 'Cells (0, 1) and (0, 2) must be alive');
	});

	it('Cell (2, 0) from a column grid of size 4x1, is alive', function() {
	    const expected = [
		['Dead'],
		['Dead'],
		['Alive'],
		['Dead'],
	    ];
	    assert.deepEqual(newTestGrid([[2, 0]], [4, 1]), expected, 'The cell (2, 0) must be alive');
	});

	it('Cells (1, 2), (2, 1) and (2, 2) from a grid of size 4x4, change to alive', function () {
	    const expected = [
		['Dead', 'Dead', 'Dead', 'Dead'],
		['Dead', 'Dead', 'Alive', 'Dead'],
		['Dead', 'Alive', 'Alive', 'Dead'],
		['Dead', 'Dead', 'Dead', 'Dead'],
	    ];
	    assert.deepEqual(newTestGrid([[1, 2], [2, 1], [2, 2]], [4, 4]), expected, 'Cells (1, 2), (2, 1) and (2, 2) must be alive');
	});
    });    
});
