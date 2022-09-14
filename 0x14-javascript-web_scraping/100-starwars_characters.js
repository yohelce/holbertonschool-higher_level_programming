#!/usr/bin/node
const axios = require('axios').default;
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(url.concat(movieId))
  .then(function (response) {
    for (const people of response.data.characters) {
      axios.get(people).then(function (response2) {
        console.log(response2.data.name);
      });
    }
  })
  .catch(function (err) {
    console.log(err.response.status);
  });
