import React from 'react'

const PokemonList = ({ pokemonList }) => {
  return (
    <div>
      <h1>Lista de Pokémon</h1>
      <ul>
        {pokemonList.map((pokemon, index) => (
          <li key={index}>
            <img
              src={pokemon.image || '/fallback.png'}
              alt={pokemon.name}
              onError={(e) => { e.target.src = '/fallback.png'; }}
              style={{ width: '100px' }}
            />
            <p>{pokemon.name}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default PokemonList
