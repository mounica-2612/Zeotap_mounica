# Zeotap_mounica

Project Summary
This project is a part of the Zeotap assignment, where the objective is to build a rule engine and a weather monitoring service using Python. The project involves:

1.Rule Engine (app/rule_engine.py and app/combine_rules.py):

->A simple rule engine to parse and evaluate logical conditions (AND, OR) for specified user attributes.
->It parses a rule string into an Abstract Syntax Tree (AST) and evaluates conditions against user data.
->Allows combining multiple rules to form complex conditions using logical operators.

2.Weather Monitoring Service (weather_monitoring/weather.py):

->A service that fetches real-time weather data for multiple cities using the OpenWeatherMap API.
->The service collects data such as temperature, weather conditions, and timestamps for each city.
->Provides functionalities to generate daily summaries and alert notifications if temperature thresholds are exceeded.
->Visualizes temperature trends over time for each city.