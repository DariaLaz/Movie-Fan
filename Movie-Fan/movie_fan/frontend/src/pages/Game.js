import React, { useState } from "react";
// import Button from 'react-bootstrap/Button';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Container, Paper, Button } from '@material-ui/core';

export default function GamePage(){
    // game will be gotten from the backend
    const [game, setGame] = useState({
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
    });
    return (
        <Container className="root" maxWidth="md">
        <Paper className="paper" elevation={3}>
            <Typography component='h4' variant='h3'>
                {game.name}
            </Typography>
            <Typography component='h4' variant='h5'>
                {game.description}
            </Typography>
            <Grid container spacing={3}>
                {game.categories.map((category, index) => (
                    <Grid item xs={12} sm={6} key={index}>
                        <Typography component='h4' variant='h5'>
                            {category.name}
                        </Typography>
                        <Typography component='h4' variant='h5'>
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