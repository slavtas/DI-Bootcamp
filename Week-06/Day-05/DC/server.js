const express = require ('express');
const cors = require ('cors');
const {emojis} = require('./emojis/emojis');

const app = express();
app.use(cors());

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`run on ${PORT}`);
});

app.use('/', express.static(__dirname + '/public'));

const shuffleArray = (array) => {
    for(let i = array.length-1; i>0; i--){
        const j = Math.floor(Math.random() * (i+1));
        console.log('j', j);
        console.log([array[j],array[i]]);
        console.log([array[i],array[j]]);
        [array[i],array[j]] = [array[j],array[i]];
    }
    return array;
};

app.get('/emojis', (req,res) =>{
    const randomIndex = Math.floor(Math.random() * emojis.length);
    const randomEmoji = emojis[randomIndex];
    const shuffleEmojis = shuffleArray(emojis);
    res.json({randomEmoji, shuffleEmojis})
});
