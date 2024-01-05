import React, { Component, useState } from "react";
import HomePage from "./HomePage";
import MoviePage from "./Movie";
import { BrowserRouter as Router, Routes, Route, Redirect } from "react-router-dom";
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
        <Router>
            <Routes>
                {/* {!isAuth && (<Redirect to='login/'/>)} */}
                
                <Route path="register/" element={<Register setIsAuth={setIsAuth} />} />
                <Route path="login/" element={<Login setIsAuth={setIsAuth}/>} />

                {!isAuth &&
                    (<Route path="*" element={<Login setIsAuth={setIsAuth}/>} />)}

                <Route path="/games/:gameId" element={<GameDetails />} />
                <Route path="movie/" element={<MoviePage />} />
                <Route path="create-game/" element={<CreateGame />} />
                <Route path="join/" element={<Join />} />
                <Route path="*" element={<HomePage />} />

                
            </Routes>
        </Router>
        </div>
    );
  
}

const root = ReactDOM.createRoot(document.getElementById('main'));
root.render(<App />);