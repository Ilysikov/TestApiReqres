import os

if __name__ == "__main__":
    os.system("poetry run pytest test --alluredir allure-results")
