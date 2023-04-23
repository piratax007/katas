import { assert } from "chai";
import { add, getDelimiters } from "./code.js";

describe('The function add', () => {
    describe('with an empty string', () => {
        it('returns zero', () => {
            assert.equal(add(""), 0);
        });
    });

    describe('with a single number string', () => {
        it('returns the whole number', () => {
            assert.equal(add("0"), 0);
            assert.equal(add("1"), 1);
            assert.equal(add("17"), 17);
            assert.equal(add("999"), 999);
        });
    });

    describe('with a string of two numbers separated by comma', () => {
        it('returns the sum of the two numbers', () => {
            assert.equal(add("1,2"), 3);
            assert.equal(add("4,0"), 4);
            assert.equal(add("12,15"), 27);
            assert.equal(add("112,3"), 115);
        });
    });

    describe('with a string that have more than two numbers separated by commas and spaces after the comma', () => {
        it('returns the sum of all numbers in the given string', () => {
            assert.equal(add("1, 2, 3"), 6);
            assert.equal(add("3, 5, 6, 2"), 16);
            assert.equal(add("1, 12, 24, 118, 5, 63"), 223);
        });
    });

    describe('with a string containing numbers separated by commas or new lines', () => {
        it('returns the sum of the numbers into the given string', () => {
            assert.equal(add("1\n2"), 3);
            assert.equal(add("1\n2,3"), 6);
            assert.equal(add("3,4\n2"), 9);
            assert.equal(add("3, 5\n12\n18,10,25\n1"), 74);
        });
    });

    describe('taking a string in which the first line have the delimiter', () => {
        it('returns the sum of the numbers separated by the delimiter from the second line forward', () => {
            assert.equal(add("//;\n1;2"), 3);
            assert.equal(add("//,\n4,7,2"), 13);
        })
    });

    describe('taking a negative number', () => {
        it('throw an exception "negatives not allowed" and the negative passed', () => {
            assert.throws(() => {add("//,\n-1");}, Error, 'negatives not allowed: -1');
            assert.throws(() => {add("-30, 2");}, Error, 'negatives not allowed: -30');
        });
    });

    describe('taking more than a single negative number', () => {
        it('throw and exception "negatives not allowed" showing all the negatives passed', () => {
            assert.throws(() => {add("//;\n3;-2;10;-1;5");}, Error, 'negatives not allowed: -2,-1');
            assert.throws(() => {add("0, -1, 3, 2, -5, -7, -10, 12");}, Error, 'negatives not allowed: -1,-5,-7,-10');
        });
    });

    describe('taking numbers bigger than 1000', () => {
        it('should ignore these bigger numbers', () => {
            assert.equal(add("//;\n2;1001"), 2);
            assert.equal(add("1500\n54,152,4\n10,2310"), 220);
        });
    });

    describe('with a delimiter which length is greater than one', () => {
        it('should use the delimiter without care their length', () => {
            assert.equal(add("//[:]\n11:3"), 14);
            assert.equal(add("//[***]\n1***2***3"), 6);
            assert.equal(add("//[-----]\n10-----3-----5-----2"), 20);
        });
    });

/*    describe('with more than one delimiter', () => {
        it('should add the numbers without care how many delimiters were specified', () => {
            assert.equal(add("//[*][%]\n1*2%3"), 6);
        });
        });
        */
});

describe('The function getDelimiters', () => {
    it('get the delimiter from a string with the format "//[delimiter]"', () => {
        assert.deepEqual(getDelimiters("//[;]"), [';']);
        assert.deepEqual(getDelimiters("//[***]"), ['***']);
        assert.deepEqual(getDelimiters("//[$$]"), ['$$']);
    });

    it('get all the delimiters from a string with the format "\\[delim1][delim2]...[delimn]"', () => {
        assert.deepEqual(getDelimiters("//[-][::]"), ['-', '::']);
        assert.deepEqual(getDelimiters("//[-][%][***]"), ['-', '%', '***']);
    });
});
