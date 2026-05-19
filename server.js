//import express framwork, Nodes built in paths and filesys module
const express = require('express');
const path = require('path');
const fs = require('fs')

//basic app
const app = express();

//define port microsergice will listen
const PORT = 3001;
//location store img
const IMAGES_DIR = path.join(__dirname, 'images');
const EXTENSIONS = ['.png', '.jpg','.jpeg','.gif','.JPG','.JPEG'];

//we send a name, look if name exists
app.get('/image', (req,res) => {
    const name = req.query.name;
    //if no name entered
    if (!name) {
        return res.status(400).json({ error: 'Missing required query paramter: name'});
    }

    let foundPath = null;
    for (const ext of EXTENSIONS) {
        const candidate = path.join(IMAGES_DIR, name + ext);
        if (fs.existsSync(candidate)) {
            foundPath = candidate;
            break;
        }
    }
//if no file found under name, return error
    if(!foundPath) {
        return res.status(404).json({ error: `No image found for the name: "${name}`});
    }
    res.sendFile(foundPath);
});

//server comfr message.
app.listen(PORT, () => {
    console.log(`Image microservice running on http://localhost:${PORT}`);
});