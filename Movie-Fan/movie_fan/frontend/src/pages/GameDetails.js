import React, { useState, useEffect } from "react";
import { redirect, useParams, useNavigate } from 'react-router-dom';
import { Container, Paper, Typography, Grid, Button } from '@material-ui/core';
import CategoryCard from "../components/CategotyCard";
import getCookie from "../helpers.js"


export default function GameDetails() {
    const {gameId} = useParams();
    const navigate = useNavigate();
    const [game, setGame] = useState(null);

    useEffect(() => {
        fetch(`/api/games/?game_id=${gameId}&username=${localStorage.getItem('username')}`)
            .then(response => {
                if (!response.ok) {
                    alert(`HTTP error! Status: ${response.status}`);
                    // navigate('/')
                    return;
                }
                return response.json();})
            .then(game => setGame(game))
            .catch(err => alert(err));
    }, [gameId]);

    if (!game) {
        return <p>Loading...</p>;
    }
    console.log(game)

    const handleStartGame = async (e) => {
        e.preventDefault();
        const csrftoken = getCookie('csrftoken');

        const response = await fetch(`/api/games/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                game_id: gameId,
            })
        });
        if (!response.ok) {
            alert(`HTTP error! Status: ${response.status}`);
            return;
        }
    }

    return (
        <Container className="root" maxWidth="md">
            <Paper className="paper" elevation={3}>
                <Typography variant="h2" align="center">
                    {game.name}
                </Typography>
                <Typography variant="h6" align="center">
                    {game.description}
                </Typography>
                {
                    game.mode === 0 &&
                    game.host === localStorage.getItem('username') &&
                    <Button variant="contained" className="detailsBtn" onClick={handleStartGame}>
                        Start Game
                    </Button>
                }
                
            </Paper>
            <Grid container elevation={game.categories.length} className="categoryCardContainer">
                    {game.categories.map((category, index) => (
                        <CategoryCard category={category} key={index}/>
                    ))}
            </Grid> 
           
        </Container>

    );
}