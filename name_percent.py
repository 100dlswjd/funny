# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

JAEUM_DIC = { "ㄱ" : 2
            , "ㄴ" : 2
            , "ㄷ" : 3
            , "ㄹ" : 5
            , "ㅁ" : 4
            , "ㅂ" : 4
            , "ㅅ" : 2
            , "ㅇ" : 1
            , "ㅈ" : 3
            , "ㅊ" : 4
            , "ㅋ" : 3
            , "ㅌ" : 4
            , "ㅍ" : 4
            , "ㅎ" : 3
            , "ㄲ" : 4
            , "ㄸ" : 6
            , "ㅃ" : 8
            , "ㅆ" : 4
            , "ㅉ" : 6
            , 'ㄵ' : 5
            , 'ㄶ' : 5
            , 'ㄺ' : 7
            , 'ㄻ' : 9
            , 'ㄼ' : 9
            , 'ㄽ' : 7
            , 'ㄾ' : 9
            , 'ㄿ' : 9
            , 'ㅀ' : 8
            , 'ㅄ' : 9 }

MOEUM_DIC = {"ㅏ" : 2
            , "ㅑ" : 3
            , "ㅓ" : 2
            , "ㅕ" : 3
            , "ㅗ" : 2
            , "ㅛ" : 3
            , "ㅜ" : 2
            , "ㅠ" : 3
            , "ㅡ" : 1
            , "ㅣ" : 1
            , "ㅐ" : 3
            , "ㅒ" : 4
            , "ㅔ" : 3
            , "ㅖ" : 4
            , "ㅘ" : 4
            , "ㅙ" : 5
            , "ㅚ" : 3
            , "ㅝ" : 4
            , "ㅞ" : 5
            , "ㅟ" : 3
            , "ㅢ" : 2
            , " " : 0
            }


def name_divide(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        if '가'<=w<='힣':
            ch1 = (ord(w) - ord('가'))//588
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            pass
    return r_lst

def name_to(name : list):
    hap = list()
    for le in range(0,3):
        num = 0
        for lee in range(0,3):
            if lee == 0:
                num += JAEUM_DIC[name[le][lee]]
            else:
                num += MOEUM_DIC[name[le][lee]]
        
        hap.append(num)
    return hap

name_1 = name_divide("테스트")
number = name_to(name_1)
print(number)
