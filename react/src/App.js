// src/App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [pokemons, setPokemons] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPokemons = async () => {
      try {
        const response = await axios.get('http://localhost:8080/pokemons/');
        console.log(response);
        setPokemons(response.data);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchPokemons();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error fetching data</p>;

  return (
    <div className="App">
      <h1>Pokémon List</h1>
      <ul>
        {pokemons.map(pokemon => (
          <li key={pokemon.pokedex_number}>
            <h2>{pokemon.name}</h2>
            <p>Primary Type: {pokemon.primary_type}</p>
            <p>Secondary Type: {pokemon.secondary_type}</p>
            <img src={pokemon.image_url} alt={pokemon.name} />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
