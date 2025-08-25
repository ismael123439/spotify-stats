# Spotify Stats

App web en **Flask** para ver tus **artistas** y **canciones** más escuchadas usando la API de Spotify (OAuth2).

---

## Requisitos

- Python 3.10+
- Cuenta en [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)

---

## Instalación

```bash
git clone https://github.com/tu-usuario/spotify-stats.git
cd spotify-stats

python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
requirements.txt (el tuyo):

ini
Copiar
Editar
Flask==2.3.3
requests==2.32.0
spotipy==2.25.1
python-dotenv==1.0.0
plotly==5.18.0
Configuración en Spotify
Entra a Spotify Developer Dashboard y crea una app.

Copiá Client ID y Client Secret.

Agregá Redirect URIs (podés poner varias):

http://127.0.0.1:5000/callback

http://localhost:5000/callback

Si alguna vez cambiás la URL (por ejemplo otro puerto o dominio), agregala también en Redirect URIs de tu app de Spotify.

Variables de entorno
Creá un archivo .env en la raíz del proyecto con:

env
Copiar
Editar
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret
REDIRECT_URI=http://127.0.0.1:5000/callback
No subas .env al repositorio.

Ejecutar
bash
Copiar
Editar
python app.py
Abrí en el navegador:

cpp
Copiar
Editar
http://127.0.0.1:5000
Rutas
/ — Página de inicio (botón de login).

/login — Redirige a Spotify para autorizar.

/callback — Recibe el code y guarda el access_token en sesión.

/top-artists?time_range=<valor> — Artistas top.

/top-tracks?time_range=<valor> — Canciones top.

time_range admite:

short_term — última semana (aprox.)

medium_term — últimos 6 meses (aprox.)

long_term — todo el tiempo (histórico)

Ejemplos:

bash
Copiar
Editar
/top-artists?time_range=short_term
/top-tracks?time_range=long_term
Estructura del proyecto
bash
Copiar
Editar
spotify-stats/
├─ app.py
├─ requirements.txt
├─ .env                  # (no subir)
├─ README.md
├─ static/
│  └─ css/
│     └─ styles.css
└─ templates/
   ├─ index.html
   ├─ top_artists.html
   └─ top_tracks.html
En los HTML, el CSS se incluye así:

html
Copiar
Editar
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
Notas
Los datos de escucha exactos (reproducciones) no están disponibles vía API pública; Spotify devuelve ranking y metadatos, no el conteo de plays.

La sesión se maneja con cookies de Flask; no se guarda nada en base de datos.

Problemas comunes
redirect_uri_mismatch: la REDIRECT_URI de tu .env debe coincidir exactamente con una de las Redirect URIs configuradas en tu app de Spotify.

CSS no carga: verificá la ruta en el HTML (usar {{ url_for('static', filename='css/styles.css') }}) y que el archivo exista en static/css/styles.css.

makefile
Copiar
Editar
