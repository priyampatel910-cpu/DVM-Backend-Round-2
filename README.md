# DVM Recruitment: Task Two

  

## 1. Description of the project:

 I have selected the basic track for the task.

 The project I made is a web service called Evently, which lets a user book events, as well as allow organizers to create events.

>## Features (User)
>
> A new user is directed to the home page, where there are options to sign up and log in.
> I have made the website such that the user cannot aaccess anything without being authenticated, so login/signup is required.
> Won't go into technical details now, but I made the signup feature with a customized version of `UserCreationForm()`
>
> The moment you authenticate yourself, you will be directed to a user homepage/dashboard, where you can view your user account. The features Evently provides is:
> * It lets the user view their wallet balance (default is 0)
> * It lets the user add money to their wallet (for now, a fake payment gateway)
> * It lets the user browse for upcoming events in the Events section, where each event shows its name, its category, venue, date and time, and the ticket price
> * When a user click on a certain event's booking page link, the user gets redirected to the booking page with more information onthe event, as well as the billing summary.
> * Here is where I introduced some constraints for booking:
>
> Firstly, you get to book ONLY ONE TICKET for any event per one user. This is in sync with the BITS fest apps where the student can book an event ticket only for himself. So when the POST request is sent, the template will check if the user has any ticket prior to now or not, and will respond accordingly. (This could be changed to multiple tickets per user, using an intermediate table)
>
> Secondly, if the user has less money in their wallet than the ticket price, then the transaction will not take place and the user will be warned and advised to add money to their wallet.
>
> Lastly, if the tickets for the event are sold out, the user will not be able to book the event and will get the error message.
>
>  * In case the booking is successful, the amount of money equal to the ticket price of the event will be deducted from the user's account, available slots of the event will decrease by one, and now, when the user goes on My Bookings page (must be authenticated), they will see the list of events they booked
>  * In addition to that, My Bookings will also show the transaction history, may it be Wallet add or Wallet deduct (I am planning to make a separate page for that too)
>  * The authenticated user can sign out at any instance they want, once they sign up/ log in

> ## Features (Organizer)
> I have also added a feature that allows an **organizer user account** to create and handle events. This special account can only be made by **superuser** in Django Admin.
>
>It has the following features:
>* The organizer logs in with provided credentials.
>* The organizer can view all of their current events, and can view details. regarding any particular event, like the amount of tickets sold, number of slots remaining or customer details.
>* The organizer can also create a new event using *Add event* option on organizer dashboard.


## 2. How to use? (Without Dockerizing)
>
> ## Prerequisites
>
> Before running this project, ensure you have the following installed:
> * **Python** (version 3.10+ recommended)
> * **uv** (Fast Python package installer and manager)
> * **PostgreSQL** (Running locally or accessible via a network)

> ## Getting Started
>
> Follow these steps to clone the repository and set up your local development environment.
>
> ### 1. Clone the Repository
> ```bash
> cd projectfile
> git clone https://github.com/priyampatel910-cpu/DVM-Backend-Round-2.git
> cd event-platform
> ```
>
> ### 2. Set Up the Virtual Environment and Dependencies
> This project uses `uv` for dependency management. Run the following command to create a virtual environment and install all required packages:
> ```bash
> uv sync
> ```
> *Note: This automatically creates a `.venv` directory and installs the dependencies listed in `pyproject.toml` / `uv.lock`.*
>
> Activate the virtual environment: `.venv\Scripts\activate.bat`
>
> ### 3. Configure Environment Variables
> Create a `.env` file in the root directory of the project to configure your PostgreSQL database connection and Django settings. 
>
>Use this to create the Django secret key required in in `.env` file:
>```bash
>python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
>```
>
> *I have already added* `env.example` *file in the repo for the format. Note that you have to name your actual environment file* `.env`
>
> ### 4. Create the Database
> Ensure your PostgreSQL server is running, then create a database matching the name in your `.env` file:
> ```sql
> 
> CREATE ROLE event_app_user
> WITH LOGIN PASSWORD 'your-password';
>
> CREATE DATABASE event_platform
> OWNER event_app_user;
>
> ```
> *I have already configured the* `DATABASES` *so that it directly reads from* `.env` *which you have created above.*
>
> ### 5. Run Migrations and Start the Server
> Apply the database migrations to set up your tables:
> ```bash
> uv run python manage.py migrate
>  ```
>
> Create a superuser to access the Django admin panel:
>```bash
> uv run python manage.py createsuperuser
> ```
>
> Start the local development server:
> ```bash
> uv run python manage.py runserver
>```
> The application will be accessible at `127.0.0.1:8000`.
>
> ## Running Management Commands
> Because this project uses `uv`, you can run any Django management command by prefixing it with `uv run`:
>* Add a new package: `uv add package_name`.
>* 




