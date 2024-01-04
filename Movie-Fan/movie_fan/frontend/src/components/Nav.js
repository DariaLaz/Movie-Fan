import React from "react";
import { Link } from "react-router-dom";
import { Grid, Toolbar, Typography, Button } from "@material-ui/core";

export default function Nav() {
    return (
    //   <Toolbar className="Nav">
    //     <Typography variant="h6">MovieFan</Typography>
    //     <Grid container justify="flex-end">
    //       <Button component={Link} to="/" color="inherit">Home</Button>
    //       <Button component={Link} to="/create-game" color="inherit">Create game</Button>
    //       <Button component={Link} to="/join" color="inherit">Join game</Button>
    //     </Grid>
        
    //   </Toolbar>

        <nav className="Nav">
            
            <ul>
                <li>bhjkjh</li>
                <li>rdsf</li>
                <li>rdsf</li>

                {/* <li><Link to="/">Home</Link></li>*/}
            </ul>
        </nav>
    );
}