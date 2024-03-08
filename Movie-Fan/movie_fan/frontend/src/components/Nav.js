import React from "react";
import { AppBar, Toolbar, Typography, Link } from "@material-ui/core";
import Logout from "./Logout";
import {
  createGamePage,
  homePage,
  joinPage,
  loginPage,
  registerPage,
} from "../RedirectPages";

export default function Nav({ isAuth, setIsAuth }) {
  return (
    <AppBar position="static" className="navContainer">
      <Toolbar className="Nav">
        <Typography variant="h6">Movie-Fan</Typography>

        {!isAuth && (
          <div style={{ marginLeft: "auto" }}>
            <Link
              href={loginPage}
              color="inherit"
              style={{ marginRight: "20px" }}
            >
              LOGIN
            </Link>

            <Link
              href={registerPage}
              color="inherit"
              style={{ marginRight: "20px" }}
            >
              REGISTER
            </Link>
          </div>
        )}

        {isAuth && (
          <div style={{ marginLeft: "auto" }}>
            <Link
              href={homePage}
              color="inherit"
              style={{ marginRight: "20px" }}
            >
              Home
            </Link>

            <Link
              href={createGamePage}
              color="inherit"
              style={{ marginRight: "20px" }}
            >
              Create game
            </Link>

            <Link
              href={joinPage}
              color="inherit"
              style={{ marginRight: "20px" }}
            >
              Join
            </Link>

            <Logout setIsAuth={setIsAuth} />
          </div>
        )}
      </Toolbar>
    </AppBar>
  );
}
