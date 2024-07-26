const calculateNumber = require("./2-calcul_chai.js");
const { expect } = require("chai");


describe("Calculate | sum", () => {
    it("should sum the numbers(their floor) when the decimal part is lower than 5", () => {
        expect(calculateNumber('SUM', 1.1, 1.4)).equal(2);
        expect(calculateNumber('SUM', 1.1, 1.4)).equal(2);
    })

    it("should sum the numbers(their ceiling) when the decimal part is bigger or equal to 5", () => {
        expect(calculateNumber('SUM', 1.7, 2.8)).equal(5);
        expect(calculateNumber('SUM', 1.9, 7.9)).equal(10);
    })
})

describe("calculate | subtract", () => {
    it("should subtract the numbers(their floor) when the decimal part is lower than 5", () => {
        expect(calculateNumber('SUBTRACT', 1.1, 1.4)).equal(0);
        expect(calculateNumber('SUBTRACT', 1.1, 1.4)).equal(0);
    });

    it("should subtract the numbers(their ceiling) when the decimal part is bigger or equal to 5", () => {
        expect(calculateNumber('SUBTRACT', 3.7, 1.8)).equal(2);
        expect(calculateNumber('SUBTRACT', 7.9, 1.9)).equal(6);
    })
})

describe("calculate | divide", () => {
    it("should divide the numbers(their floor) when the decimal part is lower than 5", () => {
        expect(calculateNumber('DIVIDE', 4.1, 2.2)).equal(2);
    });

    it("should divide the numbers(their ceiling) when the decimal part is bigger or equal to 5", () => {
        expect(calculateNumber('DIVIDE', 5.9, 2.1)).equal(3);
    });

    it("should throw an error if the second number is rounded to zero", () => {
        expect(calculateNumber('DIVIDE', 5, 0.1)).equal("Error");
    })
})