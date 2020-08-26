const express = require('express')
const app = express()
const path = require('path')
const port = 3000

app.all('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'website_view/index.html'))    
    
})

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`)
})