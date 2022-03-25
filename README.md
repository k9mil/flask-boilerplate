# Welcome 

No Flask-SQLAlchemy, no ORMS, no Flask-WTF, no Bootstrap.

Simple layout, with Flask + Blueprints.

## Tree Structure

  ```sh
|   .gitignore
|   LICENSE
|   Procfile
|   README.md
|   requirements.txt
|
\---project
    |   config.py
    |   __init__.py
    |
    +---errors
    |       routes.py
    |       __init__.py
    |
    +---main
    |       routes.py
    |       __init__.py
    |
    +---static
    |       style.css
    |
    +---system
    |       models.py
    |       __init__.py
    |
    \---templates
        |   index.html
        |
        +---base
        |       base.html
        |       error_base.html
        |
        \---errors
                404.html
  ```
  
## Getting Started

1. Clone the flask-boilerplate repository.
    ```
    $ git clone https://github.com/realpython/flask-boilerplate.git
    $ cd flask-boilerplate
    ```

2. Initialize a virtual environment for packages.
    ``` 
    [windows]
    $ python -m venv venv
    $ venv/Scripts/activate
    
    [bash]
    $ python -m venv venv
    $ source env/bin/activate
    ```

3. Install the dependencies.
    ```
    $ pip install -r requirements.txt
    ```

4. Run the flask application.
    ```
    $ flask run
    ```

  
## License

Licensed under the MIT License - see the [LICENSE file](https://github.com/k9mil/flask-boilerplate/blob/master/LICENSE) for more details