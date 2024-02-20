#!/usr/bin/node
const request = require('request');
const apiUrl = process.argvr[2];
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
