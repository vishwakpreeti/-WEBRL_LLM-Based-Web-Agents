def get_reward(current_url, expected_url_part):
    if expected_url_part in current_url:
        return 1  # Success reward
    else:
        return -1  # Failure penalty
