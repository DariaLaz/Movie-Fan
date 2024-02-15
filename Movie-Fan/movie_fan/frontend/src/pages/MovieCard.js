import { Button, Grid } from "@material-ui/core";
import React, { useEffect } from "react";
import { useState } from "react";
import { Typography } from "@material-ui/core";

export default function MovieCard({movie, setChoice}) {
  const [description, setDescription] = useState(movie.description.slice(0, 100) + "....");
  const [showMore, setShowMore] = useState(false);

  const handleShowMore = () => {
    setShowMore(!showMore);
  } 

  useEffect(() => {
    if (!showMore) {
      setDescription(movie.description.slice(0, 100));
    } else {
      setDescription(movie.description);
    }
  }, [showMore]);

  return (
    <Grid item xs={12} sm={5} className="movieCard" >
      <Typography variant="h6" align="center">
        <a href={movie.link}>{movie.title.slice(0, 30) + (movie.title.length > 30 ? "...." : " ")}</a>
      </Typography>
      <img src={movie.thumbnail} alt={movie.title}/>
      <br/>
      <Typography align="center">
        {description}
        <Button color="secondary" onClick={handleShowMore}>{showMore ? "Show Less" : "Show More"}</Button>
      </Typography>
      <Grid item xs={12} align="center">
        <Button variant="contained" color="primary" onClick={() => setChoice(movie)}>Select</Button>
      </Grid>
    </Grid>
  )
}