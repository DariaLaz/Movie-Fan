import React from "react";
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { Container, Paper, Typography, TextField, Button, Grid } from '@material-ui/core';
import MovieCard from "./MovieCard";

export default function UploadMovie() {
    const {categoryId} = useParams();
    const [category, setCategory] = useState(null);

    const [movieData, setMovieData] = useState(null);
    const [searchData, setSearchData] = useState(null);
    const [choice, setChoice] = useState(null);



    useEffect(() => {
        fetch(`/api/category/?category_id=${categoryId}&username=${localStorage.getItem('username')}`)
            .then(response => {
                if (!response.ok) {
                    alert(`HTTP error! Status: ${response.status}`);
                    // navigate('/')
                    return;
                }
                return response.json();})
            .then(category => setCategory(category))
            .catch(err => alert(err));
    }, [categoryId]);

    if (!category) {
        return <p>Loading...</p>;
    }

    const handleInputChange = (e) => {
        const { name, value } = e.target;
          setSearchData(value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        await fetch(`/api/movie/?q=${searchData}`)
            .then(response => response.json()).then(data => setMovieData(data));        
        // navigate(`/game/${id}`);
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