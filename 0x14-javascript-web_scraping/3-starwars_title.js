#!/usr/bin/node
const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films';
const specificId = process.argv[2];
const requestUrl = `${apiUrl}/${specificId}`;

request(requestUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Print title of movie
    const data = JSON.parse(body);
    console.log(`${data.title}`);
  }
});
