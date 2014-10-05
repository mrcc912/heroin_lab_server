var routes = {};

function route(pathname, response, url, postData)
{
  console.log("routing " + pathname);
  if ( typeof routes[pathname] === 'function')
  {
    console.log("routing request for " + pathname);
    routes[pathname](url, response, postData);
  }
  else
  {
    console.log("No routing function found for " + pathname);
    response.writeHead(404, {"Content-Type": "text/plain"});
    response.write("404 Not found");
    response.end();
  }
}

// Register the callback for the given pathname (GET)
function get(pathname, callback)
{
  routes[pathname] = callback;
}

// Register the callback for the given pathname (POST)
// Functionally the same as get(), but it helps the user keep track of what is post or get
// when declaring these.
function post(pathname, callback)
{
  routes[pathname] = callback;
}


exports.route = route;
exports.get = get;