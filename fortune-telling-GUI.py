from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# 多语言配置
LANGUAGE_PROMPT = {
    "cn": {
        "birthday_prompt": "请输入生日 (YYYY-MM-DD):",
        "invalid_date": "输入的日期格式不正确，请使用 YYYY-MM-DD 格式。",
        "output_labels": {
            "advice": "分析结果",
            "birthdate": "出生日期",
            "constellation": "星座",
            "life_num": "生命数字"
        }
    },
    "en": {
        "birthday_prompt": "Please enter your birthday (YYYY-MM-DD):",
        "invalid_date": "Invalid date format. Please use YYYY-MM-DD format.",
        "output_labels": {
            "advice": "Analysis Result",
            "birthdate": "Birthdate",
            "constellation": "Constellation",
            "life_num": "Life Number"
        }
    }
}

# 星座数据
constellation_info = [
    {"cn": "摩羯座", "en": "Capricorn"},
    {"cn": "水瓶座", "en": "Aquarius"},
    {"cn": "双鱼座", "en": "Pisces"},
    {"cn": "白羊座", "en": "Aries"},
    {"cn": "金牛座", "en": "Taurus"},
    {"cn": "双子座", "en": "Gemini"},
    {"cn": "巨蟹座", "en": "Cancer"},
    {"cn": "狮子座", "en": "Leo"},
    {"cn": "处女座", "en": "Virgo"},
    {"cn": "天秤座", "en": "Libra"},
    {"cn": "天蝎座", "en": "Scorpio"},
    {"cn": "射手座", "en": "Sagittarius"}
]

# 性格分析数据（可根据需要补充）
# ...

# 完整的当日运势数据（双语，详细描述）
daily_fortune = {
    "摩羯座": {
        "cn": {
            "爱情": "今日爱情运势不错，单身者可能会有浪漫的邂逅，不妨多参加社交活动；有伴侣者感情甜蜜，可安排一些小惊喜增进感情。",
            "事业": "事业运势极佳，工作上的努力会得到认可，可能会有新的项目机会降临，好好把握。",
            "健康": "健康状况良好，只需注意保持规律的作息和适量的运动。",
            "财运": "财运平稳，有小的进账机会，但要注意理性消费，避免不必要的开支。"
        },
        "en": {
            "love": "Your love fortune is quite good today. Singles may have a romantic encounter. It's advisable to participate in more social activities. Those in a relationship will enjoy a sweet relationship. You can arrange some small surprises to enhance your bond.",
            "career": "Your career fortune is excellent. Your hard work at work will be recognized, and there may be new project opportunities. Seize them well.",
            "health": "Your health condition is good. Just pay attention to maintaining regular work and rest and proper exercise.",
            "wealth": "Your wealth fortune is stable. There are small opportunities for income, but be careful with your spending and avoid unnecessary expenses."
        }
    },
    "水瓶座": {
        "cn": {
            "爱情": "爱情运势有起伏，单身者可能会遇到心仪的对象，但交流时可能会有些小误会；有伴侣者可能会因为小事发生争吵，需多沟通理解。",
            "事业": "事业上会遇到一些挑战，但只要保持积极的心态，努力克服困难，会有不错的进展。",
            "健康": "要注意休息，避免过度劳累，以免影响身体健康。",
            "财运": "财运一般，可能会有一些意外的支出，要做好预算规划。"
        },
        "en": {
            "love": "Your love fortune has ups and downs. Singles may meet someone they like, but there may be some small misunderstandings during communication. Those in a relationship may have a quarrel over small things. You need to communicate and understand more.",
            "career": "You will encounter some challenges at work. As long as you maintain a positive attitude and work hard to overcome difficulties, there will be good progress.",
            "health": "Pay attention to rest and avoid overwork, so as not to affect your health.",
            "wealth": "Your wealth fortune is average. There may be some unexpected expenses. Make a good budget plan."
        }
    },
    "双鱼座": {
        "cn": {
            "爱情": "爱情甜蜜温馨，单身者可能会收到他人的表白；有伴侣者感情更加深厚，可一起度过浪漫的时光。",
            "事业": "事业运势较好，工作上会有新的灵感和创意，能得到同事和上司的认可。",
            "健康": "健康状况良好，心情愉悦有助于身体健康。",
            "财运": "财运不错，可能会有意外之财降临，可适当进行一些小投资。"
        },
        "en": {
            "love": "Your love is sweet and warm. Singles may receive a confession from someone. Those in a relationship will have a deeper relationship. You can spend a romantic time together.",
            "career": "Your career fortune is good. You will have new inspiration and creativity at work and be recognized by your colleagues and superiors.",
            "health": "Your health condition is good. A happy mood is conducive to your health.",
            "wealth": "Your wealth fortune is good. There may be unexpected income. You can make some small investments appropriately."
        }
    },
    "白羊座": {
        "cn": {
            "爱情": "爱情运势旺盛，单身者积极主动出击，可能会收获爱情；有伴侣者感情升温，充满激情。",
            "事业": "事业上冲劲十足，能高效完成工作任务，可能会得到晋升的机会。",
            "健康": "注意运动时的安全，避免受伤。",
            "财运": "财运亨通，有机会获得丰厚的收入，但也要注意理财。"
        },
        "en": {
            "love": "Your love fortune is strong. Singles who take the initiative may find love. Those in a relationship will have a more passionate relationship.",
            "career": "You have plenty of energy at work and can complete tasks efficiently. There may be opportunities for promotion.",
            "health": "Pay attention to safety during exercise to avoid injuries.",
            "wealth": "Your wealth fortune is prosperous. You have the opportunity to earn a substantial income, but also pay attention to financial management."
        }
    },
    "金牛座": {
        "cn": {
            "爱情": "爱情运势平稳，单身者可通过朋友介绍认识新的异性；有伴侣者感情稳定，相互支持。",
            "事业": "事业上按部就班，稳步前进，会有不错的业绩。",
            "健康": "注意饮食均衡，避免暴饮暴食。",
            "财运": "财运稳定，适合储蓄和稳健投资。"
        },
        "en": {
            "love": "Your love fortune is stable. Singles can meet new people through friends. Those in a relationship will have a stable relationship and support each other.",
            "career": "You are making steady progress at work and will achieve good results.",
            "health": "Pay attention to a balanced diet and avoid overeating.",
            "wealth": "Your wealth fortune is stable. It is suitable for saving and conservative investments."
        }
    },
    "双子座": {
        "cn": {
            "爱情": "爱情运势多变，单身者可能会同时遇到多个有好感的对象，需谨慎选择；有伴侣者可能会因为沟通问题产生矛盾。",
            "事业": "事业上思维活跃，能提出新颖的想法，但要注意执行力。",
            "健康": "注意调节情绪，避免焦虑和压力过大。",
            "财运": "财运一般，开支可能会比较多，要合理安排资金。"
        },
        "en": {
            "love": "Your love fortune is changeable. Singles may meet several people they like at the same time. You need to choose carefully. Those in a relationship may have conflicts due to communication problems.",
            "career": "You have an active mind at work and can come up with novel ideas, but pay attention to execution.",
            "health": "Pay attention to regulating your emotions and avoid excessive anxiety and stress.",
            "wealth": "Your wealth fortune is average. There may be more expenses. Arrange your funds reasonably."
        }
    },
    "巨蟹座": {
        "cn": {
            "爱情": "爱情温馨甜蜜，单身者可能会在家庭聚会或朋友活动中遇到有缘人；有伴侣者感情更加深厚，家庭氛围融洽。",
            "事业": "事业上注重细节，能把工作完成得很好，但可能会过于敏感，影响工作效率。",
            "健康": "注意肠胃健康，避免食用生冷食物。",
            "财运": "财运平稳，会有一些小的储蓄。"
        },
        "en": {
            "love": "Your love is warm and sweet. Singles may meet someone special at family gatherings or friend activities. Those in a relationship will have a deeper relationship and a harmonious family atmosphere.",
            "career": "You pay attention to details at work and can complete tasks well, but you may be too sensitive, which may affect your work efficiency.",
            "health": "Pay attention to your gastrointestinal health and avoid eating cold food.",
            "wealth": "Your wealth fortune is stable. You will have some small savings."
        }
    },
    "狮子座": {
        "cn": {
            "爱情": "爱情运势高涨，单身者魅力四射，容易吸引他人的注意；有伴侣者感情升温，备受宠爱。",
            "事业": "事业上有领导风范，能带领团队取得好成绩，可能会得到表彰和奖励。",
            "健康": "注意休息，避免过度劳累引发身体不适。",
            "财运": "财运不错，有机会获得额外的收入，但要避免盲目消费。"
        },
        "en": {
            "love": "Your love fortune is high. Singles are very charming and easy to attract others' attention. Those in a relationship will have a more passionate relationship and be well - loved.",
            "career": "You have leadership qualities at work and can lead the team to achieve good results. You may receive recognition and rewards.",
            "health": "Pay attention to rest and avoid physical discomfort caused by overwork.",
            "wealth": "Your wealth fortune is good. There is an opportunity to get extra income, but avoid blind consumption."
        }
    },
    "处女座": {
        "cn": {
            "爱情": "爱情运势平稳，单身者可通过学习或工作认识新的朋友；有伴侣者感情稳定，相互理解。",
            "事业": "事业上追求完美，工作认真负责，但可能会因为过于挑剔而给自己带来压力。",
            "健康": "注意眼部和颈椎健康，避免长时间使用电子设备。",
            "财运": "财运稳定，合理规划开支可有所结余。"
        },
        "en": {
            "love": "Your love fortune is stable. Singles can meet new friends through study or work. Those in a relationship will have a stable relationship and understand each other.",
            "career": "You pursue perfection at work and are serious and responsible, but you may put pressure on yourself because of being too picky.",
            "health": "Pay attention to your eye and cervical spine health and avoid using electronic devices for a long time.",
            "wealth": "Your wealth fortune is stable. You can have some savings by planning your expenses reasonably."
        }
    },
    "天秤座": {
        "cn": {
            "爱情": "爱情运势良好，单身者有机会参加社交活动，结识心仪的对象；有伴侣者感情甜蜜，相互陪伴。",
            "事业": "事业上善于协调人际关系，能解决工作中的矛盾，推动项目进展。",
            "健康": "注意保持良好的体态，避免久坐。",
            "财运": "财运不错，有机会获得他人的资助或合作机会。"
        },
        "en": {
            "love": "Your love fortune is good. Singles have the opportunity to participate in social activities and meet someone they like. Those in a relationship will have a sweet relationship and accompany each other.",
            "career": "You are good at coordinating interpersonal relationships at work and can solve conflicts and promote project progress.",
            "health": "Pay attention to maintaining a good posture and avoid sitting for a long time.",
            "wealth": "Your wealth fortune is good. There is an opportunity to get support from others or cooperation opportunities."
        }
    },
    "天蝎座": {
        "cn": {
            "爱情": "爱情运势神秘莫测，单身者可能会有意外的缘分降临；有伴侣者感情充满激情，但可能会有一些小猜疑。",
            "事业": "事业上有较强的洞察力，能发现工作中的问题并及时解决，可能会有新的突破。",
            "健康": "注意心理调节，避免情绪波动过大。",
            "财运": "财运较好，有机会获得投资收益，但要注意风险控制。"
        },
        "en": {
            "love": "Your love fortune is mysterious. Singles may have unexpected romantic encounters. Those in a relationship will have a passionate relationship, but there may be some small suspicions.",
            "career": "You have strong insight at work and can find and solve problems in time. There may be new breakthroughs.",
            "health": "Pay attention to psychological adjustment and avoid excessive mood swings.",
            "wealth": "Your wealth fortune is good. There is an opportunity to get investment income, but pay attention to risk control."
        }
    },
    "射手座": {
        "cn": {
            "爱情": "爱情运势乐观，单身者可尽情享受自由，有机会结识志同道合的朋友；有伴侣者感情轻松愉快，可一起旅行放松。",
            "事业": "事业上充满活力，勇于尝试新事物，可能会开拓新的业务领域。",
            "健康": "注意运动强度，避免运动损伤。",
            "财运": "财运平稳，开支合理，不会有太大的经济压力。"
        },
        "en": {
            "love": "Your love fortune is optimistic. Singles can enjoy their freedom and have the opportunity to meet like - minded friends. Those in a relationship will have a relaxed and happy relationship. You can travel together to relax.",
            "career": "You are full of energy at work and brave enough to try new things. You may open up new business areas.",
            "health": "Pay attention to the intensity of exercise and avoid sports injuries.",
            "wealth": "Your wealth fortune is stable. Your expenses are reasonable and there will be no great financial pressure."
        }
    }
}

# 获取星座函数
def get_constellation(month, day, lang):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return next(item[lang] for item in constellation_info if item["cn"] == "水瓶座")
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return next(item[lang] for item in constellation_info if item["cn"] == "双鱼座")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return next(item[lang] for item in constellation_info if item["cn"] == "白羊座")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return next(item[lang] for item in constellation_info if item["cn"] == "金牛座")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return next(item[lang] for item in constellation_info if item["cn"] == "双子座")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return next(item[lang] for item in constellation_info if item["cn"] == "巨蟹座")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return next(item[lang] for item in constellation_info if item["cn"] == "狮子座")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return next(item[lang] for item in constellation_info if item["cn"] == "处女座")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return next(item[lang] for item in constellation_info if item["cn"] == "天秤座")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return next(item[lang] for item in constellation_info if item["cn"] == "天蝎座")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return next(item[lang] for item in constellation_info if item["cn"] == "射手座")
    else:
        return next(item[lang] for item in constellation_info if item["cn"] == "摩羯座")

# 计算生命数字函数
def calculate_life_number(birthday):
    num = sum(int(i) for i in birthday)
    while num > 9:
        num = sum(int(i) for i in str(num))
    return num

class FortuneApp:
    def __init__(self, root):
        self.root = root
        self.lang = "cn"
        self.root.title("生日命理分析系统" if self.lang == "cn" else "Birthday Fortune Analysis System")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0")
        self.create_widgets()
        self.update_language()

    def create_widgets(self):
        # 语言选择
        self.lang_frame = ttk.Frame(self.root, style="TFrame")
        self.lang_frame.pack(pady=10)

        self.lang_var = tk.StringVar(value="1")
        ttk.Radiobutton(self.lang_frame, text="中文", variable=self.lang_var,
                        value="1", command=self.change_language, style="TRadiobutton").grid(row=0, column=0)
        ttk.Radiobutton(self.lang_frame, text="English", variable=self.lang_var,
                        value="2", command=self.change_language, style="TRadiobutton").grid(row=0, column=1)

        # 生日输入
        self.input_frame = ttk.Frame(self.root, style="TFrame")
        self.input_frame.pack(pady=10)

        self.date_label = ttk.Label(self.input_frame, style="TLabel")
        self.date_entry = ttk.Entry(self.input_frame, width=15, style="TEntry")
        self.submit_btn = ttk.Button(self.input_frame, text="分析", command=self.analyze, style="TButton")

        self.date_label.pack(side=tk.LEFT, padx=5)
        self.date_entry.pack(side=tk.LEFT, padx=5)
        self.submit_btn.pack(side=tk.LEFT, padx=5)

        # 结果显示
        self.result_frame = ttk.LabelFrame(self.root, text="分析结果", style="TLabelframe")
        self.result_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.result_labels = {
            "birthdate": ttk.Label(self.result_frame, style="TLabel"),
            "constellation": ttk.Label(self.result_frame, style="TLabel"),
            "life_num": ttk.Label(self.result_frame, style="TLabel"),
            "fortune": ttk.Label(self.result_frame, justify=tk.LEFT, style="TLabel")
        }

        for label in self.result_labels.values():
            label.pack(anchor=tk.W, padx=5, pady=2)

        # 界面美化
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("TEntry", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10))
        style.configure("TRadiobutton", background="#f0f0f0", font=("Arial", 10))
        style.configure("TLabelframe", background="#f0f0f0", font=("Arial", 12, "bold"))
        style.configure("TLabelframe.Label", background="#f0f0f0", font=("Arial", 12, "bold"))

    def update_language(self):
        self.lang = "cn" if self.lang_var.get() == "1" else "en"
        lang_data = LANGUAGE_PROMPT[self.lang]

        # 更新界面文字
        self.root.title("生日命理分析系统" if self.lang == "cn" else "Birthday Fortune Analysis System")
        self.result_frame.config(text=lang_data["output_labels"]["advice"])
        self.date_label.config(text=lang_data["birthday_prompt"])
        self.submit_btn.config(text=lang_data["output_labels"]["advice"])

        # 更新结果标签
        labels = lang_data["output_labels"]
        self.result_labels["birthdate"].config(text=f"{labels['birthdate']}: ")
        self.result_labels["constellation"].config(text=f"{labels['constellation']}: ")
        self.result_labels["life_num"].config(text=f"{labels['life_num']}: ")

    def change_language(self):
        self.update_language()

    def analyze(self):
        birthday = self.date_entry.get()
        if not birthday:
            messagebox.showerror("错误", LANGUAGE_PROMPT[self.lang]["invalid_date"])
            return
        try:
            birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("错误", LANGUAGE_PROMPT[self.lang]["invalid_date"])
            return

        month = birth_date.month
        day = birth_date.day
        constellation = get_constellation(month, day, self.lang)

        # 获取运势数据
        cn_name = next((item["cn"] for item in constellation_info if item[self.lang] == constellation), "未知")
        fortune_data = daily_fortune.get(cn_name, {}).get(self.lang, {})

        # 显示结果
        labels = LANGUAGE_PROMPT[self.lang]["output_labels"]
        life_number = calculate_life_number(birthday.replace("-", ""))

        # 更新界面显示
        self.result_labels["birthdate"].config(text=f"{labels['birthdate']}: {birthday}")
        self.result_labels["constellation"].config(text=f"{labels['constellation']}: {constellation}")
        self.result_labels["life_num"].config(text=f"{labels['life_num']}: {life_number}")

        # 显示当日运势
        fortune_text = "当日运势：\n" if self.lang == "cn" else "Daily Fortune:\n"
        for category, value in fortune_data.items():
            fortune_text += f"{category}: {value}\n"
        self.result_labels["fortune"].config(text=fortune_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FortuneApp(root)
    root.mainloop()