
# Django Test Projects

This repository contains three simple Django projects developed for learning and testing purposes.

## Projects

1. ### hello

   The `hello` project is a Django application that demonstrates how to render parameters sent through an HTTP request.

   - **Routes**:
     - `/hello`: Displays a default greeting.
     - `/hello/<name>`: Displays a customized greeting with the provided `<name>` parameter.

2. ### newyear

   The `newyear` project is an application that determines if the current date corresponds to January 1st (New Year's Day). If it does, it displays a message indicating that it's New Year; otherwise, it shows a message indicating that it's not New Year.

   - **Routes**:
     - `/newyear`: Checks if it's New Year's Day and displays a corresponding message.

3. ### task

   The `task` project is a Django application that manages a list of tasks. It allows displaying an existing list of tasks and adding new tasks to the list.

   - **Routes**:
     - `/task`: Displays the list of tasks.
     - `/task/add`: Allows adding new tasks via a form (GET and POST requests supported).

## Running Locally

To run any of these projects locally, follow these steps:

### 1. Clone the Repository

```bash
git clone <repository_url>
cd django-test-projects
```

### 2. Install Dependencies

Make sure you have Python and pip installed. Then, install the Django dependencies.

```bash
pip install -r requirements.txt
```

### 3. Run a Project

Navigate to the directory of the project you want to run (`hello`, `newyear`, or `task`) and perform the following actions:

```bash
cd hello    # for example, if you want to run 'hello'
python manage.py runserver
```

### 4. Access the Application

Open a web browser and go to `http://127.0.0.1:8000/` to see the application in action.

For specific routes:

- `http://127.0.0.1:8000/task/`: View the task list.
- `http://127.0.0.1:8000/task/add`: Add new tasks via form submission.

Additionally:

- `http://127.0.0.1:8000/newyear`: Check if it's New Year's Day.
- `http://127.0.0.1:8000/hello`: Display a default greeting.
- `http://127.0.0.1:8000/hello/<name>`: Display a customized greeting with `<name>`.

## Notes

- Each project is contained within its own directory in this repository.
- Make sure you have Python and Django installed in your local environment.
- The projects are simple and designed for educational purposes.
```
