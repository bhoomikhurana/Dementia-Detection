// LoginPage.js
import React, { useState } from 'react';
// import './LoginPage.css';
import Navbar from './Navbar';

function LoginPage({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Check if the entered username and password are correct
    if (username === 'admin' && password === '123') {
      // Call the onLogin function passed from the parent component (App.js in this case)
      onLogin();
    } else {
      // Handle incorrect login attempt
      alert('Invalid username or password');
    }
  };

  return (
    <>
    <Navbar/>
    <main id='main' className='flex py-32 pb-[219px] flex-col-reverse  justify-center items-center bg-customBlue overflow-hidden relative lg:flex-row'>
        <div className='flex flex-col gap-12 w-[80%] z-10 lg:w-[41%]'>
            <div>
                <p className='text-center font-bold text-5xl lg:text-left'>Login</p>
            </div>

            <div className=' self-center text-center  text-lg lg:text-left lg:self-start lg:w-[80%]'>
            <label>
        Username:
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      </label>

            </div>

            
            <div className=' self-center text-center  text-lg lg:text-left lg:self-start lg:w-[80%]'>
            <label>
        Password:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      
            </div>


            <button onClick={handleLogin} className='self-center lg:self-start bg-textBlue text-white font-bold w-32 p-2 rounded-2xl text-center hover:bg-sky-700 ease-in-out duration-500' href='/#feature'>Login</button>
        </div>
            
        <div className='z-10'>
            <img className=' h-[300px] w-[300px]' src="/brain.png" alt="" srcSet="" />
        </div>

        <div className="primary-color-border primary-color-[100] absolute -left-56 top-20 h-[400px] w-[400px] rounded-full border-[60px] border-blue-100 "></div>
        <div className="primary-color-border primary-color-[100] absolute -right-56 top-60 h-[400px] w-[400px] rounded-full border-[60px] border-blue-100 "></div>
    </main>
    </>
  );
}

export default LoginPage;

