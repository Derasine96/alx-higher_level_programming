#!/usr/bin/node

const num = process.argv;
const input1 = parseInt(num[2]);
const input2 = parseInt(num[3]);

function add (a, b) {
  return a + b;
}

const result = add(input1, input2);
console.log(result);
