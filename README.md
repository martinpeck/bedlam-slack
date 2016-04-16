# Bedlam Slack - Slash Commands

This is a flask app that implements a number of slash commands for Slack.

## Installation

- clone this repository
- set up a Python 3 virtual environment with `pyvenv venv`
- install the dependencies with `pip install -r requirements`
- you're done

## Running the code locally

- install foreman with `gem install foreman`
- create a `.env` file using the `.env.example` as a template
- use `foreman start` if you want to run the service as Heroku runs it
- use `foreman start --procfile Procfile.dev` if you want to debug and auto-load on file changes

## Deployment

This repository auto-deploys to Heroku. Simply check in to the `master` branch and you're done.

## Bugs and stuff

If you find bugs, or have suggestions, open a GitHub issue

## Contributions and Licensing

All that stuff can be found in [LICENSE.md](LICENSE.md) and [CONTRIBUTING.md](CONTRIBUTING.md). 
Go on...read them. 
You know you want to.