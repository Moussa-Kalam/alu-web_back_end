const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    if (isNaN(id)) {
        console.log('id is not a number');
        res.sendStatus(404);
    } else {
        res.send(`Payment methods for cart ${req.params.id}`);
    }
});

app.listen(7865, () => {
    console.log('API available on localhost port 7865');
});