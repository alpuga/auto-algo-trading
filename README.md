# AutoTrader Python Strategy Backtesting

A Python environment for backtesting trading strategies using the AutoTrader framework. Currently implements a MACD-based trading strategy with customizable parameters.

## Overview

This project provides a framework for:

- Backtesting trading strategies using historical data from Yahoo Finance
- Implementing and testing MACD-based trading strategies
- Configurable risk management and position sizing
- Visual analysis of trading performance

## Installation

This project uses Poetry for dependency management. To get started:

1. Clone the repository
2. Install Poetry if you haven't already:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:

```bash
poetry install
```

## Project Structure

## Current Strategy: Simple MACD

The implemented MACD strategy follows these rules:

1. Trade in the direction of the trend (using 200 EMA)
2. Entry signal on MACD cross above/below zero line
3. Stop loss at recent price swing
4. Take profit at 1.5x risk-reward ratio

### Configuration

Strategy parameters can be modified in `config/macd.yaml`:

```yaml
INTERVAL: "1h" # Trading timeframe
PERIOD: 300 # Required candles
SIZING: "risk" # Position sizing method
RISK_PC: 1.5 # Risk per trade (%)

PARAMETERS:
  ema_period: 200 # EMA period
  MACD_fast: 12 # MACD fast period
  MACD_slow: 26 # MACD slow period
  MACD_smoothing: 9 # MACD signal line period
  RR: 1.5 # Risk-reward ratio
```

## Usage

To run a backtest:

```bash
poetry run python autotrader_python/runfile.py
```

This will:

1. Load the strategy configuration
2. Run a backtest from 2021-01-01 to 2022-01-01
3. Display the results with visual plots

## Dependencies

- Python ^3.13
- AutoTrader ^1.1.2
- Additional dependencies managed through Poetry

## Contributing

Feel free to contribute by:

1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License
