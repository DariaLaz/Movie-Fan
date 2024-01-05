import React from "react";
import { Link } from "react-router-dom";
import { Grid, Toolbar, Typography, Button } from "@material-ui/core";
import Logout from "./Logout";

export default function Nav({isAuth, setIsAuth}) {
    
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
                {isAuth && (
                    <li><Logout setIsAuth={setIsAuth}/></li>
                )}
                {!isAuth && (
                        <li><Button>Login</Button></li>
                )}
                 {!isAuth && (
                        <li><Button>Register</Button></li>
                )}

                {/* <li><Link to="/">Home</Link></li>*/}
            </ul>
        </nav>
    );
}