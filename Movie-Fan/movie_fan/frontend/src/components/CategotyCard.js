import { Button, Grid, Typography, TextField } from "@material-ui/core";
import React from "react";
import { useState } from "react";
import { Form, Link } from "react-router-dom";

export default function CategoryCard({category, setCategories}) {
    const [uploadFormVisible, setUploadFormVisible] = React.useState(false);
    const [mode, setMode] = React.useState(category.mode);
    // const [mode, setMode] = React.useState(2)
    const [voteFormVisible, setVoteFormVisible] = React.useState(false);




    const handleSubmition = (e) => {
        e.preventDefault();
        // console.log("submitted");
        // setUploadFormVisible(false);
        // setMode(4);
    }

    const handleVoting = (e) => {

    }
    return (
        <Grid item xs={12} sm={10} className="categoryCard" >
            <Typography variant="h5" align="left">
                {category.name}
            </Typography>
            <Typography variant="h6" align="left">
                {category.description}
            </Typography>

            {/* Not started category */}
            {
                mode == 0 &&
                (<Typography variant="h6" align="left" color="textSecondary"> Not started yet!</Typography>)
            }
            
            {/* Upload Button */}
            {
                mode == 1 && 
                !uploadFormVisible &&
                (
                    <Button component={Link} to={`/upload/${category.id}`} variant="contained" className="detailsBtn">Upload</Button>
                )
            }
            
            {
                mode == 4 &&
                (
                    <Button variant="contained" className="detailsBtn" disabled>Upload</Button>
                )
            }
            
            
            
            {
                mode == 5 &&
                (
                    <Button variant="contained" className="detailsBtn" disabled>Vote</Button>
                )
            }

            
            
        </Grid>
        // <Grid item xs={12} sm={5} className="categoryCard" >
        //     <Typography component='h6' variant='h3'>
        //         {category.name}
        //     </Typography>
        //     <Typography component='p' variant='h5'>
        //         {category.description}
        //     </Typography>
        //     {/* <Button component={Link} to={`games/${game.id}`} variant="contained" className="detailsBtn">
        //         Details
        //     </Button> */}
        // </Grid>
    );
}
