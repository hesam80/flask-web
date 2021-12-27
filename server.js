'use strict';

import express from 'express';
import { version } from 'process';


// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello World baby');
});


app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
console.log(`Version: ${version}`);