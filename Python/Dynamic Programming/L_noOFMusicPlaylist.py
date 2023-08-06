def numMusicPlaylists(no_of_songs: int, goal: int, cooldown: int) -> int:
    """Return number of playlist based on provided criteria

    Args:
        no_of_songs (int): _description_
        goal (int): _description_
        cooldown (int): _description_

    Returns:
        int: _description_
    """
    MOD = 10 ** 9 + 7
    cache = {}
    def count(current_goal, old_songs):
        if (current_goal, old_songs) in cache:
            return cache[(current_goal, old_songs)]
        if (current_goal == 0 and old_songs == no_of_songs):
            return 1
        if (current_goal == 0 or old_songs > no_of_songs):
            return 0
        current_playlist = (no_of_songs - old_songs) * count(current_goal - 1, old_songs + 1)
        if old_songs > cooldown:
            current_playlist += (old_songs - cooldown) * count(current_goal - 1, old_songs)
        cache[(current_goal, old_songs)] = current_playlist % MOD
        return cache[(current_goal, old_songs)]
    return count(goal, 0)
