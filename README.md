
# Back-end Development Capstone

A Django concert-site project. The checked-in implementation uses Django templates and static files, with SQLite configured as its database. `requirements.txt` also lists Flask and other packages, but the Django application code and settings do not use Flask or MongoDB.

## Tech Stack

- Python
- Django (listed without a version pin in `requirements.txt`)
- SQLite (`db.sqlite3`, configured in `django_concert/settings.py`)
- Django templates and static assets

## Project Structure

- `manage.py`: Django management entry point
- `concert/`: views, URL patterns, models, forms, and migrations
- `django_concert/`: project settings and root URL configuration
- `templates/`: home, songs, photos, and other page templates
- `static/`: site assets
- `requirements.txt`: Python dependencies
- `requirements.txt`: Python dependencies
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

`concert/views.py` currently renders the home template in `index()`, but `songs()` and `photos()` contain only `pass`. They do not fetch or return data. The `requests` module is imported but not used, and there is no configured service URL or service-URL environment variable.

The templates are present: `songs.html` loops over a `songs` context value and includes a lyrics modal for each song; `photos.html` loops over a `photos` context value and displays each photo URL and event details. Since the views do not provide those values, the templates currently display no song titles or photos. Clicking a song title is the modal trigger in the template, but no title is currently rendered.

The root URL configuration maps `/` to the home view first. The named Songs and Photos URL patterns in `concert/urls.py` also use an empty path, so they do not define separate `/songs` or `/photos` pages; reversing their names points to `/`. The URL patterns do not currently provide working Songs or Photos pages.

## Related Repositories

- Songs: https://github.com/Awab7-ux/Back-End-Development-Songs
- Songs: https://github.com/Awab7-ux/Back-end-Development-Songs
- Pictures: https://github.com/Awab7-ux/Back-end-Development-Pictures

## Author

Awab Imad (Awab7-ux)
