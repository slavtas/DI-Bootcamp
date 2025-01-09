const express = require('express');
const posts = require('./data.js');

const app = express();
const PORT = 5000;

app.use(express.json());

app.get("/api/posts", (req, res) => {
    res.json(posts);
});

app.get("/api/posts/:postID", (req, res) => {
    const postID = parseInt(req.params.postID);
    if (isNaN(postID)) {
        return res.status(400).json({ message: "Invalid post ID" });
    }

    const post = posts.find((p) => p.id === postID);
    if (post) {
        res.json(post);
    } else {
        res.status(404).json({ message: "Post not found" });
    }
});

app.get("/api/search", (req, res) => {
    const { title } = req.query;

    if (!title || !title.trim()) {
        return res.status(400).json({ message: "Query parameter 'title' is required and cannot be empty" });
    }

    const lowerCaseTitle = title.toLowerCase();
    const filteredPosts = posts.filter((post) =>
        post.title.toLowerCase().includes(lowerCaseTitle)
    );

    if (filteredPosts.length > 0) {
        res.json(filteredPosts);
    } else {
        res.status(404).json({ message: "No posts match your search" });
    }
});

app.post("/api/posts", (req, res) => {
    const { title, content } = req.body;

    if (!title || !content) {
        return res.status(400).json({ message: "Title and content are required" });
    }

    const newPost = {
        id: posts.length + 1,
        title,
        content,
    };

    posts.push(newPost);
    res.status(201).json(newPost);
});

app.put("/api/posts/:id", (req, res) => {
    const postID = parseInt(req.params.id);
    if (isNaN(postID)) {
        return res.status(400).json({ message: "Invalid post ID" });
    }

    const { title, content } = req.body;
    if (!title || !content) {
        return res.status(400).json({ message: "Title and content are required" });
    }

    const postIndex = posts.findIndex((p) => p.id === postID);
    if (postIndex !== -1) {
        posts[postIndex] = { id: postID, title, content };
        res.status(200).json({ message: "Post updated", post: posts[postIndex] });
    } else {
        res.status(404).json({ message: "Post not found" });
    }
});

app.delete("/api/posts/:id", (req, res) => {
    const postID = parseInt(req.params.id);
    if (isNaN(postID)) {
        return res.status(400).json({ message: "Invalid post ID" });
    }

    const postIndex = posts.findIndex((p) => p.id === postID);
    if (postIndex !== -1) {
        const deletedPost = posts.splice(postIndex, 1);
        res.status(200).json({ message: "Post deleted", post: deletedPost });
    } else {
        res.status(404).json({ message: "Post not found" });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
