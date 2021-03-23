#!/usr/bin/node
// function that returns reversed list

exports.esrever = function (list) {
    let rev = [];
    for (let i = list.length - 1; i >= 0; i--) {
	rev.push(list[i]);
	}
    return rev;
};
