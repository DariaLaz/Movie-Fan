import React, { useState } from "react";
import getCookie from "../helpers";
import { Container, Paper, Typography, TextField, Button } from '@material-ui/core';
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function Register() {
    const [email, setEmail] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const navigate = useNavigate()

    const handleRegister = async (e) => {
      e.preventDefault()
      try{
        var responce = {}
        const csrftoken = getCookie('csrftoken');
        await fetch('/api/register/', 
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,},
          body: JSON.stringify({
              username: username,
              password: password,
              email: email
          })
        })
        .then(response => response.json()).then(data => responce = data);
        await fetch('/api/players/',
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,},
          body: JSON.stringify({
              name: username
          })
        }).then(response => response.json());
        navigate('/login')
      } catch (error) {
        alert('Register failed:');
      }
  };

  if (localStorage.getItem("username")){
    useEffect(() => {
      navigate("/")
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
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          fullWidth
        >
            Register
        </Button>
      </form>
    </Paper>
  </Container>    
  );
}
