const axios = require('axios');

async function fetchPosts() {
    try {
        const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
        return response.data; // Return the array of posts
    } catch (error) {
        console.error('Error fetching posts:', error.message);
        throw error;
    }
}

module.exports = { fetchPosts };
