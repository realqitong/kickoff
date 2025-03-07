from datetime import datetime

# 多语言配置
LANGUAGE_PROMPT = {
    "cn": {
        "welcome": "=== 阳历生日命理分析系统 ===",
        "select_lang": "请选择语言 / Select language (1-中文 2-English): ",
        "birthday_prompt": "请输入您的阳历生日（格式：YYYY-MM-DD），输入q退出：",
        "invalid_date": "日期格式错误，请使用YYYY-MM-DD格式",
        "unknown_constellation": "未知星座",
        "output_labels": {
            "birthdate": "出生日期",
            "constellation": "所属星座", 
            "traits": "核心特质",
            "lucky_num": "幸运数字",
            "advice": "人生建议",
            "life_num": "命理数字"
        },
        "exit_msg": "感谢使用！"
    },
    "en": {
        "welcome": "=== Solar Birthday Analysis System ===",
        "select_lang": "Choose language (1-Chinese 2-English): ",
        "birthday_prompt": "Enter your birth date (YYYY-MM-DD), 'q' to quit: ",
        "invalid_date": "Invalid date format, please use YYYY-MM-DD",
        "unknown_constellation": "Unknown",
        "output_labels": {
            "birthdate": "Birth Date",
            "constellation": "Constellation",
            "traits": "Key Traits",
            "lucky_num": "Lucky Number",
            "advice": "Advice",
            "life_num": "Life Path Number"
        },
        "exit_msg": "Thank you for using!"
    }
}

# 完整的星座数据（双语）
constellation_info = [
    {"cn": "摩羯座", "en": "Capricorn", "date_range": (12, 22, 1, 19)},
    {"cn": "水瓶座", "en": "Aquarius", "date_range": (1, 20, 2, 18)},
    {"cn": "双鱼座", "en": "Pisces", "date_range": (2, 19, 3, 20)},
    {"cn": "白羊座", "en": "Aries", "date_range": (3, 21, 4, 19)},
    {"cn": "金牛座", "en": "Taurus", "date_range": (4, 20, 5, 20)},
    {"cn": "双子座", "en": "Gemini", "date_range": (5, 21, 6, 21)},
    {"cn": "巨蟹座", "en": "Cancer", "date_range": (6, 22, 7, 22)},
    {"cn": "狮子座", "en": "Leo", "date_range": (7, 23, 8, 22)},
    {"cn": "处女座", "en": "Virgo", "date_range": (8, 23, 9, 22)},
    {"cn": "天秤座", "en": "Libra", "date_range": (9, 23, 10, 23)},
    {"cn": "天蝎座", "en": "Scorpio", "date_range": (10, 24, 11, 22)},
    {"cn": "射手座", "en": "Sagittarius", "date_range": (11, 23, 12, 21)},
]

# 完整的性格分析数据（双语）
personality_traits = {
    "摩羯座": {
        "cn": {"特质": ["务实", "耐心", "保守"], "幸运数字": 8, "建议": "适当放松自己"},
        "en": {"traits": ["Practical", "Patient", "Conservative"], "lucky": 8, "advice": "Learn to relax"}
    },
    "水瓶座": {
        "cn": {"特质": ["创新", "独立", "叛逆"], "幸运数字": 4, "建议": "重视团队合作"},
        "en": {"traits": ["Innovative", "Independent", "Rebellious"], "lucky": 4, "advice": "Value teamwork"}
    },
    "双鱼座": {
        "cn": {"特质": ["浪漫", "善良", "敏感"], "幸运数字": 7, "建议": "增强现实感"},
        "en": {"traits": ["Romantic", "Compassionate", "Sensitive"], "lucky": 7, "advice": "Stay grounded"}
    },
    "白羊座": {
        "cn": {"特质": ["勇敢", "热情", "冲动"], "幸运数字": 7, "建议": "三思而后行"},
        "en": {"traits": ["Brave", "Passionate", "Impulsive"], "lucky": 7, "advice": "Think before acting"}
    },
    "金牛座": {
        "cn": {"特质": ["稳重", "务实", "固执"], "幸运数字": 6, "建议": "保持灵活性"},
        "en": {"traits": ["Steady", "Practical", "Stubborn"], "lucky": 6, "advice": "Be more flexible"}
    },
    "双子座": {
        "cn": {"特质": ["机智", "善变", "好奇"], "幸运数字": 5, "建议": "培养专注力"},
        "en": {"traits": ["Witty", "Adaptable", "Curious"], "lucky": 5, "advice": "Focus on priorities"}
    },
    "巨蟹座": {
        "cn": {"特质": ["温柔", "敏感", "恋家"], "幸运数字": 2, "建议": "学会表达自己"},
        "en": {"traits": ["Gentle", "Sensitive", "Home-loving"], "lucky": 2, "advice": "Express yourself"}
    },
    "狮子座": {
        "cn": {"特质": ["自信", "慷慨", "霸道"], "幸运数字": 1, "建议": "保持谦逊态度"},
        "en": {"traits": ["Confident", "Generous", "Dominant"], "lucky": 1, "advice": "Stay humble"}
    },
    "处女座": {
        "cn": {"特质": ["细心", "谨慎", "挑剔"], "幸运数字": 5, "建议": "接受不完美"},
        "en": {"traits": ["Detail-oriented", "Cautious", "Critical"], "lucky": 5, "advice": "Accept imperfections"}
    },
    "天秤座": {
        "cn": {"特质": ["优雅", "公正", "犹豫"], "幸运数字": 6, "建议": "果断做决定"},
        "en": {"traits": ["Elegant", "Fair", "Indecisive"], "lucky": 6, "advice": "Make decisions promptly"}
    },
    "天蝎座": {
        "cn": {"特质": ["敏锐", "神秘", "极端"], "幸运数字": 9, "建议": "学会信任他人"},
        "en": {"traits": ["Perceptive", "Mysterious", "Intense"], "lucky": 9, "advice": "Learn to trust others"}
    },
    "射手座": {
        "cn": {"特质": ["乐观", "自由", "粗心"], "幸运数字": 3, "建议": "注意细节处理"},
        "en": {"traits": ["Optimistic", "Free-spirited", "Careless"], "lucky": 3, "advice": "Pay attention to details"}
    }
}

def get_constellation(month, day, lang):
    for constellation in constellation_info:
        start_month, start_day, end_month, end_day = constellation["date_range"]
        if (month == start_month and day >= start_day) or \
           (month == end_month and day <= end_day):
            return constellation[lang]
    return LANGUAGE_PROMPT[lang]["unknown_constellation"]

def calculate_life_number(date_str):
    try:
        return sum(int(c) for c in date_str if c.isdigit()) % 9 or 9
    except:
        return None

def main():
    # 语言选择
    lang_choice = input(LANGUAGE_PROMPT["cn"]["select_lang"]).strip()
    lang = "cn" if lang_choice == "1" else "en"
    
    print("\n" + LANGUAGE_PROMPT[lang]["welcome"])
    
    while True:
        birthday = input(f"\n{LANGUAGE_PROMPT[lang]['birthday_prompt']}").strip()
        if birthday.lower() == 'q':
            print(LANGUAGE_PROMPT[lang]["exit_msg"])
            break

        try:
            birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            print(LANGUAGE_PROMPT[lang]["invalid_date"])
            continue

        month = birth_date.month
        day = birth_date.day
        constellation = get_constellation(month, day, lang)
        
        if constellation == LANGUAGE_PROMPT[lang]["unknown_constellation"]:
            print(LANGUAGE_PROMPT[lang]["unknown_constellation"])
            continue

        # 获取本地化星座数据
        cn_name = next((item["cn"] for item in constellation_info if item[lang] == constellation), "未知")
        traits_data = personality_traits.get(cn_name, {})
        localized_data = traits_data.get(lang, {})
        
        life_number = calculate_life_number(birthday.replace("-", ""))
        
        # 显示结果
        labels = LANGUAGE_PROMPT[lang]["output_labels"]
        separator = "★"*20 if lang == "cn" else "☆"*20
        print(f"\n{separator}")
        print(f"{labels['birthdate']}: {birthday}")
        print(f"{labels['constellation']}: {constellation}")
        print(f"{labels['traits']}: {', '.join(localized_data.get('traits' if lang=='en' else '特质', []))}")
        print(f"{labels['lucky_num']}: {localized_data.get('lucky' if lang=='en' else '幸运数字', 'N/A')}")
        print(f"{labels['advice']}: {localized_data.get('advice' if lang=='en' else '建议', '')}")
        print(f"{labels['life_num']}: {life_number}")
        print(f"{separator}\n")

if __name__ == "__main__":
    main()