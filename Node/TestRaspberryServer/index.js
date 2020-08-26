const app = require('express')()
const {exec} = require('child_process')
const path = require('path')
let port = 3000

exec('sudo python off.py')

app.get('/', (req, res) =>{
    res.sendFile(path.join(__dirname, 'website/index.html'))
})
app.post('/on', (req, res) =>{
    console.log('cum on')
    res.redirect('/')

    exec('sudo python on.py')

    res.end()
})
app.post('/off', (req, res) =>{
    console.log('cum off')
    res.redirect('/')

    exec('sudo python off.py')

    res.end()
})
app.listen(port, () =>{
    console.log(`Server is listening on http://localhost:${port}`)
})