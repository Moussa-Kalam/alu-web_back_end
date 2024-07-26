
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');
describe('getPaymentTokenFromAPI', () => {
    it('should return a promise', (done) => {
        const promise = getPaymentTokenFromAPI(true);
        promise.then((value) => {
            expect(value).to.deep.equal({data: 'Successful response from the API'});
            done();
        })
    });
})