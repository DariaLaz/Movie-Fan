import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import { Container, Paper, Typography, Grid, Button } from '@material-ui/core';
import CategoryCard from "../components/CategotyCard";
import getCookie from "../helpers.js"


export default function GameDetails() {
    const navigate = useNavigate();

    if (!localStorage.getItem('authToken')) {
        navigate('/login');
    }
    
    const {gameId} = useParams();
    const [game, setGame] = useState(null);

    useEffect(() => {
        fetch(`/api/games/?game_id=${gameId}&username=${localStorage.getItem('username')}`)
            .then(response => {
                if (!response.ok) {
                    alert(`HTTP error! Status: ${response.status}`);
                    return;
                }
                return response.json();})
            .then(game => setGame(game))
            .catch(err => alert(err));
    }, [gameId]);

    if (!game) {
        return <p>Loading...</p>;
    }


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

        setGame({
            ...game,
            mode: 1
        })
    }

    const handleDeleteGame = async (e) => {
        e.preventDefault();
        
        const result = window.confirm("Confirm delete");
        if (!result) {
            return;
        } 
        const csrftoken = getCookie('csrftoken');

        const response = await fetch(`/api/games/`, {
            method: 'DELETE',
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
        navigate('/');
    }
    
    const getResult = () => {
        const result = []
        for (var res in game.results){
            result.push(res + " - " + game.results[res])
        }
        return result.join(" ")
    }

    return (
        <Container className="root" maxWidth="md">
            <Paper className="paper" elevation={4}>
                <Typography variant="h2" align="center">
                    {game.name}
                </Typography>
                <Typography variant="h6" align="center">
                    {game.description}
                </Typography>
                <Typography variant="h6" align="center">
                    {game.participants.length} participant(s)
                </Typography>

                {
                    game.mode === 2 &&
                    getResult()
                }

                {
                    game.mode === 0 &&
                    game.participants.length < 3 &&
                    game.host === localStorage.getItem('username') &&
                    <Button variant="contained"  className="detailsBtn" disabled>
                            Start Game
                    </Button>
                }

                {
                    game.mode === 0 &&
                    game.host === localStorage.getItem('username') &&
                    game.participants.length >= 3 &&
                    <Button variant="contained"  className="detailsBtn" onClick={handleStartGame}>
                            Start Game
                    </Button>
                }

                {
                    game.mode === 0 &&
                    game.host === localStorage.getItem('username') &&
                    <Button variant="contained" 
                    className="detailsBtn" onClick={handleDeleteGame}>
                            Delete Game
                    </Button>
                }

                {
                    game.mode === 0 &&
                    <Typography variant="h6" align="center">
                        Code: {game.code}
                    </Typography>
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