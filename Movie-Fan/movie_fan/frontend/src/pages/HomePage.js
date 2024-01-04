import React, { Component } from "react";
import GamePage from "./Game";
import MoviePage from "./Movie";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Container, Paper, Typography, Grid, List, ListItem, ListItemText } from "@material-ui/core";
import GameCard from "../components/GameCard";

export default function HomePage() {
    // var user = localStorage.getItem('user');
    var player = {
        name: 'John Doe',
        my_games: [
            {
                name: 'Game 1',
                description: 'This is game 1',
                categories: [
                    {
                        name: 'Category 1',
                        description: 'This is category 1'
                    },
                    {
                        name: 'Category 2',
                        description: 'This is category 2'
                    },
                    {
                        name: 'Category 3',
                        description: 'This is category 3'
                    }
                ]
            },
            {
                name: 'Game 2',
                description: 'This is game 2',
                categories: [
                    {
                        name: 'Category 1',
                        description: 'This is category 1'
                    },
                    {
                        name: 'Category 2',
                        description: 'This is category 2'
                    }
                ]
            },
            {
                name: 'Game 3',
                description: 'This is game 3',
                categories: [
                    {
                        name: 'Category 1',
                        description: 'This is category 1'
                    },
                    {
                        name: 'Category 2',
                        description: 'This is category 2'
                    },
                    {
                        name: 'Category 3',
                        description: 'This is category 3'
                    },
                    {
                        name: 'Category 4',
                        description: 'This is category 4'
                    }
                ]
            }
        ],
        score: {
            first_place: 1,
            second_place: 1,
            third_place: 0,
            all_games: 2,
            created_games: 0
        },
        created_on: '2021-04-01T00:00:00Z'

    }
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

            <Grid container spacing={1} justifyContent="center" elevation={player.my_games.length}>
                {player.my_games.map((game, index) => 
                <GameCard game={game} index={index}/>)}
                
            </Grid>

        </Container>
    );
}