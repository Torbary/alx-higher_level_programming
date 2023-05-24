#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2]; // Read the movie ID from command line arguments
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`; // Construct the API URL

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach((characterUrl) => {
      request.get(characterUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error(charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.log(`Unable to fetch character: ${characterUrl}`);
        }
      });
    });
  } else {
    console.log('Unable to fetch movie');
  }
});
