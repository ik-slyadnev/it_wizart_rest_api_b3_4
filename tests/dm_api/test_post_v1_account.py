from hamcrest import assert_that, has_properties

class TestPostV1Account:
    def test_post_v1_account(self, account_helper, prepare_user):
        """
        Тест проверяет успешную регистрацию нового пользователя
        """
        user = account_helper.register_new_user(prepare_user)

        assert_that(user, has_properties({
            'login': prepare_user.login,
            'email': prepare_user.email,
            'password': prepare_user.password
        }))