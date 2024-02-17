import { Button, Grid, Typography } from "@material-ui/core";
import React from "react";
import { Link } from "react-router-dom";

export default function GameCard({ game }) {
  return (
    <Grid item xs={12} sm={5} className="gameCard">
      <Typography component="h4" variant="h3">
        {game.name}
      </Typography>
      <Typography component="h4" variant="h5">
        {game.description}
      </Typography>
      <Button
        component={Link}
        to={`games/${game.id}`}
        variant="contained"
        className="detailsBtn"
      >
        Details
      </Button>
    </Grid>
  );
}
