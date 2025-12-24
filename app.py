import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="LAI Battle Game", page_icon="⚔️", layout="centered")

# مظهر الأزرار والتنسيق
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3.5em; background-color: #2E86C1; color: white; font-weight: bold; font-size: 18px; }
    .stRadio > label { font-size: 20px !important; font-weight: bold; }
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
        {"q": "Choose the color of the Sky:", "options": ["Red", "Blue", "Green"], "a": "Blue"},
        {"q": "Opposite of 'Big':", "options": ["Small", "Long", "Fast"], "a": "Small"},
        {"q": "He ____ a student.", "options": ["am", "is", "are"], "a": "is"},
        {"q": "The plural of 'Cat':", "options": ["Cats", "Cates", "Catis"], "a": "Cats"},
        {"q": "Day after Monday:", "options": ["Sunday", "Tuesday", "Friday"], "a": "Tuesday"}
    ],
    "الحاسب": [
        {"q": "وحدة قياس سعة التخزين؟", "options": ["بايت", "متر", "جرام"], "a": "بايت"},
        {"q": "تعتبر الفأرة من وحدات؟", "options": ["الإخراج", "الإدخال", "المعالجة"], "a": "الإدخال"},
        {"q": "اختصار زر النسخ؟", "options": ["Ctrl+V", "Ctrl+C", "Ctrl+X"], "a": "Ctrl+C"},
        {"q": "يستخدم برنامج Word لـ؟", "options": ["الرسم", "كتابة النصوص", "الحسابات"], "a": "كتابة النصوص"},
        {"q": "شبكة تربط العالم ببعضه؟", "options": ["الإنترنت", "الإنترانت", "المودم"], "a": "الإنترنت"}
    ]
}

# --- شاشة البداية ---
if st.session_state.stage == "welcome":
    st.title("⚔️ تحدي الأبطال: معركة المعرفة")
    # تم وضع رابط صورة الولد المحارب التي أعجبتك
    st.image("https://img.freepik.com/free-vector/hero-character-fighting-monsters_23-2148471415.jpg", caption="كن أنت البطل في هذه المعركة التعليمية!")
    st.write("### هل أنتِ مستعدة لمواجهة التحدي؟")
    st.info("سوف تمرّين بـ 4 معارك، في كل معركة 5 أسئلة قوية!")
    if st.button("🚀 انطلق للمعركة!"):
        st.session_state.stage = "الرياضيات"
        st.rerun()

# --- منطق الأسئلة ---
elif st.session_state.stage in questions:
    subject = st.session_state.stage
    q_idx = st.session_state.current_q
    
    st.header(f"🛡️ معركة {subject}")
    st.progress((q_idx + 1) * 20) # شريط تقدم للمادة
    st.write(f"**التحدي رقم {q_idx + 1} من 5**")
    
    q_data = questions[subject][q_idx]
    user_choice = st.radio(q_data["q"], q_data["options"], key=f"{subject}_{q_idx}")
    
    if st.button("تأكيد الهجمة ⚔️"):
        if user_choice == q_data["a"]:
            st.session_state.scores[subject] += 1
            st.toast("إصابة مباشرة! ✅")
        else:
            st.toast("تصدى الوحش لهجمتك! ❌")
            
        if q_idx < 4:
            st.session_state.current_q += 1
            st.rerun()
        else:
            # الانتقال للمادة التالية
            subs = list(questions.keys())
            curr_idx = subs.index(subject)
            st.session_state.current_q = 0
            if curr_idx < len(subs) - 1:
                st.session_state.stage = subs[curr_idx + 1]
            else:
                st.session_state.stage = "final"
            st.rerun()

# --- التقرير النهائي والتحليل الذكي ---
elif st.session_state.stage == "final":
    st.title("🏆 وسام النصر وتحليل LAI")
    st.balloons()
    
    # عرض النتائج
    cols = st.columns(4)
    for i, (sub, score) in enumerate(st.session_state.scores.items()):
        cols[i].metric(label=sub, value=f"{score}/5")
    
    st.write("---")
    
    # تحديد أقوى وأضعف مادة
    sorted_scores = sorted(st.session_state.scores.items(), key=lambda x: x[1])
    weakest = sorted_scores[0]
    strongest = sorted_scores[-1]
    
    # 1. تحليل نقطة الضعف
    st.warning(f"💡 **تحليل LAI لنقاط الضعف:** مستواكِ في **{weakest[0]}** يحتاج إلى تطوير (درجتك: {weakest[1]}/5)")
    st.write(f"لتقوية سلاحكِ في {weakest[0]}، ننصحكِ بمراجعة المصادر التالية:")
    st.info(f"🔗 [اضغطي هنا لزيارة منصة عين التعليمية - دروس {weakest[0]}](https://ien.edu.sa)")
    
    # 2. تحليل نقطة القوة
    st.success(f"🌟 **تحليل LAI لنقاط القوة:** أنتِ محاربة أسطورية في **{strongest[0]}**! (درجتك: {strongest[1]}/5)")
    st.write(f"لزيادة مهاراتكِ وتصبحين خبيرة، ننصحكِ بتجربة مشاريع عملية:")
    st.write("- حاولي شرح الدروس لزميلاتك لترسيخ المعلومة.")
    st.write("- ابحثي عن تحديات عالمية في هذا المجال لتطوير قدراتكِ.")

    if st.button("🔄 إعادة المعركة من جديد"):
        st.session_state.stage = "welcome"
        st.session_state.current_q = 0
        st.session_state.scores = {k: 0 for k in st.session_state.scores}
        st.rerun()
