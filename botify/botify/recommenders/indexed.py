import random

from .random import Random
from .recommender import Recommender


class Indexed(Recommender):
    def __init__(self, tracks_redis, recommendations_redis, catalog):
        self.recommendations_redis = recommendations_redis
        self.fallback = Random(tracks_redis)
        self.catalog = catalog

    def recommend_next(self, user: int, prev_track: int, prev_track_time: float) -> int:
        # TODO: Load recommendations for the user from recommendations_redis Redis.
        # TODO: Return random recommendation from the loaded list.
        # TODO: If no recommendations found for the user, fallback to random.
        return self.fallback.recommend_next(user, prev_track, prev_track_time)
