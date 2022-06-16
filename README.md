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

Which job is configured to run when a branch is triggered?

