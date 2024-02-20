#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films';
const characterId = 18;

const requestUrl = `${apiUrl}?search=${characterId}`;
request(requestUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const films = data.films || [];
  console.log(`${films.length}`);
});
