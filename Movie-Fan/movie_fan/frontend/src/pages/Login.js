import React, { useState } from "react";
import getCookie from "../helpers.js"


export default function Login({setIsAuth}) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try{
        var responce = {}
        const csrftoken = getCookie('csrftoken');
        await fetch('/api/login/', 
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,},
            body: JSON.stringify({
                username: username,
                password: password,
            })
        })
        .then(response => response.json()).then(data => responce = data);
        console.log(responce)
        
        localStorage.setItem('authToken', responce.token);
        localStorage.setItem('username', responce.username);

        setIsAuth(localStorage.getItem('authToken'))

    } catch (error) {
      console.error('Login failed:', error);
    }
  };
    return (
        <div>
      <input type="username" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
    );
}