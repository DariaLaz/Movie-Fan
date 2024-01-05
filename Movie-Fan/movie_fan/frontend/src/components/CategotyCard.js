import { Button, Grid, Typography, TextField } from "@material-ui/core";
import React from "react";
import { Form, Link } from "react-router-dom";

export default function CategoryCard({category}) {
    const [uploadFormVisible, setUploadFormVisible] = React.useState(false);
    // const [mode, setMode] = React.useState(category.mode);
    const [mode, setMode] = React.useState(2)
    const [voteFormVisible, setVoteFormVisible] = React.useState(false);


    const handleSubmition = (e) => {
        e.preventDefault();
        console.log("submitted");
        setUploadFormVisible(false);
        setMode(4);
    }

    return (
        <Grid item xs={12} sm={10} className="categoryCard" >
            <Typography variant="h5" align="left">
                {category.name}
            </Typography>
            <Typography variant="h6" align="left">
                {category.description}
            </Typography>

            {/* Not started category */}
            {
                mode == 0 &&
                (<Typography variant="h6" align="left" color="textSecondary"> Not started yet!</Typography>)
            }
            
            {/* Upload Button */}
            {
                mode == 1 && 
                !uploadFormVisible &&
                (
                    <Button variant="contained" className="detailsBtn" onClick={() => setUploadFormVisible(true)}>Upload</Button>
                )
            }
            {
                mode == 4 &&
                (
                    <Button variant="contained" className="detailsBtn" disabled>Upload</Button>
                )
            }
            
            {/* Upload form */}
            {
                uploadFormVisible &&
                <Grid container spacing={1}>
                    <Grid item xs={12} align="center">
                        <TextField
                            label="Movie name"
                            placeholder="Enter a Movie"
                            variant="outlined"
                        />
                    </Grid>
                    <Grid item xs={12} align="center">
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleSubmition}
                        >
                            Upload
                        </Button>
                    </Grid>
                </Grid> 
            }

            {/* Upload Button */}
            {
                mode == 2 && 
                !voteFormVisible &&
                (
                    <Button variant="contained" className="detailsBtn" onClick={() => setVoteFormVisible(true)}>Vote</Button>
                )
            }
            {
                mode == 5 &&
                (
                    <Button variant="contained" className="detailsBtn" disabled><Vote></Vote></Button>
                )
            }
               {/* <Grid item xs={12} align="center">
                    <TextField
                        label="Code"
                        placeholder="Enter a Game Code"
                        variant="outlined"
                    />
                    </Grid>
                    <Grid item xs={12} align="center">
                    <Button
                        variant="contained"gory1
sdhfbvz
                        color="primary"
                    >
                        Enter Game
                    </Button>
                </Grid>*/}
            

            {/* {category.mode == 2 || category.mode == 4 &&
            (<Button disabled={category.mode == 4} onClick={() => setVoteFormVisible(true)}>Vote</Button>)
            }

            
            
            {category.mode == 3 &&
            (<Button component={Link} to={`games/${1}`} variant="contained" className="detailsBtn">Results</Button>)
            } */}

            
            
        </Grid>
        // <Grid item xs={12} sm={5} className="categoryCard" >
        //     <Typography component='h6' variant='h3'>
        //         {category.name}
        //     </Typography>
        //     <Typography component='p' variant='h5'>
        //         {category.description}
        //     </Typography>
        //     {/* <Button component={Link} to={`games/${game.id}`} variant="contained" className="detailsBtn">
        //         Details
        //     </Button> */}
        // </Grid>
    );
}
