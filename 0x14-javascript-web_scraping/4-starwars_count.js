#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    let count = 0;
    for (const film of response.data.results) {
      for (const people of film.characters) {
        if (people.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(function (err) {
    console.log(err.response.status);
  });
