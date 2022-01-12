from collections import defaultdict

def solution(genres, plays):
    answer = []
    gen_play = defaultdict(int)
    song_list = defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        gen_play[genre] += play
        song_list[genre].append((play,idx))
        
    gen_play = sorted(gen_play.items(), key=lambda x: x[1], reverse=True)
    
    for key, val in gen_play:
        sorted_list = sorted(song_list[key], key=lambda x: (-x[0], x[1]))
        for song in sorted_list[:2]:
            answer.append(song[1])
        
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))