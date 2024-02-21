#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const filmId = 1;

function getFilmDetails (callback) {
  const handler = (error, response, body) => {
    if (!error && response.statusCode === 200) {
      callback(null, JSON.parse(body));
    } else {
      console.error(error);
      callback(error);
    }
  };
  request({ url: url + filmId, json: true }, handler);
}

function printCharactersName (data) {
  const characters = data.characters || [];
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
}

getFilmDetails((err, data) => {
  if (err) {
    console.error('Error occurred while fetching data.');
    return;
  }
  printCharactersName(data);
});
