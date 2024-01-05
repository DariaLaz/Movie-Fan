import React, { Component, useState } from "react";
import HomePage from "./HomePage";
import GamePage from "./Game";
import MoviePage from "./Movie";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ReactDOM from 'react-dom/client';
import CreateGame from "./CreateGame";
import Join from "./JoinGame";
import Register from "./Register";
import Login from "./Login";
import GameDetails from "./GameDetails";
import Nav from "../components/Nav";

export default function App() {
    const [isAuth, setIsAuth] = useState(localStorage.getItem('authToken'))

    return (
        <div id='app'>
        <Nav isAuth={isAuth} setIsAuth={setIsAuth}/>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/games/:gameId" element={<GameDetails />} />
                <Route path="game/" element={<GamePage />} />
                <Route path="movie/" element={<MoviePage />} />
                <Route path="create-game/" element={<CreateGame />} />
                <Route path="join/" element={<Join />} />
                <Route path="register/" element={<Register setIsAuth={setIsAuth} />} />
                <Route path="login/" element={<Login setIsAuth={setIsAuth}/>} />
            </Routes>
        </BrowserRouter>
        </div>
    );
  
}

const root = ReactDOM.createRoot(document.getElementById('main'));
root.render(<App />);