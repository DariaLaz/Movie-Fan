import React, { useState } from "react";
import { Container, Paper, Typography, TextField, Button, Grid } from '@material-ui/core';
import { Add  } from '@material-ui/icons';
import { useNavigate } from 'react-router-dom';

export default function CreateGame() {
  const navigate = useNavigate();
    const [gameData, setGameData] = useState({
      name: '',
      description: '',
      categories: [
        {
            name: '',
            description: '',
        },
        ]
    });
  
    const handleInputChange = (e, index) => {
      const { name, value } = e.target;
      if (name === 'categories') {
        const updatedCategories = [...gameData.categories];

        updatedCategories[index][e.target.id] = value;
        setGameData((prevData) => ({
          ...prevData,
          categories: updatedCategories,
        }));

      } else {
        setGameData((prevData) => ({
          ...prevData,
          [name]: value,
        }));
      }
    };
  
    const handleAddCategory = (e) => {
      setGameData((prevData) => ({
        ...prevData,
        categories: [
          ...prevData.categories,
          {
            name: '',
            description: '',
          },
        ],
      }));
    };

    const handleRemoveCategory = (e, index) => {
      const updatedCategories =  [...gameData.categories.slice(0, index), ...gameData.categories.slice(index + 1)]

      setGameData((prevData) => ({
          ...prevData,
          categories: updatedCategories
      }));
    };
  
    const handleSubmit = async (e) => {
        e.preventDefault();

        var updatedCategories = [];

        for (const category of gameData.categories) {
            await fetch('/api/category/', 
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(category)
            })
            .then(response => response.json()).then(data => updatedCategories.push(data.id));
        }

        const gameDataWithCategories = {
            name: gameData.name,
            description: gameData.description,
            categories: updatedCategories,
            host: localStorage.getItem('username')
        };

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(gameDataWithCategories)
        };

        var id = -1;
        await fetch('/api/games/', requestOptions).then(response => response.json()).then(data => id = data.id);

        navigate(`/games/${id}`);
    };
    
    return (
        <Container className="root" maxWidth="md">
          <Paper className="paper" elevation={4}>

            <Typography variant="h5" align="center">
              Create Game
            </Typography>

            <form className="form" onSubmit={handleSubmit}>
              <TextField
                label="Game Name"
                fullWidth
                name="name"
                value={gameData.name}
                onChange={handleInputChange}
                required
                margin="normal"
              />

              <TextField
                label="Game Description"
                fullWidth
                multiline
                name="description"
                value={gameData.description}
                onChange={handleInputChange}
                required
                margin="normal"
              />

              {gameData.categories.map((category, index) => (
                <Grid container spacing={1} key={index}>
                  <Grid item xs={12} sm={5}>
                    <TextField
                      label="Category Name"
                      fullWidth
                      id="name"
                      name="categories"
                      value={category.name}
                      onChange={(e) => handleInputChange(e, index)}
                      required
                      margin="normal"
                    />
                  </Grid>

                  <Grid item xs={12} sm={5}>
                    <TextField
                      label="Category Description"
                      fullWidth
                      id="description"
                      name="categories"
                      value={category.description}
                      onChange={(e) => handleInputChange(e, index)}
                      required
                      margin="normal"
                    />
                  </Grid>

                  <Button
                          color="default"
                          onClick={(e) => handleRemoveCategory(e, index)}
                          display="inline-flex"
                          margin="margin"
                          > Remove
                  </Button>
                </Grid>
                
              ))}

              <Button onClick={handleAddCategory} startIcon={<Add />}>
                    Add Category
              </Button>
              
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth>
                  Create Game
              </Button>
            </form>
          </Paper>
      </Container>
    );
}