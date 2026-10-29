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

| Rule | What happens if it fails |
| --- | --- |
| **One ticket per user, per event** | The booking is blocked. This mirrors the BITS fest apps, where you only book a ticket for yourself. |
| **Enough money in the wallet** | The booking is blocked and you're nudged to top up your wallet. |
| **Slots still available** | You get a "sold out" error. |

If everything checks out, the ticket price is deducted from your wallet, the event's available slots drop by one, and the event shows up in **My Bookings**.

> Note: Allowing multiple tickets per user would be easy to add later using an intermediate table.

### For organizers

Organizer accounts can only be created by a **superuser** from the Django Admin panel. Once an organizer logs in with their credentials, they can:

-   See all their events on one dashboard
-   Open any event to check tickets sold, slots remaining, and customer details
-   Create new events with the **Add event** option

----------
