from behave.__main__ import main as run_test_case
from pathlib import Path

project_path = Path(__file__).parent.parent.parent

feature = f"{project_path}/uTest/bdd/features/CreateUserInUtestPage.feature"
scenario = "Create User in U_Test page"
run_test_case([feature, '-n', scenario])
