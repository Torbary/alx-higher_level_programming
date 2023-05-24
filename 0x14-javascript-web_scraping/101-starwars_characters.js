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
    const characterUrls = movie.characters;

    // Function to fetch and print character name
    const fetchCharacterName = (url) => {
      request.get(url, function (charError, charResponse, charBody) {
        if (charError) {
          console.error(charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.log(`Unable to fetch character: ${url}`);
        }
      });
    };

    // Fetch and print character names in the same order as characterUrls
    characterUrls.forEach((url) => {
      fetchCharacterName(url);
    });
  } else {
    console.log('Unable to fetch movie');
  }
});
