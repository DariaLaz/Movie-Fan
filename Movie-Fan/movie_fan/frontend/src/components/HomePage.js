import React, { Component } from "react";
import GamePage from "./Game";
import MoviePage from "./Movie";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <p>Home</p>
        );
    }
}