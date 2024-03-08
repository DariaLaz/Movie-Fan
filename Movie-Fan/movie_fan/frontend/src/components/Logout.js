import { Button } from "@material-ui/core";
import React from "react";
import { useNavigate } from "react-router-dom";
import { post } from "../Requests";
import { logoutPath } from "../Paths";
import { loginPage } from "../RedirectPages";

export default function Logout({ setIsAuth }) {
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      await post(logoutPath, "");

      localStorage.removeItem("authToken");
      localStorage.removeItem("username");

      setIsAuth(localStorage.getItem("authToken"));

      navigate(loginPage);
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  return <Button onClick={handleLogout}>Logout</Button>;
}
