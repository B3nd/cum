const ex = require('express')
const route = ex.Router()

route.use((req, res, next) =>{
    console.log('cum')
})

route.get('/', (req, res) =>{
    res.send('cum')
})

module.exports = route