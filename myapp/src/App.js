import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import useDarkMode from './useDarkMode';
function App() {
    const [currentTime, setCurrentTime] = useState(0);
    const [theme, toggleTheme] = useDarkMode();

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);
  return (
    <div className="App" >
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>theme is {theme}</p>
        <button type="button" onClick={toggleTheme}>Switch dark mode </button>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p style = {{
      color: theme ==='dark' ? 'rgb(174, 38, 38) ' : 'rgb(241, 232, 232)', 
      transition : '2s ease-in'
      _fontSize: 'calc(10px + 2vmin)',
      }}>The current time is {currentTime}.</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
