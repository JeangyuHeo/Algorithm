def solution(volume):
    min_surface_area = 1e9
    result = None
    
    for x in range(1, int(volume**(1/3))+2):
        yz = volume // x
        for y in range(1, int((yz**0.5))+1):
            for z in range(1, 51):
                cur_area = 2 * (x*y + y*z + x*z)
                if cur_area < min_surface_area and x*y*z >= volume:
                    min_surface_area = cur_area
                    result = [x,y,z]
                        
    return sorted(result)
        
if __name__ == "__main__":
    print("결과 값:",solution(100),"// 정답:", 455)
    print("결과 값:",solution(12345),"// 정답:", 212128)
    print("결과 값:",solution(125000),"// 정답:", 505050)
    print("결과 값:",solution(84938),"// 정답:", 424446)
    print("결과 값:",solution(35432),"// 정답:", 293436)