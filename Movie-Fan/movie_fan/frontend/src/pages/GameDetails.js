import React, { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import { Container, Paper, Typography, Grid, Button } from '@material-ui/core';

export default function GameDetails() {
    // const {gameId} = useParams();
    // const [game, setGame] = useState(null);

    // console.log(gameId);

    // useEffect(() => {
    //     fetch(`/api/games/${gameId}`)
    //         .then(res => res.json())
    //         .then(game => setGame(game))
    //         .catch(err => console.log(err));
    // }, [gameId]);

    // if (!game) {
    //     return <p>Loading...</p>;
    // }
    const game = {
        name: "Name",
        description: "Description",
        categories: [
            {
                name: "Category 1",
                description: 'Description 1',
                mode: 1
            },
            {
                name: "Category 2",
                description: 'Description 2',
                isActive: false,
            },
            {
                name: "Category 3",
                description: 'Description 3',
                isActive: false,
            },
        ],
        participants: [
            {
                name: 'name1',
                score: {
                    first_place: 1,
                    second_place: 1,
                    third_place: 0,
                    all_games: 2,
                    created_games: 0
                },
            },
            {
                name: 'name2',
                score: {
                    first_place: 0,
                    second_place: 0,
                    third_place: 0,
                    all_games: 0,
                    created_games: 0
                },
            },
            {
                name: 'name3',
                score: {
                    first_place: 0,
                    second_place: 0,
                    third_place: 0,
                    all_games: 0,
                    created_games: 0
                },
            },
            {
                name: 'name4',
                score: {
                    first_place: 0,
                    second_place: 0,
                    third_place: 0,
                    all_games: 0,
                    created_games: 0
                },
            },
        ],
        results: {
            name1: 3,
            name2: 2,
            name3: 1,
            name4: 0
        }
    };

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