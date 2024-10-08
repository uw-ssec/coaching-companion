# Coaching Companion

<span><img src="https://img.shields.io/badge/SSEC-Project-purple?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAOCAQAAABedl5ZAAAACXBIWXMAAAHKAAABygHMtnUxAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAMNJREFUGBltwcEqwwEcAOAfc1F2sNsOTqSlNUopSv5jW1YzHHYY/6YtLa1Jy4mbl3Bz8QIeyKM4fMaUxr4vZnEpjWnmLMSYCysxTcddhF25+EvJia5hhCudULAePyRalvUteXIfBgYxJufRuaKuprKsbDjVUrUj40FNQ11PTzEmrCmrevPhRcVQai8m1PRVvOPZgX2JttWYsGhD3atbHWcyUqX4oqDtJkJiJHUYv+R1JbaNHJmP/+Q1HLu2GbNoSm3Ft0+Y1YMdPSTSwQAAAABJRU5ErkJggg==&style=plastic" /><span>
![BSD License](https://badgen.net/badge/license/BSD-3-Clause/blue)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/uw-ssec/coaching-companion/main.svg)](https://results.pre-commit.ci/latest/github/uw-ssec/coaching-companion/main)
[![CI](https://github.com/uw-ssec/coaching-companion/actions/workflows/ci.yml/badge.svg)](https://github.com/uw-ssec/coaching-companion/actions/workflows/ci.yml)

This repository contains the code for the Coaching Companion project. The project is a set of migration tools that provides an internal package for Cultivate Learning engineers to modernize the existing database design. The project is built using Python and Jupyter Notebooks.

## Getting Started

To get started with your development (or fork), click the "Open with GitHub
Codespaces" button below to launch a fully configured development environment
with all the necessary tools and extensions.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/uw-ssec/coaching-companion?quickstart=1)

## Testing

### Running Tests with Pytest

To run your tests using pytest from the terminal, follow these steps:

1. Navigate to Your Project Directory: Open your terminal and navigate to the root directory of your project where your tests are located.

Run pytest: Execute the following command to run all tests:

```bash
pytest
```

2. Run Specific Tests: To run a specific test file or directory, provide the path:

```bash
pytest path/to/test_file.py
```

3. View Detailed Output: For more detailed output, use the -v (verbose) flag:
    
```bash
pytest -v
```

4. Generate a Test Report: To generate a test report, you can use the --junitxml option:

```bash
pytest --junitxml=report.xml
```

By following these steps, you can easily run and manage your tests using pytest from the terminal.

### Generate List of SQLModels [Optional]

Access the `tests/utils/generate_list_of_models.ipynb` notebook to generate a list of SQLModels from the database schema. This step is optional and only required if you want to update mulitple models. This notebook allows you to retrieve models in batches.

The output of this notebook is a list of SQLModels in a YAML file that can be used to generate unit tests.

### Generate Unit Tests from Templates

Access the `tests/utils/generate_test_from_template.ipynb` notebook to generate unit tests from the templates. This step is required if you want to update mulitple models. This notebook allows you to generate tests in batches. Currently, the template is based on models inheriting the BaseTableModel class, and you will need to add a new template for other models.

As written, the notebook will generate unit tests for the models in the `tests/models/` directory.
