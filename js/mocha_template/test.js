import { assert } from "chai";
import { dummy } from "./code.js";

describe('test suite kata', function() {
    describe('Test_function_description', function() {
		it('description', function() {
			let given = 2;
			let expected = dummy();
			assert.equal(given, expected, 'must be equal to 3');
		});
    });
});
