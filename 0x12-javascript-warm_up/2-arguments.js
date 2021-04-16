#!/usr/bin/node
// prints a message depending on number of args passed if 0 "No argument"
// if one arg "Argument found" otherwise "Arguments found"

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
