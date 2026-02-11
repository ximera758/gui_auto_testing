# GUI Auto Testing – SauceDemo

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-green)](https://www.selenium.dev/)
[![PyTest](https://img.shields.io/badge/PyTest-Testing-orange)](https://docs.pytest.org/)

This project contains UI automation tests for the SauceDemo web application using Python, Selenium WebDriver, and PyTest.

## 🚀 Project Structure

gui_auto_testing/
├── pages/
│ ├── base_page.py
│ ├── login_page.py
│ └── inventory_page.py
├── tests/
│ ├── test_login.py
│ └── test_inventory.py
├
│ 
├── requirements.txt
├── .gitignore
└── README.md
## 🛠 Tech Stack

- Python  
- Selenium WebDriver  
- PyTest  
- webdriver-manager

## 🧪 How to Run Tests

1. Install dependencies

```bash
pip install -r requirements.txt

2 Run all tests
pytest -v
🧠 What is Tested

User login functionality

Inventory display and navigation

Element interactions and assertions

💡 Example Usage

pytest tests/test_login.py

📌 Notes

Page Object Model used for maintainability

Tests structured for readability
