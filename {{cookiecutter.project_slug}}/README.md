{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

{% if is_open_source %}
## 📝 License
* This project is licensed under [{{ cookiecutter.open_source_license }}](LICENSE) license.
{% endif %}


## ©️ Credits
* This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [sharp-cookiecutter](https://github.com/cicheck/sharp-cookiecutter) project template.
* Free software: {{ cookiecutter.open_source_license }}