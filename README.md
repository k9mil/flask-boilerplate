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
## License

Licensed under the MIT License - see the [LICENSE file](https://github.com/k9mil/flask-boilerplate/blob/master/LICENSE) for more details