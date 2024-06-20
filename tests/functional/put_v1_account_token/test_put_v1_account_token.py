def test_put_v1_account_token(account_helper, prepare_user):

    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    account_helper.register_user(login=login, email=email, password=password)
    account_helper.user_login(login=login, password=password)
