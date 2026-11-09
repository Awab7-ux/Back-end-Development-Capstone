
# Back-end Development Capstone

A Django concert-site project. The checked-in implementation uses Django templates and static files, with SQLite configured as its database. `requirements.txt` also lists Flask and other packages, but the Django application code and settings do not use Flask or MongoDB.

## Tech Stack

- Python
- Django (listed without a version pin in `requirements.txt`)
- SQLite (`db.sqlite3`, configured in `django_concert/settings.py`)
- Django templates and static assets
- Requests (HTTP client used by the Songs and Photos views)

## Project Structure

- `manage.py`: Django management entry point
- `concert/`: views, URL patterns, models, forms, and migrations
- `django_concert/`: project settings and root URL configuration
- `templates/`: home, songs, photos, and other page templates
- `static/`: site assets
- `requirements.txt`: Python dependencies
- `concert/migrations/`: generated Django migrations
- `Dockerfile` and `deployment.yml`: incomplete templates containing placeholders

## Run Locally

From the repository root:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open `http://127.0.0.1:8000/` for the home page.

## Songs and Photos Status

The home page is at `/`. The Songs page is at `/songs/`; it fetches JSON with `requests.get(...).json()` and renders each song's title and lyrics from `songs.html`. Click a song title to open its lyrics modal. The Photos page is at `/photos/`; it fetches JSON and renders each `photo.pic_url`, event date, city, and state from `photos.html`.

By default, the Songs page reads `https://raw.githubusercontent.com/captainfedoraskillup/private-get-songs/main/backend/data/songs.json`, and the Photos page reads `https://raw.githubusercontent.com/captainfedoraskillup/private-get-pictures/main/backend/data/pictures.json`. Override these defaults with the `SONGS_API_URL` and `PHOTOS_API_URL` environment variables, respectively.

## Related Repositories

- Songs: https://github.com/Awab7-ux/Back-end-Development-Songs
- Pictures: https://github.com/Awab7-ux/Back-end-Development-Pictures

## Author

Awab Imad (Awab7-ux)
