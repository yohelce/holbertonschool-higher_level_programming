#!/usr/bin/node
const url = process.argv[2];
const axios = require('axios').default;

axios.get(url)
  .then(function (response) {
    const userTask = {};
    for (const task of response.data) {
      if (task.completed === true) {
        if (userTask[task.userId] === undefined) {
          userTask[task.userId] = 1;
        } else {
          userTask[task.userId] += 1;
        }
      }
    }
    console.log(userTask);
  })
  .catch(function (err) {
    console.log(err.response.status);
  });
