﻿# Zeotap_mounica
Overview
This project is part of a Zeotap assignment that demonstrates building a rule engine and a weather monitoring service using Python. It includes:

1.Rule Engine: A module for evaluating logical rules against user data.
2.Weather Monitoring Service: A module that fetches and analyzes real-time weather data for selected cities.

Requirements
Python 3.9
Docker (for containerization)
OpenWeatherMap API Key (required for the weather monitoring service)

Features
1.Rule Engine:

Parses rules in string format and converts them into an Abstract Syntax Tree (AST).
Evaluates conditions against user-defined data using logical operators (AND, OR).
Allows combining multiple rules to form complex logical expressions.

2.Weather Monitoring Service:

Fetches real-time weather data for a list of cities using the OpenWeatherMap API.
Logs weather data such as temperature, condition, and timestamp.
Generates daily summaries and alerts based on temperature thresholds.
Visualizes temperature trends over time.

Outputs
1.Rule Engine Output:

Parses rules and evaluates them based on the provided user data.
Displays the parsed Abstract Syntax Tree (AST) and the evaluation result.

2.Weather Monitoring Output:

Collects weather data for multiple cities at regular intervals.
Displays collected weather data, daily summaries, and alerts if temperature thresholds are exceeded.
