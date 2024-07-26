const request = require('request');
const chai = require('chai')
const { expect } = require('chai');


describe('server', () => {
    it('status 200', (done) => {
        request('http://localhost:7865', (error, response, body) => {
            if (error) throw error;
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
    });