// src/Home.js
import React , { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Home = () => {
    const [formData, setFormData] = useState({
        userName: '',
        password: '',
        Email: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/register/', formData)
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Home Page</h1>
            <br />
            <Link to="/login">Log In</Link>

            <div>
                        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="userName"
                value={formData.username}
                onChange={handleChange}
                placeholder="Username"
                required
            />
            <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                placeholder="Password"
                required
            />
            <input
                type="email"
                name="Email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Email"
                required
            />
            <button type="submit">Register</button>
        </form>



            </div>


        </div>
    );
};

export default Home;
