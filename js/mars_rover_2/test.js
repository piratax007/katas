import { assert } from "chai";
import { createRover, moveRoverOnce } from "./code.js";

describe('in 0x0 plateau', function() {
	describe('move one rover in 0 0 N', function() {
		describe('to the right', function() {
			it('it ends in 0 0 E', function() {
				assert.deepEqual(
					moveRoverOnce(
						'R',
						createRover(0,0,"N")
					),
					createRover(0,0,"E"),
					'must be facing to E');
			});
		});

		describe('to the left', function() {
			it('it ends in 0 0 W', function() {
				assert.deepEqual(
					moveRoverOnce(
						"L",
						createRover(0,0,"N")),
					createRover(0,0,"W"),
					'must be facing to W');
			});
		});

		describe('forward', function() {
			it('it ends in 0 1 N', function() {
				assert.deepEqual(
					moveRoverOnce(
						"M",
						createRover(0,0,"N")),
					createRover(0,1,"N"),
					'must be in 0 1 facing to N');
			});


		});
	});

	describe("move one rover in 0 0 W", function() {
		describe('to the left', function() {
			it('it ends in 0 0 S', function() {
				assert.deepEqual(
					moveRoverOnce(
						"L",
						createRover(0,0,"W")
					),
					createRover(0,0,"S"),
					'must be facing to S');
			});
		});

		describe('to the right', function() {
			it('it ends in 0 0 N', function() {
				assert.deepEqual(
					moveRoverOnce(
						'R',
						createRover(0,0,"W")
					),
					createRover(0,0,"N"),
					'must be facing to N');
			});
		});
	});

	describe("move one rover in 0 0 E", function() {
		describe('to the left', function() {
			it('it ends in 0 0 S', function() {
				assert.deepEqual(
					moveRoverOnce(
						"L",
						createRover(0,0,"W")
					),
					createRover(0,0,"S"),
					'must be facing to S');
			});
		});

		describe('to the right', function() {
			it('it ends in 0 0 N', function() {
				assert.deepEqual(
					moveRoverOnce(
						'R',
						createRover(0,0,"W")
					),
					createRover(0,0,"N"),
					'must be facing to N');
			});
		});

		describe('forward', function() {
			it('it ends in 0 1 E', function() {
				assert.deepEqual(
					moveRoverOnce(
						"M",
						createRover(0,0,"E")),
					createRover(1,0,"E"),
					'must be in 0 1 facing to E');
			});
		});
	});
});
