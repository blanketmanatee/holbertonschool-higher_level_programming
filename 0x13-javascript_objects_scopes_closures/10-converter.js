#!/usr/bin/node
// converts a number from base 10 to another base passed as an arg

exports.converter = function (base) {
    return function mainConvert (num) {
	return num.toString(base);
	};
    };
