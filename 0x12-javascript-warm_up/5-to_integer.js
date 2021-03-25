#!/usr/bin/node
// write a script that prints My number: <first argument converted in integer>
// if first arg can be converted to int. if it cannot print "Not a number"

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
