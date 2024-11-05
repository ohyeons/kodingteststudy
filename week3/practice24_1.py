#치킨 쿠폰

def solution(chicken):
    chicken_sum = 0  
    
    while chicken >= 10:
        service = chicken // 10
        chicken = chicken % 10 + service
        chicken_sum += service  
        
    return chicken_sum  