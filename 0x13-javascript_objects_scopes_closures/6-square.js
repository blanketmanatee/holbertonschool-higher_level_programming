#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the
// rectangle using the character c
// If c is undefined, use the character X

module.exports = class Square extends require('./square') {
    charPrint (c) {
	if (c === undefined) {
	    c = 'X';
	    }

	for (let i = 0; i < this.height; i++) {
	    console.log(c.repeat(this.width));
	    }
	}
    };
