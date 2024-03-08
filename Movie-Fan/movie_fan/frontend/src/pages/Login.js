import React, { useEffect, useState } from "react";
import { post } from "../Requests";

import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";
import { loginPath } from "../Paths";
import { homePage } from "../RedirectPages";

export default function Login({ setIsAuth }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      var responce = {};

      const loginObj = {
        username: username,
        password: password,
      };

      await post(loginPath, loginObj)
        .then((response) => response.json())
        .then((data) => (responce = data));

      const tokenRes = responce.token;
      const usernameRes = responce.username;

      if (tokenRes && usernameRes) {
        localStorage.setItem("authToken", tokenRes);
        localStorage.setItem("username", usernameRes);

        setIsAuth(localStorage.getItem("authToken"));
        navigate(homePage);
      } else {
        alert("wrong credentials");
      }
    } catch (error) {
      alert("Login failed:" + error);
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
          Login
        </Typography>
        <form className="form" onSubmit={handleLogin}>
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
            Login
          </Button>
        </form>
      </Paper>
    </Container>
  );
}
