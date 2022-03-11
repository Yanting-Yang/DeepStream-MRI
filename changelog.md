# Web Development

## 2022-02-22

1. Create github repository
1. Add Blueprint. Change the structure.
1. Add a favcion[^1].
1. Create the overall framwork.

Build development environment.
Github Action. Automatic Deployment.

[^1]: [Adding a favicon](https://flask.palletsprojects.com/en/2.0.x/patterns/favicon/)

## 2022-02-26

1. Setup Github Action.

    Set `KNOWN_HOSTS` and `SSH_KEY` in the repository-settings-Secrets-New repository secret.

    Get `KNOWN_HOSTS`:

    ```shell
    ssh-keyscan -H [ip]
    ```

    Add excute permission to shell script:

    ```shell
    chmod 764 deploy_to_aws.sh 
    ```

2. Change directory name to app.

    `flask run` automatically detects an app (`app` or `application`) or factory (`create_app` or `make_app`)[^2]. Therefore FLASK_APP environment does not need to be used.

    Application structure becomes:

    ```shell
    DeepStream-MRI
    └── app
        └── __init__.py (contains create_app)
    ```

    [^2]: [Application Discovery](https://flask.palletsprojects.com/en/2.0.x/cli/#application-discovery)

3. Rewrite `__init__.py`.

## 2022-03-08

1. Edit index.html

    Use dark theme. Add tools pannel.

    Use list group and collapse to show tool items.

## 2022-03-10

1. Rewrite templates using jinja2 template inheritance and include function.
1. Edit index.html and publication.html
