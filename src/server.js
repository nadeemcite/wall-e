var express = require('express');
var app = express();
const PORT = 8000;

app.listen(PORT,(err)=>{
    console.log(err || 'server running at ' + PORT);
});
