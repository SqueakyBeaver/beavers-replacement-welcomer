# Running
Make a `config.json` file based off of `config.json.example` and the below section on configuring.
Then just `pip install -r requirements.txt` then `python main.py`
venv is optional, though if you're on nixOS and using direnv stuff, it will auto-create one for you

# Configuring (via `config.json`)
| Variable                   | What the value should be            | Explanation                                                                                             |
| -------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `bot.token`                | string of a discord id              | The bot's token. You should know how to get this                                                        |
| `bot.random.enabled`       | true or false                       | Whether the bot will respond after a random amount of messages (for that authenticity)                  |
| `bot.random.low`           | any number `x` >= `0`               | The minimum amount for the random calculation                                                           |
| `bot.random.high`          | any number greater than the minimum | The maximum amount for the random calculation                                                           |
| `bot.fixed`                | any number `x` >= `0`               | The number of messages that the bot should respond after. Will not have any effect if random is enabled |
| `bot.server.id`            | a string of a discord id            | The id of the server to watch in                                                                        |
| `bot.server.watch_channel` | a string of a discord id            | The id of the channel to watch in                                                                       |
| `bot.server.watch_user`    | a string of a discord id            | The id of the user to respond to                                                                        |