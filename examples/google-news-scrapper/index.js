'use strict';

const { metacall, metacall_load_from_file } = require('metacall');

metacall_load_from_file('py', [ 'main.py']);

// console.log(metacall('get_google_news_result', 'bitcoin'));

const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send(req.query.term ?
    metacall('get_google_news_result', req.query.term) :
    'Invalid term'));

app.listen(port, () => console.log(`Listening on port ${port}`));
