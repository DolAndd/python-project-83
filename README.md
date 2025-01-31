## Page analyzer.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/DolAndd/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DolAndd/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/858ebc035b21236ac119/maintainability)](https://codeclimate.com/github/DolAndd/python-project-83/maintainability)
![example event parameter](https://github.com/DolAndd/python-project-83/actions/workflows/action.yaml/badge.svg?event=push)

#### Description:
Page Analyzer is a web service that makes requests to specified sites, analyzes them and saves the received data into the created database. The application is based on the Flask framework

#### Download and Installation:
1. Download the application from GitHub using the [link](https://github.com/DolAndd/python-project-83).
2. Install [uv](https://docs.astral.sh/uv/#__tabbed_1_1).
3. Go to the project directory `python-project-83` and type `make install`.
4. Create a database. Create a `.env` file and enter the data base data into it.
5. Type `make biuld` to connect the database to the project.

#### Launching the application
1. Command `make dev` to run the application locally.
2. Command `make render-start` to run on Render.com.

Project site:
https://python-project-83-ssdc.onrender.com
