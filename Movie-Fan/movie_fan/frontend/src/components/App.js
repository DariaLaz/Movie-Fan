import React, { Component } from "react";
import HomePage from "./HomePage";
import GamePage from "./Game";
import MoviePage from "./Movie";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ReactDOM from 'react-dom/client';
import CreateGame from "./CreateGame";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="game/" element={<GamePage />} />
                <Route path="movie/" element={<MoviePage />} />
                <Route path="create-game/" element={<CreateGame />} />
            </Routes>
        </BrowserRouter>
    );
  
}

// const appDiv = document.getElementById("app");
// render(<App />, appDiv);
const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(<App />);