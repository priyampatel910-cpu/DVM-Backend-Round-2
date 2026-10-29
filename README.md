
#  Evently

A small event-booking web app built with **Django** and **PostgreSQL**. Users book tickets using an in-app wallet, and organizers create and manage their own events.

This is my submission for **DVM Recruitment, Task Two** (Backend, Basic Track).

----------

## What does it do?

Evently has two kinds of people using it: **users** who book events, and **organizers** who put those events up. Everything sits behind a login, so you can't see anything without signing up first.

### For users

-   **Sign up / log in:** the signup form is a customised version of Django's `UserCreationForm()`.
-   **Wallet:** every account starts with a balance of 0. You can top it up through a *(fake)* payment gateway.
-   **Browse events:** see each event's name, category, venue, date and time, and ticket price.
-   **Booking page:** click an event to see more details plus a billing summary before you confirm.
-   **My Bookings:** your booked events and your full transaction history (wallet top-ups and deductions).
-   **Sign out** whenever you like.

### Booking rules

Three checks run before a booking goes through:

Rule

What happens if it fails

**One ticket per user, per event**

The booking is blocked. This mirrors the BITS fest apps, where you only book a ticket for yourself.

**Enough money in the wallet**

The booking is blocked and you're nudged to top up your wallet.

**Slots still available**

You get a "sold out" error.

If everything checks out, the ticket price is deducted from your wallet, the event's available slots drop by one, and the event shows up in **My Bookings**.

> Note: Allowing multiple tickets per user would be easy to add later using an intermediate table.

### For organizers

Organizer accounts can only be created by a **superuser** from the Django Admin panel. Once an organizer logs in with their credentials, they can:

-   See all their events on one dashboard
-   Open any event to check tickets sold, slots remaining, and customer details
-   Create new events with the **Add event** option

----------

## Running it locally (without Docker)

### Prerequisites

-   **Python** 3.10+
-   **uv** as recommended in the task description
-   **PostgreSQL** 18.6

### 1. Clone the repo

```bash
git clone https://github.com/priyampatel910-cpu/DVM-Backend-Round-2.git
cd DVM-Backend-Round-2
```

### 2. Install dependencies

```bash
uv sync
```

This creates a `.venv` folder and installs everything listed in `pyproject.toml` / `uv.lock`.

<details> <summary>Want to activate the virtual environment manually?</summary>

`uv run` picks up the environment automatically, so this is optional.

-   **Windows (CMD):** `.venv\Scripts\activate.bat`
-   **Windows (VS Code):** press `Ctrl + Shift + P`, choose **Python: Select Interpreter**, pick `event-platform`, then open a new terminal.

</details>

### 3. Set up your `.env` file

Copy the example file and rename it to `.env` in the project root:

```bash
cp .env.example .env
```

Fill in your database details, then generate a Django secret key and paste it in:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

`settings.py` reads the database config straight from this file.

### 4. Create the database

With PostgresQL running, create a role and database that match what you put in `.env`:

```sql
CREATE ROLE event_app_user
  WITH LOGIN PASSWORD 'your-password';

CREATE DATABASE event_platform
  OWNER event_app_user;

```

### 5. Migrate, create a superuser, and run

```bash
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver

```

Open **http://127.0.0.1:8000** and you're in.

> [!TIP] Since this project uses `uv`, prefix any Django command with `uv run`. To add a package, use `uv add package_name`.

----------

## Running it with Docker

The repo includes a `compose.yaml` and a `Dockerfile`, but I haven't published a prebuilt image, so you'll build it yourself. Compose runs two services: **web** (Django) and **db** (PostgreSQL), so you don't need a separate Dockerfile for Postgres.

> Note: I learned how to write the compose file for this project, but I still don't fully understand how the `healthcheck` options work. I'll dig into that once I'm done with the rest.

### 1. Clone the repo

```bash
git clone https://github.com/priyampatel910-cpu/DVM-Backend-Round-2.git
cd DVM-Backend-Round-2

```

### 2. Create your `.env` file

Rename `.env.example` to `.env` and fill in the details. It needs to live in the **project root**.

### 3. Build and start the services

Make sure you have Docker Engine installed (I built this on v29.9.2), then run:

```bash
docker compose up --build -d

```

The `-d` flag is optional. It runs the containers in the background so you can keep using your terminal.

### 4. Migrate and create a superuser

The migration files are already committed, so there's no need to run `makemigrations`. Just apply them:

```bash
docker compose run --rm web uv run --no-sync python manage.py migrate

```

Then create your superuser the same way:

```bash
docker compose run --rm web uv run --no-sync python manage.py createsuperuser

```

You can swap in any other Django command after `uv run`.

> Note: **`docker compose run` vs `docker compose exec`:** `run` spins up a _temporary_ container for a single command (`--rm` deletes it afterwards), while `exec` runs a command inside a container that's _already running_. Use whichever suits you.

----------

## Looking back

This project was tough, but seeing everything finally work smoothly was really satisfying. I know it has some fundamental problems: my model choices could be better, and I put everything in one app instead of splitting features into separate ones, which will hurt scalability. I've learned from these mistakes and plan to do better in the next project.

## A note on AI usage

All the minimalistic HTML templates were generated by AI, because I don't know CSS well enough to style them myself. All I did was pass data from `views.py` into the templates, and the rest of the UI is AI-generated. Since this is a backend task, I figured a fancy frontend wasn't necessary, but I added one anyway. Hope you don't mind! I'm happy to share the chat if you'd like to see it.