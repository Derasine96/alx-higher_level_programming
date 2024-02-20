#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
const fileEncoding = 'utf8';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(fileName, body, fileEncoding, (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`File ${fileName} has been saved.`);
      }
    });
  } else {
    console.error('Unexpected response status code');
  }
});
