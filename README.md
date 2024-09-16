# Synthetic Sparsity

Calendly is good, but there are excellent reasons you don’t necessarily want to over-expose your availability.

Take the example of perhaps wanting an investor to believe you’re in high demand and that they’re lucky to have your time. It changes how they approach the conversation and drives your confidence.

Personally, I also feel over-exposed if it’s too open. I just don’t like it.

Here’s my dumb-as-a-doorknob fix:

- Generate a bunch of quasi-random synthetic events.
- Import these into a new Google Calendar
- Use those events as blockers in Calendly to reduce my available slots in a natural-looking way

I’ve also thrown in the feature of offsetting the start/end of events, with layered chances of success. This lets you create multiple events with a minute more or less of buffer with wildly ranging levels of availability.

## Setup

### Generating good synthetic events (this repo)

(Recommended regular python things) Make a venv (eg. `python -m venv .venv`)

Install `ics` (eg. `pip install ics`)

Play with the variables at the top of `synthetic_sparsity.py`

Run the script (`python synthetic_sparsity.py`)

### Setting up Google Calendar

1. Create a new calendar
https://calendar.google.com/calendar/u/0/r/settings/createcalendar

2. Import the synthesized data
https://calendar.google.com/calendar/u/0/r/settings/export
⚠️ Be careful, don’t import it to your main calendar by accident. It’s a mess


### Calendly

Add the new calendar you just created under "check for conflicts"
I found I needed to wait a minute to get it to sync and reopen this menu once or twice for it to appear.
https://calendly.com/app/personal/availability/connected_calendars

