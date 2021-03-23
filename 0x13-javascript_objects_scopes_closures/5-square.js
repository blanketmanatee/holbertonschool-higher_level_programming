#!/usr/bin/node
// new class Square that inherits from class Rectangle takes constructor size
// constructor of Rectangle called using super()

module.exports = class Square extends require('./4-rectangle') {
    constructor (size) {
	super (size, size);
	}
};
