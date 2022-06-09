{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

## Local setup

1. Clone repository:

```shell
# Using ssh
git clone git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}.git
```

2. Navigate to cloned directory:

```shell
cd {{cookiecutter.project_slug}}
```

3. Create & activate virtual environment:

```shell
# Example with pyenv
pyenv virtualenv 3.9.6 {{cookiecutter.repository_name}}
pyenv local {{cookiecutter.repository_name}}
```

4. Install project requirements

```shell
pip install -Ur requirements.txt  # Packages needed to run app 
```

5. [Optional] Install dev tools

```shell
pip install tox  # tool used to isolate tests from local environment
pip install -e ".[tests,style,typing]"
```

## Committing changes

* After changing projects dependencies please do not edit fil [requirements.txt](requirements.txt) manually.
* Instead, add dependency to [setup.cfg](setup.cfg) and run:

```shell
tox -e pip-compile
```

* to update `requirements.txt`.

{% if is_open_source %}

## 📝 License

* This project is licensed under [{{ cookiecutter.open_source_license }}](LICENSE) license. {% endif %}

## ©️ Credits

* This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and
  the [sharp-cookiecutter](https://github.com/cicheck/sharp-cookiecutter) project template.
* Free software: {{ cookiecutter.open_source_license }}