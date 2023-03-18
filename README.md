### Dhabetny
#### the Travel Plan Recommender App

This is a web application built with Flask that recommends travel plans for users based on their preferences. The application uses OpenAI's GPT-3 language model to generate travel plans based on the input provided by the user.

Getting Started
To get started with the application, follow these steps:

Clone the repository to your local machine.
Install the required dependencies listed in requirements.txt.
Create an account on the OpenAI platform and obtain an API key.
Set the environment variable OPENAI_API_KEY to your API key.
Start the Flask server by running python app.py in your terminal.
Navigate to http://localhost:5000/ in your web browser to access the application.
Usage
Once the application is running, the user can input their preferences on the homepage. The preferences include the following:

City to visit
Number of places to visit
Number of days for the trip
Number of people traveling
Budget for the trip
The user can submit their preferences by clicking the "Submit" button, and the application will generate a travel plan based on the input using OpenAI's GPT-3 language model. The generated travel plan will be displayed on a new page.

Acknowledgments
This application was built using Flask and OpenAI's GPT-3 language model.
The HTML and CSS templates used in the application were obtained from Bootstrap.
The application was developed as part of a project for learning web development and natural language processing

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
