// This simple express server will connect to the database

// load stuff that's used here
const express = require("express")

const { exec } = require('child_process')

// and create the express app
const app = express()
const port = 3000

// To send the Hello-World greetings:
app.get('/', (req, res ) => {
    res.send("Hello world")
})

// And listen to port to eventually print output
app.listen(port, () => {
    console.log("Server B listens to port " + port)
})

// use child_process to run shell script

// Sleep a little to sync stout-log to console
// with the one of server_A
const sleep = (millis) => {
  var stop = new Date().getTime();
  while (new Date().getTime() < stop + millis) {}
}
// Now sleep for three seconds
sleep(3000)

const scripPath = "ping_server_a.sh"
//
// Run a shell script
const myShellScript = exec(`sh ${scripPath}`, (error, stdout, stderr) => {
    if (error)
       console.error("Error:" + error.message)
    if (stderr)
       console.error("stderr:" + stderr)

   console.log("stdout:" + stdout)
})
