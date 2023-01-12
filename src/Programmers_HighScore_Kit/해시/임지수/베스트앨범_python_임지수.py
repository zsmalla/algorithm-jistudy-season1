from collections import defaultdict
from heapq import heappush, heappop
def solution(genres, plays):
    music_dict = defaultdict(list)
    count_dict = defaultdict(int)
    result = []
    for genre,play in zip(genres, plays):
        count_dict[genre] += play
    for idx, genre, play in zip(range(len(genres)), genres, plays):
        heappush(music_dict[genre], (-play, idx))   # max heap
    for key, value in music_dict.items():
        for _ in range(2):
            play, idx = heappop(music_dict[key])
            result.append((count_dict[key], -play, idx))
            if not music_dict[key]:
                break
    return [idx for _, _, idx in sorted(result, key = lambda x : (-x[0], -x[1], x[2]))]