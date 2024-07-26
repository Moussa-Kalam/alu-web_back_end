const request = require('request');
const chai = require('chai')
const { expect } = require('chai');


describe('/ api', () => {
    it('status 200', (done) => {
        request('http://localhost:7865', (error, response, body) => {
            if (error) throw error;
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });


});

describe('GET /cart/:id', () => {
    it('status 404', (done) => {
        request('http://localhost:7865/cart/asd', (error, response) => {
            if (error) throw error;
            expect(response.statusCode).to.equal(404);
            done();
        });

    });

    it('status 200', (done) => {
        request('http://localhost:7865/cart/400', (error, response, body) => {
            if (error) throw error;
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 400');
            done();
        });

    }
    );
});