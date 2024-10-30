const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 8080;

// Database connection
const db = new sqlite3.Database('./landmark_phuket.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
        console.error("Database connection failed:", err.message);
    } else {
        console.log("Connected to the SQLite database.");
    }
});

// Middleware
app.use(cors({ origin: '*' }));
app.use(express.json());

// Endpoint to get all landmarks data
app.get('/api/landmarks', (req, res) => {
    db.all('SELECT * FROM landmarks', [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
        } else {
            res.json({ data: rows });
        }
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});