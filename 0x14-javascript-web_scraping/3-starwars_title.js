#!/usr/bin/node
const axios = require('axios').default;
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(url.concat(movieId))
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (err) {
    console.log(err.response.status);
  });
