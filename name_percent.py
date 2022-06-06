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
            , 'ㅄ' : 9
            , " " : 0 }

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
            }


def name_divide(korean_word) -> list:
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

def name_to_number(name : list) -> list:
    hap = list()
    for name_len in range(len(name)):
        num = 0
        for jaeum_moeum in range(0,3):
            if jaeum_moeum == 1:
                num += MOEUM_DIC[name[name_len][jaeum_moeum]]
            else:
                num += JAEUM_DIC[name[name_len][jaeum_moeum]]
        num = num%10
        hap.append(num)
    return hap

def number_general(nos_1 : list, nos_2 : list) -> list:
    result = list()
    maxlen = len(nos_1) if len(nos_1) >= len(nos_2) else len(nos_2)
    for stroke in range(maxlen):
        try:
            result.append(nos_1[stroke])
        except IndexError:
            pass
        try:
            result.append(nos_2[stroke])
        except IndexError:
            pass

    return result

def add_stroke(name_stroke : list ) -> int:
    idx = 0
    data = list()
    while True:
        try:
            number = name_stroke[idx] + name_stroke[idx+1]
            number = number%10
            data.append(number)
            idx += 1
        except IndexError:
            return data
    pass

def percent(name_stroke : list()):
    percent = add_stroke(name_stroke)
    while True:
        percent = add_stroke(percent)
        if len(percent) == 2:
            return (percent[0] * 10) + percent[1]

def name_percent(name_1 : str, name_2 : str):
    name_1_divide = name_divide(name_1)
    name_2_divide = name_divide(name_2)
    number1 = name_to_number(name_1_divide)
    number2 = name_to_number(name_2_divide)

    test = number_general(number1,number2)
    result = percent(test)
    return result

