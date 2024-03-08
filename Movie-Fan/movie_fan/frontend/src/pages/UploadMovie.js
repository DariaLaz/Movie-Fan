import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { post, get } from "../Requests";
import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
  Grid,
} from "@material-ui/core";
import MovieCard from "../components/MovieCard.js";
import { categoryPath, getPath, moviePath, sarpPath, submitionPath } from "../Paths.js";
import { homePage, loginPage } from "../RedirectPages.js";

export default function UploadMovie() {
  const navigate = useNavigate();

  if (!localStorage.getItem("authToken")) {
    navigate(loginPage);
  }
  const { categoryId } = useParams();
  const [category, setCategory] = useState(null);

  const [movieData, setMovieData] = useState(null);
  const [searchData, setSearchData] = useState(null);
  const [choice, setChoice] = useState(null);

  useEffect(() => {
    const urlObj = {
      category_id: categoryId,
      username: localStorage.getItem("username")
    }
    get(getPath(categoryPath, urlObj))
      .then((response) => {
        if (!response.ok) {
          alert(`HTTP error! Status: ${response.status}`);
          return;
        }
        return response.json();
      })
      .then((category) => setCategory(category))
      .catch((err) => alert(err));
  }, [categoryId]);

  if (choice) {
    var id = -1;

    (async () => {
      const postMovieObj = {
        title: choice.title,
        description: choice.description ? choice.description : "N/A",
        tumbnail: choice.thumbnail ? choice.thumbnail : "N/A",
        link: choice.link ? choice.link : "N/A",
        genre: choice.genre ? choice.genre : "N/A",
        rating: choice.rating,
      };

      await post(moviePath, postMovieObj)
        .then((r) => r.json())
        .then((d) => (id = d.id));

      const postSubmitionObj = {
        username: localStorage.getItem("username"),
        category_id: categoryId,
        movie_id: id,
      };

      await post(submitionPath, postSubmitionObj)
        .then((res) => res.json())
        .then((data) => console.log(data));
    })();
    navigate(homePage);
  }

  if (!category) {
    return <p>Loading...</p>;
  }

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setSearchData(value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const urlObj = {
      q: searchData,
    };

    await get(getPath(sarpPath, urlObj))
      .then((response) => response.json())
      .then((data) => setMovieData(data));
  };

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

          <Button type="submit" variant="contained" color="primary" fullWidth>
            Search
          </Button>
        </form>
        <Grid container spacing={1} justifyContent="center" className="stats">
          {movieData &&
            movieData.movies.map((movie, index) => (
              <MovieCard key={index} movie={movie} setChoice={setChoice} />
            ))}
        </Grid>
      </Paper>
    </Container>
  );
}
