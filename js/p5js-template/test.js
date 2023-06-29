const dummy = require('./code.js');

test('dummy returns three', () => {
    expect(dummy()).toBe(3);
});