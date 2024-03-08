import React, { useState } from "react";
import {
  Grid,
  Typography,
  Button,
  TextField,
  Paper,
  Container,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";
import { post } from "../Requests";
import { joinPath } from "../Paths";
import { gameDetailsPage, loginPage } from "../RedirectPages";

export default function Join() {
  const navigate = useNavigate();

  if (!localStorage.getItem("authToken")) {
    navigate(loginPage);
  }
  const [code, setCode] = useState("");

  const handleCodeChange = (e) => {
    const { value } = e.target;
    setCode(value);
  };

  const handleEnterGame = async (e) => {
    const joinObj = {
      code: code,
      username: localStorage.getItem("username"),
    };

    await post(joinPath, joinObj).then((response) => {
      if (response.ok) {
        response.json().then((data) => navigate(gameDetailsPage(data.id)));
      } else {
        alert("Invalid code");
      }
    });
  };

  return (
    <Container className="root" maxWidth="md">
      <Paper className="paper">
        <Grid container spacing={1}>
          <Grid item xs={12} align="center">
            <Typography variant="h4" component="h4">
              Join a Game
            </Typography>
          </Grid>
          <Grid item xs={12} align="center">
            <TextField
              label="Code"
              placeholder="Enter a Game Code"
              variant="outlined"
              onChange={handleCodeChange}
            />
          </Grid>
          <Grid item xs={12} align="center">
            <Button
              variant="contained"
              color="primary"
              onClick={handleEnterGame}
            >
              Enter Game
            </Button>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
}
