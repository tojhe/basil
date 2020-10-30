# Welcome to Basil

This is a trading tool that I've built because I am too poor to afford 3Comma's subscription plans.
I've built this tool to align with my crypto trading habits and need, with Binance.

This repository is largely built on top of the library [python-binance](https://github.com/binance-exchange/python-binance) to interact with Binance API and execute trades.

# Features

- The key rudimentary feature now is the trailing buy tool to be used to buys coins at the best possible rate.
    - To understand more about trailing buy, please refer to 3Comma's [article](https://help.3commas.io/en/articles/3108937-how-trailing-buy-works).

# Planned integrations
- A messaging system to relay buy/sell orders on trigger.
- Containizeration for modules to buy/sell vs logic.
- Environment variables/config file reference for API keys/secrets