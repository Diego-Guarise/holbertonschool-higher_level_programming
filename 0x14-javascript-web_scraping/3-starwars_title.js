#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, res, body) {
  if (error) {
    console.log(error);
    return;
  }
  const text = JSON.parse(body);
  console.log(text.title);
});
