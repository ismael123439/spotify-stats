# 🎵 Spotify Stats

A Flask web application to view your most listened artists and songs using the Spotify Web API with OAuth2 authentication.

## ✨ Features

- 🔐 OAuth2 authentication with Spotify
- 🎤 View your top artists across different time periods
- 🎵 View your top tracks across different time periods
- 📊 Interactive data visualization with Plotly
- 📱 Responsive web interface
- ⏰ Multiple time ranges: short-term, medium-term, and long-term

## 🛠️ Prerequisites

- Python 3.10+
- A Spotify account
- Spotify Developer Dashboard account

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/ismael123439/spotify-stats.git
cd spotify-stats
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Spotify Developer Setup

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create a new app
3. Copy your **Client ID** and **Client Secret**
4. Add the following Redirect URIs to your app settings:
   - `http://127.0.0.1:5000/callback`
   - `http://localhost:5000/callback`

### 2. Environment Variables

Create a `.env` file in the project root:

```env
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
REDIRECT_URI=http://127.0.0.1:5000/callback
```

⚠️ **Important**: Never commit the `.env` file to your repository!

## 🚀 Usage

### Start the application
```bash
python app.py
```

### Open in browser
Navigate to: `http://127.0.0.1:5000`

## 📍 API Endpoints

| Endpoint | Description | Parameters |
|----------|-------------|------------|
| `/` | Home page with login button | - |
| `/login` | Redirects to Spotify authorization | - |
| `/callback` | Handles OAuth callback and stores token | - |
| `/top-artists` | Shows top artists | `time_range` |
| `/top-tracks` | Shows top tracks | `time_range` |

### Time Range Options

- `short_term` - Last 4 weeks
- `medium_term` - Last 6 months  
- `long_term` - All time (years of data)

### Example URLs
```
/top-artists?time_range=short_term
/top-tracks?time_range=long_term
```

## 📁 Project Structure

```
spotify-stats/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (don't commit!)
├── README.md            # Project documentation
├── static/
│   └── css/
│       └── styles.css   # CSS styles
└── templates/
    ├── index.html       # Home page template
    ├── top_artists.html # Top artists page
    └── top_tracks.html  # Top tracks page
```

## 📋 Dependencies

```txt
Flask==2.3.3
requests==2.32.0
spotipy==2.25.1
python-dotenv==1.0.0
plotly==5.18.0
```

## 🔧 Troubleshooting

### Common Issues

**`redirect_uri_mismatch` error**
- Ensure the `REDIRECT_URI` in your `.env` file exactly matches one of the Redirect URIs configured in your Spotify app settings

**CSS not loading**
- Verify the CSS path in HTML templates uses: `{{ url_for('static', filename='css/styles.css') }}`
- Check that `styles.css` exists in `static/css/` directory

**Authorization issues**
- Double-check your Client ID and Client Secret in the `.env` file
- Ensure your Spotify app is not in development mode restrictions

## 📝 Important Notes

- Spotify's public API doesn't provide exact play counts, only ranking and metadata
- Session management uses Flask cookies - no database storage
- The application requires active internet connection to communicate with Spotify's API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Support

If you encounter any issues or have questions, please [open an issue](https://github.com/ismael123439/spotify-stats/issues) on GitHub.

---

Made with ❤️ and 🎵