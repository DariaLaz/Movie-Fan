import { Button, Grid, Typography, TextField } from "@material-ui/core";
import React from "react";
import { useState } from "react";
import { Form, Link } from "react-router-dom";
import { useEffect } from "react";

export default function CategoryCard({category, setCategories}) {
    const [mode, setMode] = React.useState(category.mode);
    const [showMore, setShowMore] = useState(false);
    const [result, setResult] = useState("");
    const submition = []

    const handleShowMore = () => {
        setShowMore(!showMore);
    } 
   
    if (category.mode == 1) {
        (async () => {
            const response = await fetch(`/api/submition/?category_id=${category.id}`);

            const data = await response.json();

            for (let i = 0; i < data.length; i++) {
                submition.push(data[i].player.name)
            }

            if (submition.find(s => s == localStorage.getItem("username"))) {
                setMode(4);
            }
        })();
    }

    if (category.mode == 2) {
        (async () => {
            const response = await fetch(`/api/category/?category_id=${category.id}`);

            const data = await response.json();

            for (let i = 0; i < data.voters.length; i++) {
                submition.push(data.voters[i].name)

            }

            if (submition.find(s => s == localStorage.getItem("username"))) {
                setMode(5);
            }
        })();
    }

    if (category.mode == 3) {
        (async () => {
            const response = await fetch(`/api/category/?category_id=${category.id}`);

            const data = await response.json();

            for (let i = 0; i < data.submitions.length; i++) {
                submition.push({
                    movie: data.submitions[i].movie.title,
                    submittedBy: data.submitions[i].player.name,
                    points: data.submitions[i].points
                })
            }

            setResult(submition.map(s => s.movie + " - " + s.submittedBy + " - " + s.points).join('\n'))
        })();
    }

    if (submition) {
        useEffect(() => {
            if (!showMore) {
                setResult("");
            } else {
                console.log(submition.length)       
            }
        }, [showMore]);
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
                mode == 2 &&
                (
                    <Button component={Link} to={`/vote/${category.id}`} variant="contained" className="detailsBtn">Vote</Button>
                )
            }
            
            {
                mode == 5 &&
                (
                    <Button component={Link} to={`/vote/${category.id}`} variant="contained" className="detailsBtn" disabled>Vote</Button>
                )
            }

            {
                mode == 3 &&
                (
                    <Typography align="center">
                    {
                        showMore && result
                    }
                   
                    <br/>
                        <Button variant="contained" color="primary" onClick={handleShowMore}>{!showMore ? "Show Results" : "Hide Results"}</Button>
                    </Typography>

                )
            }
        </Grid>
    );
}
