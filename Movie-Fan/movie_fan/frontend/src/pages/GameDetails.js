import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import { Container, Paper, Typography, Grid, Button } from '@material-ui/core';

export default function GameDetails() {
    const {gameId} = useParams();
    const [game, setGame] = useState(null);

    console.log(gameId);

    useEffect(() => {
        fetch(`/api/games/${gameId}`)
            .then(res => res.json())
            .then(game => setGame(game))
            .catch(err => console.log(err));
    }, [gameId]);

    if (!game) {
        return <p>Loading...</p>;
    }

    
    console.log(game);
    return (
        <Container className="root" maxWidth="md">
            <Paper className="paper" elevation={3}>
                <Typography variant="h5" align="center">
                    {game.name}
                </Typography>
                <Typography variant="h5" align="center">
                    {game.description}
                </Typography>
                <Grid container spacing={3}>
                    {game.categories.map((category, index) => (
                        <Grid item xs={12} sm={6} key={index}>
                            <Typography variant="h5" align="center">
                                {category.name}
                            </Typography>
                            <Typography variant="h5" align="center">
                                {category.description}
                            </Typography>
                            <Button>
                                Upload
                            </Button>
                            <Button>
                                Vote
                            </Button>
                            <Button>
                                See Results
                            </Button>
                        </Grid>
                    ))}
                </Grid>
            </Paper>
        </Container>

    );
}