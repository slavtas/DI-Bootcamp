const express = require('express');
const { fetchPosts } = require('./data/dataService');
const app = express();
const PORT = 5000;

app.get('/api/posts', async (req, res) => {
    try {
        const posts = await fetchPosts();
        console.log('Data retrieved successfully.');
        res.json(posts); // Respond with the fetched posts
    } catch (error) {
        res.status(500).json({ message: 'Error fetching posts', error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
