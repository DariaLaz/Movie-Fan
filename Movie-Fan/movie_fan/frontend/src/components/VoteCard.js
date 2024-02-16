import { Grid, Typography } from "@material-ui/core";
import React from "react";
import { TextField } from "@material-ui/core";

export default function SubmitionCard({submition, handleRatingChange}) {
    return (
        <Grid item xs={12} sm={12}>
            <Typography variant="h5" align="center">
                <b>{submition.movie.title}</b>
            </Typography>
            <img src={submition.movie.thumbnail}/>
            { submition.player.name == localStorage.getItem("username") && <Typography variant="h6" align="center">You submitted this movie so you can't vote for it!</Typography>}
            {
                submition.player.name != localStorage.getItem("username") &&
                <Grid item xs={12} align="center">
                <TextField
                    id="outlined-number"
                    label="Rating"
                    type="number"
                    InputLabelProps={{
                        shrink: true,
                    }}
                    variant="outlined"
                    onChange={(e) => handleRatingChange(submition.id, e.target.value)}
                />
            </Grid>
            }
        </Grid> 
    );
}