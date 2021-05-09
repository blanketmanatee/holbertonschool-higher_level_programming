#!/usr/bin/node

require('request').get(process.argv[2], function (err, r, body) {
    if (err) {
	console.log(err);
	} else {
	    let counter = 0;
	    let data = JSON.parse(body).results;
	    for (let i = 0; i < data.length; i++) {
		if (data[i].characters[n].includes('/18/') {
		    counter++;
		    break;
		    }
		}
    console.log(counter);
    }
});
