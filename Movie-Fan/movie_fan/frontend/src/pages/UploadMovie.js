import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Container, Paper, Typography, TextField, Button, Grid } from '@material-ui/core';
import MovieCard from "./MovieCard";
import getCookie from "../helpers.js"

export default function UploadMovie() {
    const {categoryId} = useParams();
    const [category, setCategory] = useState(null);

    const [movieData, setMovieData] = useState(null);
    const [searchData, setSearchData] = useState(null);
    const [choice, setChoice] = useState(null);

    const navigate = useNavigate();

    useEffect(() => {
        fetch(`/api/category/?category_id=${categoryId}&username=${localStorage.getItem('username')}`)
            .then(response => {
                if (!response.ok) {
                    alert(`HTTP error! Status: ${response.status}`);
                    return;
                }
                return response.json();})
            .then(category => setCategory(category))
            .catch(err => alert(err));
    }, [categoryId]);

    if(choice) {
       (async () => {
            const csrftoken = getCookie('csrftoken');
            var id = -1;

            const obj = {
                title: choice.title,
                description: choice.description ? choice.description : "N/A",
                tumbnail: choice.thumbnail ? choice.thumbnail : "N/A",
                link: choice.link ? choice.link : "N/A",
                genre: choice.genre ? choice.genre : "N/A",
                rating: choice.rating,
            }

            await fetch(`/api/movies/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(obj)
            }).then(r => r.json()).then(d => id = (d.id));
            
            const requestBody = {
                username: localStorage.getItem("username"), 
                category_id: categoryId,
                movie_id: id
            }
            
            await fetch(`/api/submition/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(requestBody)
            })
            .then(res => res.json())
            .then(data => console.log(data))

            navigate(`/category/${categoryId}`);
        })();
        
    }

    if (!category) {
        return <p>Loading...</p>;
    }

    const handleInputChange = (e) => {
        const { name, value } = e.target;
          setSearchData(value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        await fetch(`/api/sarp_movie/?q=${searchData}`)
            .then(response => response.json()).then(data => setMovieData(data)); 
    }

    return (
    <Container className="root" maxWidth="md">
        <Paper className="paper" elevation={4}>
            <Typography variant="h5" align="center">
                Upload Movie
            </Typography>
            <form className="form" onSubmit={handleSubmit}>
                <TextField
                label="Search Movie By...."
                fullWidth
                name="name"
                onChange={handleInputChange}
                required
                margin="normal"
                />
                
                <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                >
                    Search
                </Button>
            </form>
            <Grid container spacing={1} justifyContent="center" className="stats">
                {movieData && movieData.movies.map((movie, index) => (
                    <MovieCard key={index} movie={movie} setChoice={setChoice}/>
                ))}
            </Grid>
        </Paper>
    </Container>
    );
}