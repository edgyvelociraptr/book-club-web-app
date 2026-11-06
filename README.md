# Little Bookclub App
My goals with this application is to help my little bookclub (and maybe others) run and schedule their meetings from one application. This application will be able to 1) choose the next group read 2) schedule meetings/formalize planning and 3) provide a forum to discuss as they read without having to worry about potential spoilers.

With our group it seems that a lot of the planning tends to utilize groups texts and just remembering. This can easily lead to issues as planning texts can easily get buried and people can easily forget what was said or set-up. Book suggestions can get buried, the voting process can be a bit scattered, the location or who is hosting can be forgotten, and members tend to read at different speeds and start at different times. The goal of this application is to give members a structures space for all of that information to live. 

## Installation
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

## Getting Started
To run the app:
```bash
docker-compose up
```

# License
Copyright (c) Mikayla Powell (2026)
