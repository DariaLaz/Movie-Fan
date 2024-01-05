import React, { Component, useState } from "react";
import {Grid, Typography, Button, TextField, Paper, Container} from "@material-ui/core";
import { Link } from "react-router-dom";
import getCookie from "../helpers.js"



export default function Join() {
    const [code, setCode] = useState("");

    const handleCodeChange = (e) => {
        const { value } = e.target;
        setCode(value);
    };

    const handleEnterGame = (e) => {
        const csrftoken = getCookie('csrftoken');
        (async () => {
            await fetch('/api/games/', 
            {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,},
                body: JSON.stringify({
                    code: code,
                    username: localStorage.getItem("username")
                })
            })
            .then(response => response.json()).then(data => console.log(data));
        })()
    }

    return (
        <Container className="root" maxWidth="md">
            <Paper className="paper">
            <Grid container spacing={1}>
                    <Grid item xs={12} align="center">
                    <Typography variant="h4" component="h4">
                        Join a Game
                    </Typography>
                    </Grid>
                    <Grid item xs={12} align="center">
                    <TextField
                        label="Code"
                        placeholder="Enter a Game Code"
                        variant="outlined"
                        onChange={handleCodeChange}
                    />
                    </Grid>
                    <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleEnterGame}
                    >
                        Enter Game
                    </Button>
                    </Grid>
                </Grid>
            </Paper>
        </Container>
    );
}