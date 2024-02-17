import React, { useEffect, useState } from "react";
import getCookie from "../helpers.js";
import {
  Container,
  Paper,
  Typography,
  TextField,
  Button,
  Grid,
} from "@material-ui/core";
import { useNavigate } from "react-router-dom";

export default function Login({ setIsAuth }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      var responce = {};
      const csrftoken = getCookie("csrftoken");

      await fetch("/api/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
          username: username,
          password: password,
        }),
      })
        .then((response) => response.json())
        .then((data) => (responce = data));

      const tokenRes = responce.token;
      const usernameRes = responce.username;

      if (tokenRes && usernameRes) {
        localStorage.setItem("authToken", tokenRes);
        localStorage.setItem("username", usernameRes);

        setIsAuth(localStorage.getItem("authToken"));
        navigate("/");
      } else {
        alert("wrong credentials");
      }
    } catch (error) {
      alert("Login failed:");
    }
  };

  if (localStorage.getItem("username")) {
    useEffect(() => {
      navigate("/");
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
