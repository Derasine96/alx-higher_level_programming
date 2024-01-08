#!/usr/bin/node
const num = process.argv;
const input = parseInt(num[2]);
const factorial = function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

const result = factorial(input);
console.log(result);
