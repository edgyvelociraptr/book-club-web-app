# Little Bookclub App
My goals with this application are to help my little bookclub (and maybe others) run and schedule their meetings from one application. This application will be able to 1) choose the next group read 2) schedule meetings/formalize planning and 3) provide a forum to discuss as they read without having to worry about potential spoilers.

With our group it seems that a lot of the planning tends to utilize groups texts and just remembering. This can easily lead to issues as planning texts can easily get buried and people can easily forget what was said or set-up. Book suggestions can get buried, the voting process can be a bit scattered, the location or who is hosting can be forgotten, and members tend to read at different speeds and start at different times. The goal of this application is to give members a structured space for all of that information to live. 

## Installation
```bash
docker-compose build
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
```

## Getting Started
To run the app:
```bash
docker-compose up
```
Then proceed to access http://localhost:8000/ via your local browser and login with the account information you created. An admin should be able to add/remove members, create meetings, and control voting from the admin site: http://localhost:8000/admin.

# License

The MIT License (MIT)

Copyright (c) Mikayla Powell (2026)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
