#!/usr/bin/node
const num = process.argv;
const input = parseInt(num[2]);
if (!isNaN(input)) {
  console.log('My number: ' + input);
} else {
  console.log('Not a number');
}
