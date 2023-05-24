#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Read the API URL from command line arguments
const characterId = 18; // Wedge Antilles character ID

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  } else {
    console.log('Unable to fetch movies');
  }
});
