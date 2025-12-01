# test_repo_2

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

## Overview

test_repo_2 is a personal budget management tool designed to help users track expenses, set spending limits, and review monthly financial summaries. It empowers individuals to make informed financial decisions by offering an intuitive, secure, and user-friendly experience for managing personal finances effectively.

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

## Core features

1. **Expense Management**: Allows users to add, view, and remove individual expenses with details such as amount, category, and description. Expenses are stored in a local SQLite database for persistence and can be managed through a graphical interface.
2. **Budget Tracking**: Enables users to set and manage a budget amount. The application tracks the current budget balance in real time and updates it when expenses are added or removed, ensuring accurate financial oversight.
3. **Graphical User Interface**: Provides a user-friendly desktop interface built with Tkinter, allowing users to interact with the budget manager through intuitive elements like buttons, entry fields, and a listbox for viewing and managing expenses.
4. **Data Persistence**: Utilizes SQLite to store budget and expense data locally in a 'budget.db' file, ensuring that all financial records persist across application sessions and are not lost upon closure.
5. **Budget Validation**: Prevents users from adding expenses that exceed their current budget by validating transaction amounts before recording them, thus enforcing responsible spending behavior.
6. **Input Error Handling**: Implements robust error handling for invalid user inputs, such as non-numeric values, and provides clear feedback via message boxes to improve usability and prevent application errors.

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

Ekarerina-Ulyanova (2025). test_repo_2 repository [Computer software]. https://github.com/Ekarerina-Ulyanova/test_repo_2

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