import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="LAI Battle Game", page_icon="⚔️", layout="centered")

# دالة لتنسيق الأزرار والمظهر
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #2E86C1; color: white; font-weight: bold; }
    .main { background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة اللعبة
if 'stage' not in st.session_state:
    st.session_state.stage = "welcome"
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'scores' not in st.session_state:
    st.session_state.scores = {"الرياضيات": 0, "العلوم": 0, "الإنجليزي": 0, "الحاسب": 0}

# قاعدة بيانات الأسئلة (5 لكل مادة)
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
        {"q": "Choose the color of the Sky:", ["Red", "Blue", "Green"], "a": "Blue"},
        {"q": "Opposite of 'Big':", ["Small", "Long", "Fast"], "a": "Small"},
        {"q": "He ____ a student.", ["am", "is", "are"], "a": "is"},
        {"q": "The plural of 'Cat':", ["Cats", "Cates", "Catis"], "a": "Cats"},
        {"q": "Day after Monday:", ["Sunday", "Tuesday", "Friday"], "a": "Tuesday"}
    ],
    "الحاسب": [
        {"q": "وحدة قياس سعة التخزين؟", "options": ["بايت", "متر", "جرام"], "a": "بايت"},
        {"q": "تعتبر الفأرة من وحدات؟", "options": ["الإخراج", "الإدخال", "المعالجة"], "a": "الإدخال"},
        {"q": "اختصار زر النسخ؟", "options": ["Ctrl+V", "Ctrl+C", "Ctrl+X"], "a": "Ctrl+C"},
        {"q": "يستخدم برنامج Word لـ؟", "options": ["الرسم", "كتابة النصوص", "الحسابات"], "a": "كتابة النصوص"},
        {"q": "شبكة تربط العالم ببعضه؟", "options": ["الإنترنت", "الإنترانت", "المودم"], "a": "الإنترنت"}
    ]
}

# --- منطق اللعبة ---

if st.session_state.stage == "welcome":
    st.title("⚔️ تحدي الأبطال: معركة المعرفة")
    st.image("https://img.freepik.com/free-vector/hero-character-fighting-monsters_23-2148471415.jpg") # صورة بطل يحارب
    st.write("### هل أنتِ مستعدة لمواجهة وحوش الجهل؟")
    st.info("لديكِ 4 معارك (مواد)، كل معركة بها 5 تحديات!")
    if st.button("🚀 ابدأ المعركة!"):
        st.session_state.stage = "الرياضيات"
        st.rerun()

elif st.session_state.stage in questions:
    subject = st.session_state.stage
    q_idx = st.session_state.current_q
    
    st.header(f"🛡️ معركة {subject}")
    st.write(f"**التحدي رقم {q_idx + 1} من 5**")
    
    current_q_data = questions[subject][q_idx]
    user_choice = st.radio(current_q_data["q"], current_q_data["options"], key=f"{subject}_{q_idx}")
    
    if st.button("تأكيد الهجمة ⚔️"):
        if user_choice == current_q_data["a"]:
            st.session_state.scores[subject] += 1
            st.toast("إصابة مباشرة! ✅")
        else:
            st.toast("حاول مرة أخرى في التحدي القادم ❌")
            
        if q_idx < 4:
            st.session_state.current_q += 1
            st.rerun()
        else:
            # الانتقال للمادة التالية
            subjects_list = list(questions.keys())
            current_sub_idx = subjects_list.index(subject)
            st.session_state.current_q = 0
            if current_sub_idx < len(subjects_list) - 1:
                st.session_state.stage = subjects_list[current_sub_idx + 1]
            else:
                st.session_state.stage = "final"
            st.rerun()

elif st.session_state.stage == "final":
    st.title("🏆 انتهاء المعركة - تقرير النصر")
    st.balloons()
    
    for sub, score in st.session_state.scores.items():
        st.write(f"**{sub}:** {score} من 5")
        st.progress(score * 20) # شريط طاقة للمادة
        
    weak_sub = min(st.session_state.scores, key=st.session_state.scores.get)
    if st.session_state.scores[weak_sub] < 3:
        st.warning(f"💡 المحارب يحتاج لتدريب إضافي في: {weak_sub}")
        st.write(f"إليكِ رابط لتقوية سلاحك في {weak_sub}: [اضغطي هنا](https://ien.edu.sa)")
    else:
        st.success("أنتِ محاربة أسطورية! مستواكِ مذهل في كل شيء.")

    if st.button("🔄 إعادة التحدي"):
        st.session_state.stage = "welcome"
        st.session_state.current_q = 0
        st.session_state.scores = {k: 0 for k in st.session_state.scores}
        st.rerun()
