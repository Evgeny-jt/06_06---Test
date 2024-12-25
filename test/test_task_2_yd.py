import pytest
import requests

class TestYandexDisk:
    def setup_method(self):
        self.utl = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Authorization': ''} # ввести свой токен от yandex disk

    @pytest.mark.parametrize(
        'param, name, status_code',
        (
                ["path", 'foto', 201],
                ["path", 'foto', 409],
                ["pach", 'foto', 400],
        )
    )
    def test_yandex_disk_create_folder(self, param, name, status_code):
        params = {
            param: name
        }
        response = requests.put(self.utl, params=params, headers=self.headers)
        assert response.status_code == status_code

