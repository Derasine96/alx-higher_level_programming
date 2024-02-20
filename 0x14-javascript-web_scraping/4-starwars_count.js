#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const count = JSON.parse(body).results.reduce((count, movie) => {
    return movie.characters.some(character => character.endsWith('/18/')) ? count + 1 : count;
  }, 0);
  console.log(count);
});
