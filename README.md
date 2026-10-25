# DVM Recruitment: Task Two

## 1. Description of the project:

> I have selected the basic track for the task.
>
> The project I made is a web service called Evently, which lets a user book events. It works as follows:
> > A new user is directed to the home page, where there are options to sign up and log in.
> > I have made the website such that the user cannot aaccess anything without being authenticated, so login/signup is required.
> > Won't go into technical details now, but I made the signup feature with a customized version of `UserCreationForm()`
> >
> > The moment you authenticate yourself, you will be directed to a user homepage/dashboard, where you can view your user account. The features Evently provides is:
> > * It lets the user view their wallet balance (default is 0)
> > * It lets the user add money to their wallet (for now, a fake payment gateway)
> > * It lets the user browse for upcoming events in the Events section, where each event shows its name, its category, venue, date and time, and the ticket price
> > * When a user click on a certain event's booking page link, the user gets redirected to the booking page with more information onthe event, as well as the billing summary.
> > * Here is where I introduced some constraints for booking:
> >   > Firstly, you get to book ONLY ONE TICKET for any event per one user. This is in sync with the BITS fest apps where the student can book an event ticket only for himself. So when the POST request is sent, the template will check if the user has any ticket prior to now or not, and will respond accordingly. (This could be changed to multiple tickets per user, using an intermediate table)
> >   > 
> >   > Secondly, if the user has less money in their wallet than the ticketprice, then the transaction will not take place and the user will be warned and advised to add money to their wallet.
> >   >
> >   > Lastly, if the tickets for the event are sold out, the user will not be able to book the event and will get the error message.
> >   >
> > * In case the booking is successful, the amount of money equal to the ticket price of the event will be deducted from the user's account, available slots of the event will decrease by one, and now, when the user goes on My Bookings page (must be authenticated), they will see the list of events they booked
> > * In addition to that, My Bookings will also show the transaction history, may it be Wallet add or Wallet deduct (I am planning to make a separate page for that too)
> > * The authenticated user can sign out at any instance they want, once they sign up/ log in
