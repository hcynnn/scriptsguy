const express = require('express');
const sgms = require('../sguyms.js');

const app = express();

const PORT = 3003;

app.get('/', (req, res) => {
  sgms.call_py(0, 'create_transparent_red_circle_window')
  res.send('hi, scripts-guy!');
});

app.listen(PORT, () => {
  console.log(`http://localhost:${PORT}`);
});
