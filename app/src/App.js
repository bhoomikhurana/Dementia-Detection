// App.js
import React, { useState } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import Main from "./components/Main/Main";
import Feature from "./components/Feature";
import Contact from "./components/Contact";
import LoginPage from "./components/LoginPage";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  const handleLogin = () => {
    // Set the login state to true when the user successfully logs in
    setLoggedIn(true);
  };

  return (
    <>
      {loggedIn ? (
        <>
          <Navbar />
          <Main />
          <Feature />
          <Contact />
        </>
      ) : (
        <LoginPage onLogin={handleLogin} />
      )}
    </>
  );
}

export default App;
