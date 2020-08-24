import React from 'react';

function Movies() {
    const movies = [];

    return (
        <div>
            <h1>List of Movies - React</h1>
            {movies.map(movie => {
                return <h2 key={movie.id}>{movie.title}</h2>
            })}
        </div>
    )
}

export default Movies;