#!/usr/bin/node
const fs = require('fs');
const fileEncoding = 'utf8';
const fileName = process.argv[2];
const textToWrite = process.argv[3];

fs.writeFile(fileName, textToWrite, fileEncoding, (err) => {
  if (err) {
    console.error(err);
  }
});
