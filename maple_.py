import random

def starforce_enforce(starforce = 0):
    """
    star_pos -> 시작 스타포스
    리턴값 -> 22성 성공 여부(bool)
    """
    destroy_persent = { 0 : 0
                    , 1 : 0
                    , 2 : 0
                    , 3 : 0
                    , 4 : 0
                    , 5 : 0
                    , 6 : 0
                    , 7 : 0
                    , 8 : 0
                    , 9 : 0
                    , 10 : 0
                    , 11 : 0
                    , 12 : 0.6
                    , 13 : 1.3
                    , 14 : 1.4
                    , 15 : 2.1
                    , 16 : 2.1
                    , 17 : 2.1
                    , 18 : 2.8
                    , 19 : 2.8
                    , 20 : 7.0
                    , 21 : 7.0
                        }

    success_persent = { 0 : 95
                    , 1 : 90
                    , 2 : 85
                    , 3 : 80
                    , 4 : 75
                    , 5 : 70
                    , 6 : 65
                    , 7 : 60
                    , 8 : 55
                    , 9 : 50
                    , 10 : 50
                    , 11 : 45
                    , 12 : 40
                    , 13 : 35
                    , 14 : 30
                    , 15 : 30
                    , 16 : 30
                    , 17 : 30
                    , 18 : 30
                    , 19 : 30
                    , 20 : 30
                    , 21 : 30
                        }

    fail_persent = {0 : 5
                ,1 : 10
                ,2 : 15
                ,3 : 20
                ,4 : 25
                ,5 : 30
                ,6 : 35
                ,7 : 40
                ,8 : 45
                ,9 : 50
                ,10 : 50
                ,11 : 55
                ,12 : 59.4
                ,13 : 63.7
                ,14 : 68.6
                ,15 : 67.9
                ,16 : 67.9
                ,17 : 67.9
                ,18 : 67.2
                ,19 : 67.2
                ,20 : 63.0
                ,21 : 63.0
                    }

    count = 0
    while True:
        random_num = random.random() * 100
                        # 0 ~ 100
        count += 1
        destroy = destroy_persent[starforce]
        success = success_persent[starforce]
        fail = fail_persent[starforce]
        if random_num <= destroy:
            #print(f"{count}번째에 터짐 아 돈만날림 {star_pos}")
            return False
        
        elif random_num <= destroy+success:
            #print(f"야 왠일 ? 성공 {star_pos}")
            starforce += 1 
        elif random_num:
            #print(f"실패함 {star_pos}")
            starforce -= 1

            if starforce == -1:
                starforce += 1

            if starforce == 9:
                starforce += 1

            if starforce == 14:
                starforce += 1
            
        if starforce == 22:
            #print(f"ㅋㅋㅋ 22성 달성 {count}만큼 도전함")
            return True

def cube_enforce(cube : str, start: str = "레어", end : str = "레전드리"):
    """
    큐브종류 -> 레드큐브, 블랙큐브, 수상한큐브, 장인의큐브, 명장의큐브
    스타트/엔드 -> 레어, 에픽, 유니크, 레전드리
    리턴값 -> 횟수(int), 가격(int)
    """
    cube_money = { "레드큐브" : 1250
            , "블랙큐브" : 2260
            , "수상한큐브" : 50
            , "장인의큐브" : 490
            , "명장의큐브" : 700}

    cube_persent_legend = { "레드큐브" : 0.3
            , "블랙큐브" : 1
            , "수상한큐브" : 0
            , "장인의큐브" : 0
            , "명장의큐브" : 0.1996 }

    cube_persent_unique = { "레드큐브" : 1.8
            , "블랙큐브" : 3.5
            , "수상한큐브" : 0
            , "장인의큐브" : 4.7619
            , "명장의큐브" : 1.6959}

    cube_persent_epic = { "레드큐브" : 6
            , "블랙큐브" : 15
            , "수상한큐브" : 0.9901
            , "장인의큐브" : 4.7619
            , "명장의큐브" : 7.9994}

    cube_grade_str = { "레어" : 1
                , "에픽" : 2
                , "유니크" : 3
                , "레전드리" : 4
    }

    cube_grade_num = { 1 : "레어"
                , 2 : "에픽"
                , 3 : "유니크"
                , 4 : "레전드리"
    }
    
    count = 0
    money = 0
    start_gread = cube_grade_str[start]
    end_gread = cube_grade_str[end]
    while True:
        persent = random.random() * 100
        count += 1 
        money += cube_money[cube]
        if start_gread == end_gread:
            break
        else:
            if start_gread == 1:
                if persent <= cube_persent_epic[cube]:
                    start_gread += 1
            elif start_gread == 2:
                if persent <= cube_persent_unique[cube]:
                    start_gread += 1
            elif start_gread == 3:
                if persent <= cube_persent_legend[cube]:
                    start_gread += 1
        
    return count, money
