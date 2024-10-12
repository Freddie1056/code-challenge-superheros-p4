import React, { useState, useEffect } from 'react';
import { getHeroes, getPowers, getHeroPowers } from './services/api';

function App() {
    const [heroes, setHeroes] = useState([]);
    const [powers, setPowers] = useState([]);
    const [heroPowers, setHeroPowers] = useState([]);

    // Fetch heroes, powers, and hero powers when the component loads
    useEffect(() => {
        async function fetchData() {
            try {
                const heroesData = await getHeroes();
                const powersData = await getPowers();
                const heroPowersData = await getHeroPowers();
                
                setHeroes(heroesData);
                setPowers(powersData);
                setHeroPowers(heroPowersData);
            } catch (error) {
                console.error("Error fetching data", error);
            }
        }
        fetchData();
    }, []);

    return (
        <div className="App">
            <h1>Superheroes</h1>

            <h2>Heroes</h2>
            <ul>
                {heroes.map(hero => (
                    <li key={hero.id}>{hero.name}</li>
                ))}
            </ul>

            <h2>Powers</h2>
            <ul>
                {powers.map(power => (
                    <li key={power.id}>{power.name}</li>
                ))}
            </ul>

            <h2>Hero Powers</h2>
            <ul>
                {heroPowers.map(heroPower => (
                    <li key={heroPower.id}>{heroPower.hero.name} - {heroPower.power.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
