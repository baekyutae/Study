class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 시작 지점 색깔
        start_color = image[sr][sc]
        row = len(image)
        col = len(image[0])

        # 방문 여부 저장
        visited = set()

        # 색깔변환 함수
        def dfs(r,c):
            # image 범위 밖이면 안됨
            if not 0<= r < row or not 0<= c<col:
                return

            # 방문 했거나 시작 지점 색깔이랑 다르면 탐색 범위 아님
            if not image[r][c] == start_color or (r,c) in visited:
                return

            # 방문 가능하면 우선 방문 체크부터
            visited.add((r,c))
            image[r][c] = color # 위 if 문에서 걸렀으니 바로 color로 변환

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return

        # 변환시작
        dfs(sr,sc)
        #변환된 image 반환
        return image
