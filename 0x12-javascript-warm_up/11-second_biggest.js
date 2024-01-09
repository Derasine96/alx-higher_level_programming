#!/usr/bin/node
const num = process.argv.slice(2).map(Number);

let max = 0;
let secondMax = 0;

if (num.length <= 3) {
  console.log('0');
} else {
  for (let i = 0; i < num.length; i++) {
    if (num[i] > max) {
      secondMax = max;
      max = num[i];
    } else if (num[i] > secondMax && num[i] < max) {
      secondMax = num[i];
    }
  }

  console.log(secondMax);
}
