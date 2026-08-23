# Web Automation Test Suite - Parabank (BDD + Playwright Python)

End-to-end (E2E) automation testing suite built with **Playwright Python** and **pytest-bdd** using the **Page Object Model (POM)** pattern.

---

## 📁 Project Structure

```text
TRYPWAUTO/
├── features/
│   └── parabank.feature        # 7 Gherkin BDD Scenarios
├── pages/
│   ├── __init__.py
│   ├── login_page.py           # POM for Authentication & Validation
│   └── account_page.py         # POM for Account Navigation & Services
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Playwright fixtures & Tracing config
│   └── test_parabank.py        # Step definitions mapping
├── pytest.ini                  # Pytest runner configuration
├── requirements.txt            # Project dependencies
└── README.md
```

---

## 🛠️ Tech Stack & Prerequisites

* **Language:** Python 3.11+
* **Framework:** pytest, pytest-bdd
* **Automation Engine:** Playwright Python
* **Parallel Execution:** pytest-xdist

---

## 🚀 Setup & Execution

### 1. Clone & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate # On macOS/Linux
```

### 2. Install Dependencies & Browsers
```bash
pip install -r requirements.txt
playwright install
```

### 3. Run Test Suite

* **Standard Execution:**
  ```bash
  pytest
  ```

* **Parallel Execution (Fast Multi-worker):**
  ```bash
  pytest -n auto
  ```

---

## 🧪 Scenarios Covered

1. **Successful login** with valid credentials (`john` / `demo`).
2. **Failed login** with invalid credentials.
3. **Form validation error** when credentials are submitted empty.
4. **Navigation** to "Open New Account" page.
5. **Navigation** to "Transfer Funds" page.
6. **Navigation** to "Bill Pay" service.
7. **User logout** and session teardown.

---

## 🔍 Debugging & Artifacts

Test runs automatically capture Playwright traces in `trace.zip`. To inspect traces visually:
```bash
playwright show-trace trace.zip
```