import os


def check_env(env_list):
    """Check that all environment variables in env_list are set."""
    missing_env = []
    for env_var in env_list:
        if env_var not in os.environ:
            missing_env.append(env_var)
    if missing_env:
        raise EnvironmentError(
            f"Missing environment variables: {', '.join(missing_env)}"
        )
