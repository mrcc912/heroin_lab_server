var router = require("./router.js");

function index(url, response)
{
  response.writeHead('200', {"Content-Type": "text/plain"});
  response.write("INDEX PAGE BITCH\n");
  response.end();
}

function login(url, response)
{

}

// Setting up the functions to be used and with which paths
router.get("/", index);
router.get("login", login);