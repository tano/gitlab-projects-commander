def check_token(private_token):
    if private_token is None:
        print('please set GITLAB_PRIVATE_TOKEN environment variable')
        exit(1)