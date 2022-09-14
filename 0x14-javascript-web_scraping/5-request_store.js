#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const url = process.argv[2];
const filename =  process.argv[3];

axios.get(url)
  .then(function (response) {
    fs.writeFile(filename, response.data, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (err) {
    console.log(err);
  });
