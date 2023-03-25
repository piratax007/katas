let assert = require('chai').assert

describe('test suite kata', function() {
    describe('Test_function_description', function() {
	it('description', function() {
	    let given = 2;
	    let expected = 3;
	    assert.equal(given, expected, 'must be equal to 3');
	});
    });
});
