#!/usr/bin/node
// prints first arg passed to it if no args pass "No argument"

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
