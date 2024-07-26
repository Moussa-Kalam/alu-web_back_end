const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe('sendPaymentRequestToApi', () => {
    it('should call calculateNumber when calculating the total', () => {
        const calculateStub = sinon.stub(Utils, 'calculateNumber').returns(10);
        const consoleSpy = sinon.spy(console, 'log');
        sendPaymentRequestToApi(100, 20);
        expect(calculateStub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
        expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
    });
});