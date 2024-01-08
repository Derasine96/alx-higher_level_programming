#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log('undefined is undefined');
} else if (!args[3]) {
  console.log(args[2] + ' is undefined');
} else {
  console.log(args[2] + ' is ' + args[3]);
}
