import React, { Component, useState } from "react";
import HomePage from "./HomePage";
import { BrowserRouter as Router, Routes, Route, Redirect, useNavigate } from "react-router-dom";
import ReactDOM from 'react-dom/client';
import CreateGame from "./CreateGame";
import Join from "./JoinGame";
import Register from "./Register";
import Login from "./Login";
import GameDetails from "./GameDetails";
import Nav from "../components/Nav";
import UploadMovie from "./UploadMovie";
import Vote from "./Vote";

export default function App() {
    const [isAuth, setIsAuth] = useState(localStorage.getItem('authToken'))

    return (
        <div id='app'>
        
        <Router>
            <Nav isAuth={isAuth} setIsAuth={setIsAuth}/>
            <Routes>                
                <Route path="register/" element={<Register setIsAuth={setIsAuth} />} />
                <Route path="login/" element={<Login setIsAuth={setIsAuth}/>} />

                {!isAuth &&
                    (<Route path="*" element={<Login setIsAuth={setIsAuth}/>} />)}

                <Route path="/games/:gameId" element={<GameDetails />} />
                <Route path="/upload/:categoryId" element={<UploadMovie />} />
                <Route path="create-game/" element={<CreateGame />} />
                <Route path="join/" element={<Join />} />
                <Route path="*" element={<HomePage />} />
                <Route path="vote/:categoryId" element={<Vote />} />
            </Routes>
        </Router>
        </div>
    );
  
}

const root = ReactDOM.createRoot(document.getElementById('main'));
root.render(<App />);