import React from "react";
import { useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { Container, Paper, Typography, Button, Grid } from "@material-ui/core";
import VoteCard from "../components/VoteCard.js";
import { useNavigate } from "react-router-dom";
import { put, get } from "../Requests.js";
import { categoryPath, getPath, submitionPath } from "../Paths.js";
import { gameDetailsPage, loginPage } from "../RedirectPages.js";

export default function Vote() {
  const navigate = useNavigate();

  if (!localStorage.getItem("authToken")) {
    navigate(loginPage);
  }

  const { categoryId } = useParams();
  const [category, setCategory] = useState(null);
  const [submitions, setSubmitions] = useState(null);
  const [ratings, setRatings] = useState({});

  const allPoints = 10;

  useEffect(() => {
    const urlObj = {
      category_id: categoryId,
      username: localStorage.getItem("username"),
    };
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

  useEffect(() => {
    const urlObj = {
      category_id: categoryId,
    };
    get(getPath(submitionPath, urlObj))
      .then((response) => {
        if (!response.ok) {
          alert(`HTTP error! Status: ${response.status}`);
          return;
        }
        return response.json();
      })
      .then((submitions) => setSubmitions(submitions))
      .catch((err) => alert(err));
  }, [categoryId]);

  const handleRatingChange = (submitionId, rating) => {
    setRatings((prevRatings) => ({
      ...prevRatings,
      [submitionId]: rating,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (
      Object.values(ratings).reduce((a, b) => a + parseInt(b), 0) !== allPoints
    ) {
      alert("Please rate all movies with 10 points");
      return;
    }
    if (Object.values(ratings).some((rating) => rating < -3 || rating > 10)) {
      alert("Please rate all movies between 0 and 10");
      return;
    }

    const urlObj = {
      category_id: categoryId,
      username: localStorage.getItem("username"),
    };

    await put(getPath(categoryPath, urlObj), ratings);

    navigate(gameDetailsPage(category.game_id));
  };

  return (
    <Container className="root" maxWidth="md">
      <Paper className="paper" elevation={4}>
        <Typography component="h1" variant="h2">
          Vote
        </Typography>
        <Typography component="h4" variant="h5">
          Vote for your favorite movie
        </Typography>
        <Grid>
          <form onSubmit={handleSubmit}>
            {submitions &&
              submitions.map((submition, index) => (
                <VoteCard
                  key={index}
                  submition={submition}
                  handleRatingChange={handleRatingChange}
                />
              ))}
            <Grid item xs={12} align="center">
              <Button
                type="submit"
                variant="contained"
                className="detailsBtn"
                color="primary"
                onClick={handleSubmit}
              >
                Submit
              </Button>
            </Grid>
          </form>
        </Grid>
      </Paper>
    </Container>
  );
}
