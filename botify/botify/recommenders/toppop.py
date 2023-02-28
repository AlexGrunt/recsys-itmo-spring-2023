import random
from typing import List

from .random import Random
from .recommender import Recommender


class TopPop(Recommender):
    def __init__(self, tracks_redis, top_tracks: List[int]):
        self.random = Random(tracks_redis)
        self.top_tracks = top_tracks

    def recommend_next(self, user: int, prev_track: int, prev_track_time: float) -> int:
        # TODO: Implement TopPop: return random track from self.top_tracks
        return self.random.recommend_next(user, prev_track, prev_track_time)
