import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="LAI Battle Game", page_icon="⚔️", layout="centered")

# تنسيق الألوان والأزرار
st.markdown("""
    <style>
    .stButton > button { width: 100%; border-radius: 20px; height: 3.5em; background-color: #E74C3C; color: white; font-weight: bold; font-size: 18px; border: none; }
    .stButton > button:hover { background-color: #C0392B; border: 2px solid white; }
    .stRadio > label { font-size: 20px !important; font-weight: bold; color: #2C3E50; }
    footer {visibility: hidden;}
    .footer-text { position: fixed; bottom: 10px; width: 100%; text-align: center; color: #7f8c8d; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة اللعبة
if 'stage' not in st.session_state:
    st.session_state.stage = "welcome"
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"الرياضيات": 0, "العلوم": 0, "الإنجليزي": 0, "الحاسب": 0}

# الأسئلة
questions = {
    "الرياضيات": [
        {"q": "5 + 7 = ?", "options": ["11", "12", "13"], "a": "12"},
        {"q": "ما هو ضعف العدد 8؟", "options": ["16", "14", "18"], "a": "16"},
        {"q": "100 - 45 = ?", "options": ["65", "55", "45"], "a": "55"},
        {"q": "3 × 9 = ?", "options": ["24", "27", "30"], "a": "27"},
        {"q": "نصف العدد 50 هو؟", "options": ["20", "25", "30"], "a": "25"}
    ],
    "العلوم": [
        {"q": "ما هو مركز المجموعة الشمسية؟", "options": ["الأرض", "الشمس", "القمر"], "a": "الشمس"},
        {"q": "مادة توجد في جميع الكائنات الحية؟", "options": ["الماء", "الحديد", "الذهب"], "a": "الماء"},
        {"q": "كم عدد كواكب المجموعة الشمسية؟", "options": ["7", "8", "9"], "a": "8"},
        {"q": "العضو المسؤول عن التنفس؟", "options": ["القلب", "الرئتان", "المعدة"], "a": "الرئتان"},
        {"q": "حالة الماء عندما يتجمد؟", "options": ["سائلة", "غازية", "صلبة"], "a": "صلبة"}
    ],
    "الإنجليزي": [
        {"q": "Color of the Sky:", "options": ["Red", "Blue", "Green"], "a": "Blue"},
        {"q": "Opposite of 'Big':", "options": ["Small", "Long", "Fast"], "a": "Small"},
        {"q": "He ____ a student.", "options": ["am", "is", "are"], "a": "is"},
        {"q": "Plural of 'Cat':", "options": ["Cats", "Cates", "Catis"], "a": "Cats"},
        {"q": "Day after Monday:", "options": ["Sunday", "Tuesday", "Friday"], "a": "Tuesday"}
    ],
    "الحاسب": [
        {"q": "وحدة قياس سعة التخزين؟", "options": ["بايت", "متر", "جرام"], "a": "بايت"},
        {"q": "الفأرة تعتبر وحدة؟", "options": ["إخراج", "إدخال", "معالجة"], "a": "إدخال"},
        {"q": "اختصار زر النسخ؟", "options": ["Ctrl+V", "Ctrl+C", "Ctrl+X"], "a": "Ctrl+C"},
        {"q": "يستخدم Word لـ؟", "options": ["الرسم", "كتابة النصوص", "الحسابات"], "a": "كتابة النصوص"},
        {"q": "شبكة تربط العالم؟", "options": ["الإنترنت", "الإنترانت", "المودم"], "a": "الإنترنت"}
    ]
}

# --- البداية ---
if st.session_state.stage == "welcome":
    st.title("⚔️ تحدي الأبطال: معركة المعرفة")
    # صورة المحارب
    st.image("https://cdn-icons-png.flaticon.com/512/3408/3408545.png", width=250)
    st.write("### هل أنتِ مستعدة لبدء المعركة الكبرى؟")
    if st.button("🚀 انطلقي الآن!"):
        st.session_state.stage = "الرياضيات"
        st.rerun()
    st.markdown('<div class="footer-text">المطورة المبدعة: الجوري ✨</div>', unsafe_allow_html=True)

# --- الأسئلة ---
elif st.session_state.stage in questions:
    subject = st.session_state.stage
    q_idx = st.session_state.current_q
    st.header(f"🛡️ معركة {subject}")
    q_data = questions[subject][q_idx]
    user_choice = st.radio(q_data["q"], q_data["options"], key=f"{subject}_{q_idx}")
    if st.button("تأكيد الهجمة ⚔️"):
        if user_choice == q_data["a"]:
            st.session_state.scores[subject] += 1
            st.toast("إصابة مباشرة! ✅")
        if q_idx < 4:
            st.session_state.current_q += 1
        else:
            subs = list(questions.keys())
            idx = subs.index(subject)
            st.session_state.current_q = 0
            st.session_state.stage = subs[idx+1] if idx < 3 else "final"
        st.rerun()

# --- التحليل النهائي وروابط التحسين ---
elif st.session_state.stage == "final":
    st.title("🏆 وسام النصر وتحليل LAI")
    st.balloons()
    
    # تحديد أقوى وأضعف مادة
    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1])
    weakest = sorted_scores[0]
    strongest = sorted_scores[-1]

    for sub, score in st.session_state.scores.items():
        st.write(f"**{sub}:** {score}/5")
        st.progress(score * 20)
    
    st.write("---")
    # تحليل الضعف والروابط
    st.error(f"⚠️ **تحتاجين تطوير في {weakest[0]}**")
    st.write(f"لتحسين مستواكِ في {weakest[0]}، اضغطي هنا: [منصة عين التعليمية](https://ien.edu.sa)")
    
    # تحليل القوة
    st.success(f"🌟 **أنتِ أسطورية في {strongest[0]}!**")
    st.write("استمري في تطوير نفسكِ ومساعدة زميلاتك.")

    if st.button("🔄 العودة للبداية"):
        st.session_state.stage = "welcome"
        st.session_state.current_q = 0
        st.session_state.scores = {k: 0 for k in st.session_state.scores}
        st.rerun()
