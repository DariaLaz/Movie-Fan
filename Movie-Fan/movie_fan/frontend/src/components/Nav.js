import React from "react";
import { AppBar, Toolbar, Typography, Button, IconButton, Link, MenuIcon  } from "@material-ui/core";
import Logout from "./Logout";
import { BrowserRouter } from 'react-router-dom';

export default function Nav({isAuth, setIsAuth}) {
    
    return (
    <AppBar position="static" className="navContainer">
      <Toolbar className="Nav">
        <Typography variant="h6">
          Movie-Fan
        </Typography>
        
        {!isAuth && (
            <div style={{ marginLeft: 'auto' }}>
              <Link href="\login" color="inherit" style={{ marginRight: '20px' }}>
                  LOGIN
                </Link>
              <Link href="\register" color="inherit" style={{ marginRight: '20px' }}>
                  REGISTER
              </Link>
            </div>
        )}
        {isAuth && (
          <div style={{ marginLeft: 'auto' }}>
          <Link href="/" color="inherit" style={{ marginRight: '20px' }}>
            Home
          </Link>
          <Link href="/create-game" color="inherit" style={{ marginRight: '20px' }}>
            Create game
          </Link>
          <Link href="/join" color="inherit" style={{ marginRight: '20px' }}>
            Join
          </Link>
          <Logout setIsAuth={setIsAuth}/>
        </div> 
        )}
        
      </Toolbar>
    </AppBar>
    //   <Toolbar className="Nav">
    //     <Typography variant="h6">MovieFan</Typography>
    //     <Grid container justify="flex-end">
    //       <Button >Home</Button>
    //       <Button >Create game</Button>
    //       <Button>Join game</Button>
    //     </Grid>
        
    //   </Toolbar>

        // <nav className="Nav">
            
        //     <ul>
        //         <li>bhjkjh</li>
        //         <li>rdsf</li>
        //         <li>rdsf</li>
        //         {isAuth && (
        //             <li><Logout setIsAuth={setIsAuth}/></li>
        //         )}
        //         {!isAuth && (
        //                 <li><Button>Login</Button></li>
        //         )}
        //          {!isAuth && (
        //                 <li><Button>Register</Button></li>
        //         )}

        //         {/* <li><Link to="/">Home</Link></li>*/}
        //     </ul>
        // </nav>
    );
}