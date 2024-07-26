const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
    it('should return 1', () => {
        assert.strictEqual(calculateNumber(1, 0), 1);
    });

    it('should return 1', () => {
        assert.strictEqual(calculateNumber(1.1, 0.1), 1);
    });

    it('should return 5', () => {
        assert.strictEqual(calculateNumber(1.4, 3.5), 5);
    });

    it('should return 5', () => {
        assert.strictEqual(calculateNumber(1.9, 3), 5)
    })

});