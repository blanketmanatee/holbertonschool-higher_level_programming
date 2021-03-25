#!/usr/bin/node
// prints a square where first arg is size of square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
