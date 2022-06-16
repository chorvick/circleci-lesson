# Circle CI Lesson

Circle CI has established themselves as one of the most reliable CI/CD solutions in the industry.

In this repo we will learn how to use Circle CI to build and deploy our own applications.

# Getting Started

Signup and create a new project on Circle CI.

https://circleci.com/

Allows Circle CI to build and deploy applications within your Github account. You can also create a new project for a different Github account.

Fork this repo.

Create a branch for your changes.

Create a pull request and look for the `circleci` label.

You now have Circle CI configured to build and deploy your application.

# Circle CI

Circle CI is a continuous integration and continuous delivery service. It operates based off of a config file within the `.circleci` directory.

Within this directory there is a `config.yml` file. 

Withijn the config file there are some important settings.

| Parent | Description |
|---------|-------|
|  `workflow` | A set of jobs to run given the name of a branch. |
| `job` | A set of steps to perform  |
| `step` | A "single" executable to execute when a job is ran on a branch triggerd by a workflow. |
| `orb` | Pre-created instructions to be used by developers |


# Lesson
 
How mant workflows are configured?

How many jobs are configured?

What is the name of the job that runs the testing?


# Lab

1. Add 3 new routes to the API

| Method | Path | Description |
|---------|------|-------------|
| `GET` | `/api/v1/users` | Get all users |
| `POST` | `/api/v1/users` | Create a user |
| `GET` | `/api/v1/users/:id` | Get a user |

2. Add a test for each of the routes that properly returns a 200 status code.

3. Create a Heroku app using the `heroku create` command.

4. Add the name of the heroku app and an API key to the settings of your project in Circle CI.

5. Deploy the app to Heroku.




