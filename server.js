var http = require('http');
var url = require('url');
var handler = require("./handler.js");
var mongo = require("./mongo");
var querystring = require('querystring');


var PORT = 8080;

function start(route)
{
  function handleRequest(request, response)
  {
    var parsedURL = url.parse(request.url);
    var pathname = parsedURL.pathname;

    console.log("recieved request for pathname: " + pathname);

    var fullPostData = "";

    request.addListener("data", function(data){
      fullPostData += data;
      console.log("POST data: " + data);
    });

    request.addListener("end", function(data){
      fullPostData += data;
      route(pathname, response, parsedURL, fullPostData);
    });

  }

  var server = http.createServer(handleRequest).listen(PORT);
  console.log("Starting the server on port " + PORT);
}

exports.start = start;