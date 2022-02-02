#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, res, body) {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  const
  console.log(text.title);
});
