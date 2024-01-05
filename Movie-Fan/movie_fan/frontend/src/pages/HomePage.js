import React, { Component } from "react";
// import GamePage from "./Game";
// import MoviePage from "./Movie";
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, Paper, Typography, Grid, List, ListItem, ListItemText } from "@material-ui/core";
import GameCard from "../components/GameCard";
import { redirect } from "react-router-dom";

export default function HomePage() {
    if(!localStorage.getItem('authToken')){
        redirect('/login')
    }

    var player = {}
        async function getPlayer() {
            await fetch('/api/players', 
            {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    username: localStorage.getItem('username')
                }).then(response => response.json())
                .then(data => player = data)
            })
        }

        getPlayer()

    return (
        <Container className="root" maxWidth="md">
            <Paper className="paper" elevation={3}>
                <Typography variant="h3" align="center" id="welcome">
                    Welcome <b>{player.name}</b>
                </Typography>
                <Grid container spacing={1} justifyContent="center" className="stats">
                    <Grid item xs={12} sm={4} >
                        <Typography variant="h6">Your Score:</Typography>
                        <List>
                            <ListItem>
                                <ListItemText primary={`First Place: ${player.score.first_place}`}/>
                            </ListItem>
                            <ListItem>
                                <ListItemText primary={`Second Place: ${player.score.second_place}`}/>
                            </ListItem>
                            <ListItem>
                                <ListItemText primary={`Third Place: ${player.score.third_place}`}/>
                            </ListItem>
                        </List>
                    </Grid>
                    <Grid item xs={12} sm={4}>
                        <Typography variant="h6">Your Games:</Typography>
                        <List>
                            <ListItem>
                                <ListItemText primary={`Created Games: ${player.score.created_games}`}/>
                            </ListItem>
                            <ListItem>
                                <ListItemText primary={`All Games: ${player.score.all_games}`}/>
                            </ListItem>
                        </List>
                    </Grid>
                </Grid>
            </Paper>
            <Grid container elevation={player.my_games.length} className="gameCardContainer">
                {player.my_games.map((game, index) =>
                <GameCard key={index} game={game}/>)}
            </Grid>
        </Container>
    );
}