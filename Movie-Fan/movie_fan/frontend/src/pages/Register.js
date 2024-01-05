import React, { Component, useState } from "react";
import getCookie from "../helpers";

export default function Register() {
    const [email, setEmail] = useState('')
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleRegister = async () => {
        try{
            var responce = {}
            const csrftoken = getCookie('csrftoken');
            await fetch('/api/register/', 
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,},
                body: JSON.stringify({
                    username: username,
                    password: password,
                    email: email
                })
            })
            .then(response => response.json()).then(data => responce = data);

            await fetch('/api/players/',
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,},
                body: JSON.stringify({
                    name: username
                })
            }).then(response => response.json()).then(data => console.log(data));
            console.log(responce)
    
        } catch (error) {
          console.error('Register failed:', error);
        }
      };


    return (
    <div>
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="username" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button onClick={handleRegister}>Login</button>
    </div>
    );
}
