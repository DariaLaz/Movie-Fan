import { Grid, Typography } from "@material-ui/core";
import React from "react";

export default function GameCard(game) {
    return (
        <Grid item xs={12} sm={5} >
            <Typography component='h4' variant='h3'>
                {game.name}
            </Typography>
            <Typography component='h4' variant='h5'>
                {game.description}
            </Typography>
        </Grid>
    );
}
