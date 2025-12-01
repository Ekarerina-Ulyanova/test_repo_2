# test_repo_2

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

## Overview

test_repo_2 is a personal budget management tool that helps users track expenses, set spending limits, and visualize monthly financial summaries. It enables informed financial decisions by offering an intuitive interface to monitor spending, enforce budget constraints, and maintain financial records securely across sessions.

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

## Core features

1. **Expense Management**: Allows users to add, view, and remove individual expenses with details such as amount, category, and description. Expenses are stored in a local SQLite database for persistence.
2. **Budget Tracking**: Enables users to set and manage a budget amount. The application tracks the current budget balance and ensures expenses do not exceed available funds.
3. **Graphical User Interface**: Provides a user-friendly desktop interface built with Tkinter, allowing users to interact with the budget manager through buttons, entry fields, and a listbox for viewing expenses.
4. **Data Persistence**: Utilizes SQLite to store budget and expense data locally in a 'budget.db' file, ensuring that information persists between application sessions.
5. **Monthly Financial Summary**: Displays a summary of all expenses and the total amount spent during the month, helping users review their spending habits through a dedicated view function.
6. **Budget Validation**: Prevents users from adding expenses that exceed their current budget by validating transaction amounts before recording them.
7. **Input Error Handling**: Implements error handling for invalid user inputs, such as non-numeric values, and provides user feedback via message boxes to improve usability.

## Installation

Install test_repo_2 using one of the following methods:

**Build from source:**

1. Clone the test_repo_2 repository:
```sh
git clone https://github.com/Ekarerina-Ulyanova/test_repo_2
```

2. Navigate to the project directory:
```sh
cd test_repo_2
```

## Contributing

- **[Report Issues](https://github.com/Ekarerina-Ulyanova/test_repo_2/issues)**: Submit bugs found or log feature requests for the project.

- **[Submit Pull Requests](https://github.com/Ekarerina-Ulyanova/test_repo_2/tree/main/.github/CONTRIBUTING.md)**: To learn more about making a contribution to test_repo_2.

## Citation

If you use this software, please cite it as below.

### APA format:

Ekarerina-Ulyanova (2025). test_repo_2 repository [Computer software]. https://github.com/Ekarerina-Ulyanova/test_repo_2

### BibTeX format:

```bibtex
@misc{test_repo_2,
    author = {Ekarerina-Ulyanova},
    title = {test_repo_2 repository},
    year = {2025},
    publisher = {github.com},
    journal = {github.com repository},
    howpublished = {\url{https://github.com/Ekarerina-Ulyanova/test_repo_2.git}},
    url = {https://github.com/Ekarerina-Ulyanova/test_repo_2.git}
}
```