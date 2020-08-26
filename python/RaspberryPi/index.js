const express = require('express')
const app = express()
let port = 3000


const {Device} = require('ps4-waker');

var ps4 = new Device();
//ps4.turnOn().then(() => ps4.close());
ps4.turnOn()
ps4.close()



// app.get('/', (req, res) => {

//     res.write('cum')
//     console.log('cum')

//     // const { spawn } = require('child_process')
//     // const py = spawn('python3', ['main.py'])

//     // py.stdout.on('data', (data) =>{
//     //     console.log(data.toString())
//     //     res.write(data)
//     // })
//      res.end()
// })

// app.get('/turn-on', (req, res) =>{
//     //var ps4 = new Device();
//     console.log('cum turned on')
//     res.end()
// })


// app.listen(port, () => {
//     console.log('Server is running on port ' + port)
// })