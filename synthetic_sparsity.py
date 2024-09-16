# %%
import random
from ics import Calendar, Event
from datetime import datetime, timedelta, timezone

# %%
# What's the maximum continuous blocker you want
max_run = timedelta(hours=2)

# For the sparsity levels to translate to portions of your time
#   open in each category, this needs to be your meeting size
chunk_size = timedelta(minutes=30)

# You wanna make this the actual buffer you care about between meetings
level_offset = timedelta(minutes=5)

# Calibrate this to find the levels of sparsity
#   that is useful to you, with varying levels
# A level here refers to an offset from the
#   start/end of the event, allowing you to create
#   variably sparse event types
sparsity_levels = [0.3, 0.6, 0.8]

sparsity_levels = sorted(sparsity_levels)
assert all(0.0 < sparsity_level < 1.0 for sparsity_level in sparsity_levels)

# These are the dates of the fist and last events generated
overall_start = datetime(2024, 9, 1, 0, 0, tzinfo=timezone.utc)  # 8:00 AM
# If you're playing around, I recommend bringing in this duration to ~1wk
overall_end = overall_start + timedelta(days=365)

# %%
calendar = Calendar()

considered_slot = overall_start
prev_event: Event | None = None


def add_event(level: timedelta):
    global considered_slot
    event = Event()
    event.name = "Random Blocker"
    event.description = "This is a randomly generated event occupying time."
    event.location = "No Location"

    event.begin = considered_slot + level + level_offset
    event.end = considered_slot + chunk_size - level_offset

    calendar.events.add(event)
    return event


while considered_slot < overall_end:
    # Do this up first because we need it in every case
    considered_slot += chunk_size

    # Force an empty slot if we're approaching the max run length
    if prev_event and (considered_slot - prev_event.end) + chunk_size > max_run:
        prev_event = None
        continue

    # Let's roll them dice!
    roll = random.random()

    # It's a completely filled slot
    if roll > sparsity_levels[-1]:
        if prev_event:
            prev_event.end += chunk_size
        else:
            prev_event = add_event(timedelta(minutes=0))
        continue

    # It's a completely empty slot
    elif roll < sparsity_levels[0]:
        # in this case, it's a completely empty slot
        prev_event = None
        continue

    for level_i, level_p in enumerate(sparsity_levels):
        if roll < level_p:
            if prev_event:
                prev_event.end = considered_slot + chunk_size - level_offset
            else:
                prev_event = add_event(timedelta(minutes=len(sparsity_levels) - level_i))

# %%
# Save the calendar to an .ics file
with open("synthetic_sparsity.ics", "w") as f:
    f.writelines(calendar)
