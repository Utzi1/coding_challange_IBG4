/*
 *
 */

// load all required modules
const express = require("express")
const routs = require("./routes.js")

// and create an app instance
const app = express()

// assign the variables port and base_url
var baseUrl = baseUrl = process.env.BASE_URL || ""
var port = port = process.env.PORT || 3333

// mount our base_url to at the routs
app.use(baseUrl, routs)

// bind and listen at specified port:
app.listen(port, () => {
  console.log(`localhost:${port}`)
})

// for debugging-purposes:
//console.log(`${baseUrl}`)
