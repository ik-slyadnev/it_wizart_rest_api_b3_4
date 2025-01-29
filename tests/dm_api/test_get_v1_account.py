from hamcrest import assert_that, equal_to

class TestGetV1Account:

    def test_get_v1_account_auth(self, auth_user):
        """
        Тест на получение информации об авторизованном пользователе

        Шаги:
        1. Получаем информацию об авторизованном пользователе
        2. Проверяем ответ
        """
        response = auth_user.helper.get_current_user()

        assert_that(response.status_code, equal_to(200))
        assert_that(response.json()['resource']['login'], equal_to(auth_user.user.login))

    def test_get_v1_account_no_auth(self, dm_api_facade):
        """
        Тест на получение информации без авторизации

        Шаги:
        1. Пытаемся получить информацию о пользователе без авторизации
        2. Проверяем что получаем ошибку авторизации (401)
        """
        response = dm_api_facade.account_api.get_v1_account()

        assert response.status_code == 401, "Ожидался код ответа 401 (Unauthorized)"