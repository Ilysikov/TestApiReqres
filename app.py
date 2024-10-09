import os

if __name__ == "__main__":
    # os.system("python3 -m pytest")
    os.system("poetry run pytest")
    # --alluredir allure - results
    # os.system("allure serve allure-results")