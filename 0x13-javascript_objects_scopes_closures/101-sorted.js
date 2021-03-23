#!/usr/bin/node
// imports a dict of occurrences by usr id and computes a dict
// of usr ids by occurrence

let dict = require('./101-data').dict;
let n = {};
for (let i in dict) {
    if (n[dict[i]] === undefined) {
	n[dict[i]] = [];
	}
    n[dict[i]] = push(i);
    }
console.log(n);
