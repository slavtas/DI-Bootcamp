const fs = require('fs');

try{
    const data = fs.readFileSync('info', 'utf-8');
    console.log(JSON.parse(data));    
}
catch(e) {
    console.log(e);
}