#!/usr/bin/node
const fs = require('fs');

const fileOne = fs.readFileSync(process.argv[2]);
const fileTwo = fs.readFileSync(process.argv[3]);

const destinationFile = process.argv[4];

fs.writeFile(destinationFile, fileOne + fileTwo);
