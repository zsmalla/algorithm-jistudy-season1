import sys
input = sys.stdin.readline

def get_distance(p1 : list[int], p2 : list[int]) -> int:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def split(tmp_points : list[int]) -> int:
    if len(tmp_points) < 2:
        return float('inf')
    elif len(tmp_points) == 2:
        return get_distance(*tmp_points)
    else:
        n = len(tmp_points) // 2
        min_dist = min(split(tmp_points[:n]), split(tmp_points[n:]))
        
        # x축 기준 후보 점 찾기
        target_x = []
        for i in range(len(tmp_points)):
            if (tmp_points[n][0] - tmp_points[i][0]) ** 2 < min_dist:
                target_x.append(tmp_points[i])

        # y축 기준 정렬
        target_x.sort(key=lambda x : x[1])

        # y 축 기준으로 후보 점들 사이의 거리 비교
        t = len(target_x)
        for i in range(t-1):
            for j in range(i+1, t):
                if (target_x[i][1] - target_x[j][1])**2 < min_dist:
                    min_dist = min(min_dist, get_distance(target_x[i], target_x[j]))
                else:
                    break
        return min_dist

def main() -> None:
    n = int(input())
    # https://my-coding-notes.tistory.com/103
    # TODO : 모든 점을 x 좌표를 기준으로 정렬
    # TODO : 점들의 중앙값을 기준으로 분할 -> 분할된 지점에 좌표가 2개 존재할 때까지 분할
    # TODO : 점 사이의 최소 거리를 찾고, 해당 거리보다 x좌표끼리 가까운 것만 후보 점으로 등록
    # TODO : y좌표 기준으로도 정룔 후 y좌표 차이가 최소 거리보다 낮은 것들만 대상으로 거리를 계산
    points = sorted([list(map(int, input().rstrip().split())) for _ in range(n)])
    print(split(points))


if __name__ == '__main__':
    main()
