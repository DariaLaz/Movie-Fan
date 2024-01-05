import { Button, Grid, Typography } from "@material-ui/core";
import React from "react";
import { Link } from "react-router-dom";

export default function CategoryCard({category}) {
    console.log(category);
    return (
        <Grid item xs={12} sm={10} className="categoryCard" >
            <Typography variant="h5" align="left">
                {category.name}
            </Typography>
            <Typography variant="h6" align="left">
                {category.description}
            </Typography>
            {category.mode == 1 &&
            (<Button component={Link} to={`games/${1}`} variant="contained" className="detailsBtn">Upload</Button>)
            }

            {category.mode == 2 &&
            (<Button component={Link} to={`games/${1}`} variant="contained" className="detailsBtn">Vote</Button>)
            }

            {category.mode == 0 &&
            (<Typography variant="h6" align="left">
                Not started yet!
            </Typography>)}
            
            {category.mode == 3 &&
            (<Button component={Link} to={`games/${1}`} variant="contained" className="detailsBtn">Results</Button>)
            }

            
            
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
