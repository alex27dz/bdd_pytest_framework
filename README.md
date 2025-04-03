Python automation ⛵️
---------------------	
✅ Use @tags in feature files to group tests.
✅ Run tagged tests using Behave (behave -t @tag).
✅ Run Behave tests inside Pytest (pytest --behave -t @tag).
✅ Filter tests using behave.ini.
✅ Use Pytest to run specific test files or steps.
✅ pytest --behave tests/features/login.feature

---------------------	
bdd_pytest_framework/
│── tests/
│   │── features/
│   │   ├── login.feature
│   │── steps/
│   │   ├── login_steps.py
│   │── environment.py
│── pages/
│   │── base_page.py
│   │── login_page.py
│── utils/
│   │── config.py
│   │── logger.py
│── reports/
│── conftest.py
│── pytest.ini
│── behave.ini
│── requirements.txt
│── README.md
---------------------	