import os

if __name__ == "__main__":
    os.system("poetry run pytest")
    # --alluredir allure - results
    # os.system("allure serve allure-results")