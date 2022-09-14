#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;

axios.get(url)
  .then(function (response) {
    console.log('code:', response.status);
  })
  .catch(function (err) {
    console.log('code:', err.response.status);
  });
