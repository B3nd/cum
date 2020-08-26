const express = require('express')
const path = require('path')
const app = express()


app.use('/public', (express.static(path.join(__dirname, 'test'))))

const people = require('./routes/people')

app.use('/people', people);

// app.use('/', (req, res, next) =>{
//     req.cum = 'cum'
//     console.log(req.url, req.method)
//     next();
// })

// app.get('/', (req, res) =>{
//     res.write('cum')
//     console.log(req.cum)
// })

app.listen(3000)

console.log('Server is running on port 3000')