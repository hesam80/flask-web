import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import useDarkMode from './useDarkMode';
function App() {
    const [currentTime, setCurrentTime] = useState(0);
    const [currentWeather, setCurrentWeather]=useState(0)
    const [theme, toggleTheme] = useDarkMode();

  useEffect(() => {
    fetch('/backend/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);
  useEffect(() => {
    fetch('/backend/weather').then(res => res.json()).then(data => {
      setCurrentWeather(data.currentWeather);
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
        <p>{currentWeather.base}</p>
        <p style = {{
      color: theme ==='dark' ? 'rgb(155, 255, 223) ' : 'rgb(241, 232, 232)', 
      transition : '2s ease-in',
      'font-size': theme ==='dark' ? 'calc(20px + 2vmin)' : 'calc(8px + 2vmin',
      }}>The current time is {currentTime}.</p>
        <a  className="App-link"
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
