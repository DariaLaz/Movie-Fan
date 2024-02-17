import { Button } from "@material-ui/core";
import React from "react";
import getCookie from "../helpers";
import { redirect, useNavigate } from "react-router-dom";

export default function Logout({ setIsAuth }) {
  const navigate = useNavigate();
  const handleLogout = async () => {
    try {
      const csrftoken = getCookie("csrftoken");
      await fetch("/api/logout/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrftoken,
        },
        body: "",
      });

      localStorage.removeItem("authToken");
      localStorage.removeItem("username");

      setIsAuth(localStorage.getItem("authToken"));

      navigate("/login");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  return <Button onClick={handleLogout}>Logout</Button>;
}
