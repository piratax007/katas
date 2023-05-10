import { assert } from "chai";
import { getNewDirection, validateEdges, setNewPosition, moveRover } from "./code.js";

describe('test suite mars rover kata', () => {
    describe('The getNewDirection function', () => {
        it('with N as the current direction, and L as the rotate direction, returns W as the new direction', () => {
            assert.equal(getNewDirection('N', 'L'), 'W');
        });

        it('with N as the current direction, and R as the rotate direction, returns E as the new direction', () => {
            assert.equal(getNewDirection('N', 'R'), 'E');
        });

        it('with W as the current direction, and L as the rotate direction, returns S as the new direction', () => {
            assert.equal(getNewDirection('W', 'L'), 'S');
        });

        it('with W as the current direction, and R as the rotate direction, returns N as the new direction', () => {
            assert.equal(getNewDirection('W', 'R'), 'N');
        });

        it('with S as the current direction, and L as the rotate direction, returns E as the new direction', () => {
            assert.equal(getNewDirection('S', 'L'), 'E');
        });

        it('with S as the current direction, and R as the rotate direction, returns W as the new direction', () => {
            assert.equal(getNewDirection('S', 'R'), 'W');
        });

        it('with E as the current direction, and L as the rotate direction, returns N as the new direction', () => {
            assert.equal(getNewDirection('E', 'L'), 'N');
        });

        it('with E as the current direction, and R as the rotate direction, returns S as the new direction', () => {
            assert.equal(getNewDirection('E', 'R'), 'S');
        });
    });

    describe('The validateEdges function', () => {
        describe('with a grid of one cell size', () => {
            it('returns false with anyone move coordinates', () => {
                assert.isFalse(validateEdges([0, 0], [0, 1]));
                assert.isFalse(validateEdges([0, 0], [-1, 0]));
                assert.isFalse(validateEdges([0, 0], [0, -1]));
                assert.isFalse(validateEdges([0, 0], [1, 0]));
            });
        });

        describe('with a grid of more than one cell size', () => {
            it('returns true if the new position is between the grid boundaries', () => {
                assert.isTrue(validateEdges([5, 5], [3, 2]));
                assert.isTrue(validateEdges([5, 5], [0, 1]));
                assert.isTrue(validateEdges([3, 3], [3, 3]));
            });

            it('return false if the new position is out of the grid boundaries', () => {
                assert.isFalse(validateEdges([3, 3], [4, 2]));
                assert.isFalse(validateEdges([2, 2], [0, -1]));
                assert.isFalse(validateEdges([0, 3], [0, 4]));
            });
        });
    });

    describe('The setNewPosition function', () => {
        describe('on a grid with enough size', () => {
            it('returns [2, 3] such the new position from the [3, 3] current position and with W as direction', () => {
                assert.deepEqual(setNewPosition([6, 6], [3, 3], 'W'), [2, 3]);
            });

            it('returns [3, 4] such the new position from the [3, 3] current position and with N as direction', () => {
                assert.deepEqual(setNewPosition([6, 6], [3, 3], 'N'), [3, 4]);
            });

            it('returns [2, 0] such the new position from the [2, 1] current position and with S as direction', () => {
                assert.deepEqual(setNewPosition([2, 2], [2, 1], 'S'), [2, 0]);
            });

            it('returns [2, 1] such the new position from the [1, 1] current position and with E as direction', () => {
                assert.deepEqual(setNewPosition([4, 4], [1, 1], 'E'), [2, 1]);
            });
        });

        describe('on a grid with no enough size', () => {
            it('throw an exception "edge reached" if the current position is on any edge and the direction produce an over edge movement', () => {
                assert.throws(() => {setNewPosition([2, 2], [0, 1], 'W');}, Error, 'edge reached');
                assert.throws(() => {setNewPosition([2, 2], [1, 2], 'N');}, Error, 'edge reached');
                assert.throws(() => {setNewPosition([3, 2], [3, 0], 'S');}, Error, 'edge reached');
                assert.throws(() => {setNewPosition([4, 5], [5, 3], 'E');}, Error, 'edge reached');
            });
        });
    });

    describe('The moveRover function', () => {
        describe('given a grid of size [5, 5], with and [1, 2] such a current position and N such a current direction', () => {
            it('with LL such a list of movements, returns "1 2 S"', () => {
                assert.equal(moveRover([5, 5], [1, 2], 'N', 'LL'), '1 2 S');
            });

            it.skip('with RRRR such the list of movements, returns "1 1 N"', () => {
                assert.equal(moveRover([5, 5], [1, 2], 'N', 'RRRR'), '1 1 N');
            });
        });
    });
});
