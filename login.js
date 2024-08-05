// src/Login.js
import React, { useState } from 'react';
import { redirect } from "react-router-dom";
import { Link } from 'react-router-dom';

const Login = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });
    const [data, setData] = useState([]);


    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        async function getProducts() {
            await fetch(`http://localhost:8000/register/`)
            .then(response => response.json())
            .then(response=>{
              const get = response.users


              const getUserName = get.map(each => each.userName)
              const getPassowrd = get.map(each => each.password)

              if(getUserName.includes(formData.username) && getPassowrd.includes(formData.password)){
                async function getTrains() {

                    await fetch('http://localhost:8000/trainsList/')
                    .then(response => response.json())
                    .then(response => {
                        const get = response.trainsList
                        setData(get)
                        
                    })
                    
                } 
                getTrains()
              }else{
                return redirect("/");
              }

            })
            return redirect("/");
          }

          setFormData({username: '' , password: ''})

          getProducts()
    };


    return (

        <div>
            <div>
                Login Page
            </div>
        <form onSubmit={handleSubmit}>
            <h1>Log In</h1>
            <input
                type="text"
                name="username"
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
            <button type="submit">Log In</button>
        </form>
        {data.length === 0 ? <p>To know Traina Availble , please Login with your accout or create account  :  <Link to="/">Log In</Link></p> :
        <ul>
            {data.map(each => (
                <li key = {each.id}>
                    <h1>Train Number : {each.id}</h1>
                <p>{each.Train_name}</p>
                <p>From </p>
                <p>{each.From_Station} - To - {each.To_station}</p>
                <p>{each.Depatured_Time_And_Date} -reaching time - {each.Arrival_Time_And_Date}</p>
                <p>Availble Seats : {each.seat_Capacity}</p>
                </li>
            ))}
        </ul>}


        </div>
    );
};

export default Login;
