#!/usr/bin/node

const idFilm = process.argv.slice(2)[0];
const films = 'https://swapi-api.hbtn.io/api/films/' + idFilm;
const request = require('request');

request(films, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let x = 0;
    const urlJSON = JSON.parse(body);
    while (urlJSON.characters[x]) {
      const chara = urlJSON.characters[x];
      request(chara, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const charJSON = JSON.parse(body);
          console.log(charJSON.name);
        }
      });
      x++;
    }
  }
});
