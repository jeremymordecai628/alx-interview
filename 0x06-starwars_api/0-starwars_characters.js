#!/usr/bin/env node

const request = require('request');

// Get the Movie ID from the command-line arguments
const movieId = process.argv[2];
if (!movieId) {
    console.log("Please provide a Movie ID as an argument.");
    process.exit(1);
}

// Define the URL for the Star Wars API with the Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Request movie data from the API
request(url, (error, response, body) => {
    if (error) {
        console.error("Error fetching data:", error);
        return;
    }

    // Parse the response body
    const data = JSON.parse(body);

    // Check if the movie has a 'characters' list
    if (data.characters) {
        // Loop through each character URL
        data.characters.forEach(characterUrl => {
            // Make a request for each character
            request(characterUrl, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error("Error fetching character:", charError);
                    return;
                }

                // Parse and display the character name
                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
            });
        });
    } else {
        console.log("No characters found for this movie.");
    }
});
