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
    <div className="App" style = {{
      background: theme ==='dark' ? '#282c34' : '#eee',
      transition: '0.2s all'    }}>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>hello</p>
        <button type="button" onClick={toggleTheme}>Switch dark mode </button>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>The current time is {currentTime}.</p>
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
