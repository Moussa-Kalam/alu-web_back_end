const express = require('express');

const app = express();
app.use(express.json());

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

app.get('/available_payments', (req, res) => {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

app.post('/login', (req, res) => {
    console.log(req.body, '=======')
    const userName = req.body.userName;
    return res.send(`Welcome ${userName}`);
});


app.listen(7865, () => {
    console.log('API available on localhost port 7865');
});