import os

if __name__ == "__main__":
    # os.system("python3 -m pytest")
    os.system("poetry run pytest test --alluredir allure-results")
    #
    os.system("poetry run allure serve allure-results")