import React, { useState } from "react";
import { post } from "../Requests";
import { playerPath, registerPath } from "../Paths";

import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";
import { homePage, loginPage } from "../RedirectPages";

export default function Register() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      var responce = {};

      const registerObj = {
        username: username,
        password: password,
        email: email,
      };

      await post(registerPath, registerObj)
        .then((response) => response.json())
        .then((data) => (responce = data));

      const postPlayerObj = {
        name: username,
      };

      await post(playerPath, postPlayerObj).then((response) => response.json());

      navigate(loginPage);
    } catch (error) {
      alert("Register failed:" + error);
    }
  };

  if (localStorage.getItem("username")) {
    useEffect(() => {
      navigate(homePage);
    });
  }

  return (
    <Container className="root" maxWidth="md">
      <Paper className="paper" elevation={4}>
        <Typography variant="h5" align="center">
          Register
        </Typography>
        <form className="form" onSubmit={handleRegister}>
          <TextField
            label="email"
            fullWidth
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            margin="normal"
          />
          <TextField
            label="username"
            fullWidth
            name="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            margin="normal"
          />
          <TextField
            label="password"
            fullWidth
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            margin="normal"
            type="password"
          />
          <Button type="submit" variant="contained" color="primary" fullWidth>
            Register
          </Button>
        </form>
      </Paper>
    </Container>
  );
}
