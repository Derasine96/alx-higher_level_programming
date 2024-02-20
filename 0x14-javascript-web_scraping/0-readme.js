#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const fileEncoding = 'utf8';

fs.readFile(fileName, fileEncoding, (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
