# Python + Selenium CI/CD Automation Framework

This project is a lightweight, professional-grade QA automation framework built with **Python**, **Selenium**, and **PyTest**, fully integrated with **GitHub Actions CI/CD**.
It demonstrates modern QA engineering practices including page object modeling, headless browser execution, automated test reporting, and continuous integration.

---

## 🚀 Features

- **Python + Selenium** UI test automation
- **PyTest** test runner with HTML reporting
- **Page Object Model (POM)** structure
- **Headless Chrome** for CI environments
- **GitHub Actions CI/CD pipeline**
- Automatic:
  - Dependency installation
  - Test execution
  - HTML report upload
- Clean, extensible project layout suitable for real-world QA teams

---

## 📁 Project Structure
python-selenium-ci-cd/ │ ├── tests/ │   └── test_google_search.py │ ├── pages/ │   ├── base_page.py │   └── google_page.py │ ├── utils/ │   └── driver_factory.py │ ├── requirements.txt ├── pytest.ini └── .github/ └── workflows/ └── ci.yml

---

## 🧪 Running Tests Locally

### 1. Create and activate a virtual environment


python -m venv venv source venv/bin/activate   # Mac/Linux venv\Scripts\activate      # Windows

### 2. Install dependencies


pip install -r requirements.txt

### 3. Run tests


pytest

### 4. View the HTML report
After running tests, open:


report.html

---

## 🧱 CI/CD Pipeline (GitHub Actions)

This project includes a fully automated CI pipeline located at:


.github/workflows/ci.yml

The pipeline runs on every **push** and **pull request**, performing:

- Python setup
- Dependency installation
- Selenium test execution
- HTML report upload as an artifact

You can view pipeline runs under the **Actions** tab in your GitHub repository.

---

## 🧩 Technologies Used

- **Python 3.11+**
- **Selenium 4**
- **PyTest**
- **webdriver-manager**
- **GitHub Actions**
- **Headless Chrome**

---

## 📌 Example Test

```python
def test_google_search():
    driver = create_driver()
    page = GooglePage(driver)

    page.open("https://www.google.com")
    page.search("Selenium Python")

    assert "Selenium" in driver.title

    driver.quit()



🌱 Future Enhancements
- Allure reporting
- Parallel test execution
- Browser matrix (Chrome, Firefox)
- API testing integration
- Dockerized test environment

🤝 Contributing
Contributions, issues, and feature requests are welcome.
Feel free to fork the repo and submit a pull request.

📜 License
This project is open source and available under the MIT License.




