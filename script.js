function searchMovies() {
    const options = {
        method: 'GET',
        headers: {
          accept: 'application/json',
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MDIyZGFjZDMyNzljZTkxYzYzM2YxMWMwNjljNDY1ZiIsInN1YiI6IjY0YzI1ZjFhMTNhMzIwMDBlMjFiMmI5OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GHy00vGrAtL1cUxB-3fl1YxhixXY2j7dhn0pOVTPRPw'
        }
      };
    var userInput = document.getElementById("searchInputMovies").value;
        const movieId = userInput; // Assuming the first result
    fetch(`https://api.themoviedb.org/3/search/movie?query=${movieId}` , options)
        .then(response => response.json())
        .then(movieData => {
            const posterPath = movieData.results[0].poster_path
            // Use the poster_path to set the background image
            const imageUrl = `https://image.tmdb.org/t/p/original${posterPath}`;
            document.body.style.backgroundImage = `url(${imageUrl})`;
            document.body.style.backgroundSize = 'contain';
            document.body.style.backgroundRepeat = 'no-repeat'
        })
        .catch(error => console.error("Error fetching MovieDB data:", error));

    // Make a POST request to the Flask API
    fetch("http://5.42.87.92:5000/search_movies", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "user_input": userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Display the results
        document.getElementById("resultsMovies").innerText = data.results;
    })
    .catch(error => console.error("Error:", error));
}

function searchSeries() {
    // Get user input
    var userInput = document.getElementById("searchInputTV").value;
    var userSeason = document.getElementById("searchInputSeason").value;
    // Make a POST request to the Flask API
    fetch("http://5.42.87.92:5000/search_series", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ "user_input": userInput , "season": userSeason })
    })
    .then(response => response.json())
    .then(data => {
        // Display the results
        document.getElementById("resultsTV").innerText = data.results;
    })
    .catch(error => console.error("Error:", error));
}
