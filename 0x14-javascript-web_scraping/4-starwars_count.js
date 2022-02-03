#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, res, body) {
  if (error) {
    console.log(error);
    return;
  }
  const films = JSON.parse(body).results;
  const id = 18;
  let count = 0;
  for (const tmp in films) {
    const links = films[tmp].characters;
    for (const compare in links) {
      if (links[compare].includes(id)) {
        count++;
      }
    }
  }
  console.log(count);
});
