# GitHub Actions Testing Playground

This repository is a sandbox for learning and testing **GitHub Actions** workflows using small Python projects.  
The goal is to practice setting up CI/CD pipelines, running tests automatically, and enforcing code quality with linters.

---

## 📂 Projects in This Repo

### 1. Binary Search (Python)
A simple implementation of a binary search algorithm with unit tests.  
- **Workflow:** Runs ` python -m unittest` automatically on every push/pull request to unit_test_ci branch to verify correctness.

### 2. Web App Boilerplate (Python)
A minimal Python web app scaffold (Flask/FastAPI placeholder).  
- **Workflow:** Runs a linter (`flake8`) to ensure code follows Python style guidelines.

---

## ⚙️ GitHub Actions Workflows

- **CI Tests (`ci-python.yml`)**
  - Trigger: `push` and `pull_request`
  - Sets up Python environment
  - Installs dependencies
  - Runs unit tests for the binary search module

- **Linting (`lint-python.yml`)**
  - Trigger: `push` and `pull_request`
  - Checks Python code style for the web app boilerplate
  - Uses [Flake8](https://flake8.pycqa.org/) to enforce PEP8 style

---
