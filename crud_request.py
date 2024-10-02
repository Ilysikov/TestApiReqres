import httpx


class CRUD:
    def __init__(self, url):
        self.BASE_URL = url

    def get_users(self, params):
        return httpx.get(self.BASE_URL + "/api/users/", params=params)

    def post_users(self, data):
        return httpx.post(self.BASE_URL + "/api/users", data=data)

    def put_users(self, params, data):
        return httpx.put(self.BASE_URL + "/api/users/", params=params, data=data)

    def patch_users(self, params, data):
        return httpx.patch(self.BASE_URL + "/api/users/", params=params, data=data)

    def delete_users(self, params):
        return httpx.delete(self.BASE_URL + "/api/users/", params=params)

    def get_none_params(self):
        return httpx.get(self.BASE_URL)
