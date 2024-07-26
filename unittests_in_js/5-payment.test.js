const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe("payment", () => {
    let consoleSpy;
    beforeEach(() => {
        consoleSpy = sinon.spy(console, 'log');
    })
    afterEach(() => {
        consoleSpy.restore();
    })
    it("should call the consolelog once", () => {
        sendPaymentRequestToApi(100, 20);
        expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    });

    it("should call the consolelog once with different values", () => {
        sendPaymentRequestToApi(10, 10);
        expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    });
})