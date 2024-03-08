import React, { useState, useEffect } from "react";

import {
  Container,
  Paper,
  Typography,
  Grid,
  List,
  ListItem,
  ListItemText,
} from "@material-ui/core";
import GameCard from "../components/GameCard";
import { useNavigate } from "react-router-dom";
import { get } from "../Requests";
import { getPath, playerPath } from "../Paths";
import { loginPage } from "../RedirectPages";

export default function HomePage() {
  const navigate = useNavigate();

  if (!localStorage.getItem("authToken")) {
    navigate(loginPage);
  }

  var [player, setPlayer] = useState(null);

  useEffect(() => {
    const urlObj = {
      name: localStorage.getItem("username"),
    };
    get(getPath(playerPath, urlObj))
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setPlayer(data));
  }, []);

  if (!player) {
    return <p>Loading...</p>;
  }

  return (
    <Container className="root" maxWidth="md">
      <Paper className="paper" elevation={3}>
        <Typography variant="h3" align="center" id="welcome">
          Welcome <b>{player.name}</b>
        </Typography>

        <Grid container spacing={1} justifyContent="center" className="stats">
          <Grid item xs={12} sm={4}>
            <Typography variant="h6">Your Score:</Typography>
            <List>
              <ListItem>
                <ListItemText
                  primary={`First Place: ${player.score.first_place}`}
                />
              </ListItem>
              <ListItem>
                <ListItemText
                  primary={`Second Place: ${player.score.second_place}`}
                />
              </ListItem>
              <ListItem>
                <ListItemText
                  primary={`Third Place: ${player.score.third_place}`}
                />
              </ListItem>
            </List>
          </Grid>

          <Grid item xs={12} sm={4}>
            <Typography variant="h6">Your Games:</Typography>
            <List>
              <ListItem>
                <ListItemText
                  primary={`Created Games: ${player.score.created}`}
                />
              </ListItem>
              <ListItem>
                <ListItemText
                  primary={`All Games: ${player.score.all_games}`}
                />
              </ListItem>
            </List>
          </Grid>
        </Grid>
      </Paper>
      <Grid
        container
        elevation={player.my_games.length}
        className="gameCardContainer"
      >
        {player.my_games.map((game, index) => (
          <GameCard key={index} game={game} />
        ))}
      </Grid>
    </Container>
  );
}
