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

1. Setup Github Action

    Set `KNOWN_HOSTS` and `SSH_KEY` in the repository-settings-Secrets-New repository secret

    Get `KNOWN_HOSTS`:

    ```shell
    ssh-keyscan -H [ip]
    ```

    Add excute permission to shell script:

    ```shell
    chmod 764 deploy_to_aws.sh 
    ```