import React from "react";
import { AppBar, Toolbar, Typography, Link } from "@material-ui/core";
import Logout from "./Logout";

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
    );
}