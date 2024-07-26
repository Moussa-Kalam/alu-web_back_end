const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');
const sinon = require('sinon');
const { expect } = require('chai');


describe('sendPaymentRequestToApi', () => {
    it('should call calculateNumber when calculating the total', () => {
        const calculateSpy = sinon.spy(Utils, 'calculateNumber');
        sendPaymentRequestToApi(100, 20);
        expect(calculateSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    });
});