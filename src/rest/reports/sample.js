var app = require('express').Router();

app.get('/test', (req, res) => {
    res.send({
        status: true
    });
})

module.exports = app;