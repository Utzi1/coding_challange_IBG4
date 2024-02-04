// This simple express server will connect to the database

// load stuff that's used here
const express = require("express")
const mysql = require("mysql2")

// and create the express app
const app = express()

// and use port 8000:
const port = 8000

// For the connection to our database:
const connection = mysql.createConnection({
   host: "db",
   user: "root",
   password: "start123",
   database: "database"
})

// and eventually establish the connection
connection.connect(error => {
   // for debugging purposes
   if (error)
      console.log("Error connecting to DB:" + error)
   else
      console.log(" ")
})
// At first we include a little delay as the mysql db
// needs a little time to start up therefor we let the
// script sleep for a little time
const sleep = (millis) => {
  var stop = new Date().getTime();
  while (new Date().getTime() < stop + millis) {}
}
// Now sleep for three seconds
sleep(3000)

// and start the server
app.listen(port, (error) => {
   // for debugging-purposes:
   if (!error)
      console.log("Up and running! Listening on port " + port)
   else
      console.log("Error:" + error)
})

// use child_process to run shell script to check the connection to db
const {
   exec
} = require('child_process');

// Run the shell script checking for database beeing ready
const myShellScript = exec("sh check_A_connection_to_DB.sh", (error, stdout, stderr) => {
   console.log("stdout:" + stdout)
})
