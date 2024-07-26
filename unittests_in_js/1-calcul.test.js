const calculateNumber = require("./1-calcul.js");
const assert = require('assert');


describe("Calculate | sum", () => {
    it("should sum the numbers(their floor) when the decimal part is lower than 5", () => {
        assert.strictEqual(calculateNumber('SUM', 1.1, 1.4), 2);
        assert.strictEqual(calculateNumber('SUM', 1.1, 1.4), 2);
    })

    it("should sum the numbers(their ceiling) when the decimal part is bigger or equal to 5", () => {
        assert.strictEqual(calculateNumber('SUM', 1.7, 2.8), 5);
        assert.strictEqual(calculateNumber('SUM', 1.9, 7.9), 10);
    })
})

describe("calculate | subtract", () => {
    it("should subtract the numbers(their floor) when the decimal part is lower than 5", () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 1.1, 1.4), 0);
        assert.strictEqual(calculateNumber('SUBTRACT', 1.1, 1.4), 0);
    });

    it("should subtract the numbers(their ceiling) when the decimal part is bigger or equal to 5", () => {
        assert.strictEqual(calculateNumber('SUBTRACT', 3.7, 1.8), 2);
        assert.strictEqual(calculateNumber('SUBTRACT', 7.9, 1.9), 6);
    })
})

describe("calculate | divide", () => {
    it("should divide the numbers(their floor) when the decimal part is lower than 5", () => {
        assert.strictEqual(calculateNumber('DIVIDE', 4.1, 2.2), 2);
    });

    it("should divide the numbers(their ceiling) when the decimal part is bigger or equal to 5", () => {
        assert.strictEqual(calculateNumber('DIVIDE', 14.9, 4.9), 3);
    });

    it("should throw an error if the second number is rounded to zero", () => {
        assert.strictEqual(calculateNumber('DIVIDE', 5, 0.1), "Error")
    })
})