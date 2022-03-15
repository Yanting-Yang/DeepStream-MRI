# Web Development

## 2022-03-14

1. Use prettier to format code.
1. Add 404 Not Found page.
1. Add team page.
1. Edit base.html, index page, publication page.

## 2022-03-13

1. Rewirte the structure of app module so that the coding is more standard.
1. Generate a new favicon using [favicon.io](favicon.io).
1. Edit `base.html`.

## 2022-03-10

1. Rewrite templates using jinja2 template inheritance and include function.
1. Edit `index.html` and `publication.html`.

## 2022-03-08

1. Edit `index.html`:

   Use dark theme. Add tools pannel.

   Use list group and collapse to show tool items.

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

   - [Application Discovery](https://flask.palletsprojects.com/en/2.0.x/cli/#application-discovery)

   `flask run` automatically detects an app (`app` or `application`) or factory (`create_app` or `make_app`). Therefore FLASK_APP environment does not need to be used.

   Application structure becomes:

   ```shell
   DeepStream-MRI
   └── app
       └── __init__.py (contains create_app)
   ```

3. Rewrite `__init__.py`.

## 2022-02-22

1. Create github repository
1. Add Blueprint. Change the structure.
1. [Add a favcion](https://flask.palletsprojects.com/en/2.0.x/patterns/favicon/).
1. Create the overall framwork.
