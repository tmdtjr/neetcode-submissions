class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)      # 내림차순 정렬
        
        fleet = 0
        prev_time = 0                 # 바로 앞 무리의 도착 시간 기준
        
        for pos, spd in pairs:
            time = (target - pos) / spd   # 이 차의 도착 시간
            if time > prev_time:          # 앞 무리보다 늦게 도착하면
                fleet += 1                # 못 따라잡음 → 새 무리!
                prev_time = time          # 기준 갱신
            # time <= prev_time 이면 따라잡음 → 흡수 (아무것도 안 함)
        
        return fleet