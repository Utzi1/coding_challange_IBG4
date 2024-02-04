/* Routes are defined here
 * foo responds Hello
 * bar responds World
 */

const express = require("express")

// create a router instance
const router = express.Router()

// for the foo-router:
router.get("/foo", (req, res) => {
    res.json({response: "Hello"})
})

// for the bar-router:
router.get("/bar", (req, res) => {
    res.json({response: "World"})
})

module.exports = router
