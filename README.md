# [ROO] Berry Reminder Bot

This is a simple Discord bot to help users set reminders for harvesting Leppa Berries and Gracidea Flowers, as well as watering their berries.

The bot can be found at {TODO Add Link to Bot}

## Usage

### Commands

- `!leppa`: Sets a reminder to harvest Leppa Berries in 20 hours.
- `!gracidea`: Sets a reminder to harvest Gracidea Flowers in 44 hours.
- `!water <duration>`: Sets a custom reminder to water berries in the specified duration (in hours).
- `!reminders`: Lists all active reminders for the user.
- `!cancel`: Cancels all active reminders for the user.

### Example

User: `!leppa`
Bot: `Reminding @User to harvest Leppa Berry in 20 hours`

User: `!gracidea`
Bot: `Reminding @User to harvest Gracidea Flower in 44 hours`

User: `!water 3`
Bot: `Reminding @User to water their berries in 3 hours`

User: `!reminders`
Bot: `@User, you have the following active reminders:
leppa
gracidea
water`

User: `!cancel`
Bot: `@User, all of your reminders have been cancelled.`


## Project Setup

1. Install the required dependencies using pip: `pip install discord.py`
2. Replace `YOUR_TOKEN_HERE` in the last line of the code with your bot's token (or better yet, use an environment variable)

### Running the Bot Locally

To run the bot, simply execute the Python script: `python berry_reminder_bot.py`




