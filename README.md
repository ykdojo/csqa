# CSQA - An open-source Q&A website for coders

Welcome to [CSQA](https://csqa.io/)! It's an open-source Q&A website for coders of all levels.

### What is this website for?

It's for asking any coding-related questions! Whether they are about any specific language, setting up your dev environment, or anything else, please feel free to use this website for it.

### Why did you create this website?

I wanted to make a website where coders (mostly beginners-intermediate learners) can ask each other any coding-related questions.

Also, it's part of my new video series where I do some development and make a video about it every week.

### What did you use to build this website?

I used Python (Django) for backend, Postgres for database, Bootstrap for frontend, Heroku for deployment, and Namecheap for domain registration. I'm planning to add either Vue.js or React on top of it.

---

## How to run this web app locally

### 1. Install pipenv and go into the shell (make sure you have pip3 or pip first.)

If you're not familiar with this step, I recommend checking out the [first few sample chapters](https://djangoforbeginners.com/initial-setup/) of [Django for Beginners](https://gumroad.com/a/173585523) (that's my referral link).

If you're completely new to Django, I also recommend checking out [my previous video series on Django](https://www.youtube.com/watch?v=UyQn0BhVqNU&list=PLBZBJbE_rGRXBhJNdKbN7IUy-ctlOFxA1).
```
pip3 install pipenv
pipenv install
pipenv shell
```

### If you have trouble instaling psycopg2, you might want to try something like this:

https://stackoverflow.com/questions/39767810/cant-install-psycopg2-package-through-pip-install-is-this-because-of-sierra

This command worked for me:

```
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pipenv install psycopg2
```

### Note, there are two options here.

If you want to start running this server with sqlite3 right away, skip to Step 4.

Step 2 - 3 are only for setting up Postgres and they are optional.

### 2-A. Set up Postgres on your local environment.

You can use a commandline interface or something like [Postgres.app](https://postgresapp.com/), which I use.

Whatever you decide to use, you'll need to make sure Postgres is running on your local enviornment.

Please let me know if you need help with this step at [@ykdojo on Twitter](https://twitter.com/ykdojo) or on [csqa.io](https://csqa.io/).

### 2-B. Create a new Postgres database.

Create a new Postgres database. I call it csqa, but you can call it anything you want. Make sure you have created a user and set a password on it, too.

### 3. Add an environment variable for connecting to your Postgres database.

For this one, check out .bash_profile_sample as an example.

### 4. Migrate and run your server

Just run:

```
./manage.py migrate # note: make sure you have run pipenv shell before this
./manage.py runserver
```

### 5. Want to contribute?

Thank you! That would be great. Please feel free to send any pull requests here.

If you have any questions or comments, please let me know on our Discord server here: https://discordapp.com/invite/YhpHpBa
