import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة LAI التعليمية", page_icon="💡", layout="centered")

# تنسيق CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { direction: rtl; text-align: right; font-family: 'Cairo', sans-serif; }
    .stApp { background-color: #ffffff; }
    .welcome-box { text-align: center; padding: 40px; border-radius: 25px; background: #e0f4f8; border: 2px solid #00acc1; }
    .report-card { background: #f8f9fa; border-right: 8px solid #10a37f; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    .innovation-box { background: #fff3e0; border: 2px solid #fb8c00; padding: 25px; border-radius: 15px; margin-top: 20px; }
    .stButton > button { background: #00acc1; color: white; border-radius: 12px; font-weight: bold; width: 100%; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = "login"
if 'user_name' not in st.session_state: st.session_state.user_name = ""
if 'is_finished' not in st.session_state: st.session_state.is_finished = False
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- بنك الأسئلة ---
quiz_data = {
    "لغتي": [("علامة رفع الأسماء الخمسة؟", ["الالواو", "الألف"]), ("'ما أجمل السماء' أسلوب؟", ["تعجب", "نداء"]), ("همزة 'اسم'؟", ["وصل", "قطع"]), ("جمع 'قلم'؟", ["أقلام", "قلمون"]), ("الفاعل يكون؟", ["مرفوعاً", "منصوباً"])],
    "رياضيات": [("15 × 3؟", ["45", "35"]), ("جذر 64؟", ["8", "6"]), ("2^3 تساوي؟", ["8", "6"]), ("زوايا المربع؟", ["360", "180"]), ("نصف الـ 100؟", ["50", "25"])],
    "حاسب": [("ذاكرة مؤقتة؟", ["RAM", "ROM"]), ("نظام تشغيل؟", ["Windows", "Word"]), ("لغة الويب؟", ["HTML", "C++"]), ("يربط الشبكات؟", ["راوتر", "فأرة"]), ("أصغر وحدة تخزين؟", ["Bit", "Byte"])],
    "انقلش": [("I ___ a student", ["am", "is"]), ("Opposite of 'Fast'?", ["Slow", "Quick"]), ("Past of 'Go'?", ["Went", "Goes"]), ("Who cures people?", ["Doctor", "Pilot"]), ("We say: ___ Apple", ["An", "A"])],
    "علوم": [("رمز الأكسجين؟", ["O", "H"]), ("تحول السائل لغاز؟", ["تبخر", "تجمد"]), ("مركز المجموعة الشمسية؟", ["الشمس", "الأرض"]), ("قوة الجذب؟", ["الجاذبية", "الاحاحتلاك"]), ("تتنفس الأسماك بـ؟", ["الخياشيم", "الرئة"])]
}

# --- منطق الصفحات ---

# 1. صفحة تسجيل الدخول
if st.session_state.page == "login":
    if st.session_state.is_finished:
        st.warning(f"عذراً {st.session_state.user_name}، لقد أتممتِ الرحلة مسبقاً.")
    else:
        st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)
        st.image("https://img.freepik.com/free-vector/scientists-concept-illustration_114360-1011.jpg", width=350)
        st.markdown("<h1>أهلاً بكِ في منصة LAI</h1>", unsafe_allow_html=True)
        name = st.text_input("فضلاً، أدخلي اسمكِ الثلاثي للبدء:")
        if st.button("تسجيل ودخول 🚀"):
            if name:
                st.session_state.user_name = name
                st.session_state.page = "welcome"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# 2. صفحة الترحيب
elif st.session_state.page == "welcome":
    st.markdown(f"<div class='welcome-box'><h2>مرحباً المبدعة {st.session_state.user_name}</h2>", unsafe_allow_html=True)
    st.write("أنا LAI، ذكاؤكِ الاصطناعي المساعد. سنبدأ الآن رحلة تقييم المهارات.")
    if st.button("بدء الاختبار التفاعلي 🏁"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# 3. صفحات الاختبار
elif st.session_state.page.startswith("quiz_"):
    sub = st.session_state.page.replace("quiz_", "")
    subjects = list(quiz_data.keys())
    i = subjects.index(sub)
    
    st.markdown(f"### 📚 مادة {sub}")
    with st.form(f"form_{sub}"):
        score = 0
        for j, (q, opts) in enumerate(quiz_data[sub]):
            ans = st.radio(f"{j+1}. {q}", opts, key=f"{sub}_{j}")
            if ans == opts[0]: score += 1
        if st.form_submit_button("المادة التالية ➡️"):
            st.session_state.scores[sub] = score
            st.session_state.page = f"quiz_{subjects[i+1]}" if i+1 < len(subjects) else "final_report"
            st.rerun()

# 4. صفحة التقرير النهائي
elif st.session_state.page == "final_report":
    st.balloons()
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    weakest = min(st.session_state.scores, key=st.session_state.scores.get)
    
    st.markdown(f"## 📊 التقرير الذكي للطالبة: {st.session_state.user_name}")
    st.markdown(f"<div class='report-card'><h3>🌟 نقطة القوة: {strongest}</h3></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='report-card' style='border-color: #f44336;'><h3>📉 مادة للتطوير: {weakest}</h3></div>", unsafe_allow_html=True)
    
    st.markdown("### 📅 جدول المذاكرة")
    st.table({"اليوم": ["الأحد", "الاثنين", "الثلاثاء"], "التركيز": [f"مراجعة {weakest}", f"حل تمارين {weakest}", f"إبداع {strongest}"]})

    if st.button("الذهاب إلى مُبتكر 💡"):
        st.session_state.page = "innovator"
        st.rerun()

# 5. صفحة مُبتكر
elif st.session_state.page == "innovator":
    st.session_state.is_finished = True
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown("<div class='innovation-box'>", unsafe_allow_html=True)
    st.title("💡 مختبر مُبتكر للريادة")
    with st.form("innovator_form"):
        interest = st.selectbox("المجال المفضل؟", ["التقنية", "البيئة", "الصحة", "التعليم"])
        if st.form_submit_button("استخراج الفكرة الريادية ✨"):
            st.success(f"فكرتكِ: مشروع في مجال {interest} يعتمد على قوتك في {strongest}!")
            st.write("**شرح:** هذا المشروع يحل مشكلة واقعية باستخدام مهاراتك العلمية.")
            st.write("**أين تنفذ:** في مسابقة موهبة أو حاضنات الأعمال الناشئة.")
            st.info("**نصيحة:** ابدئي صغيرًا وفكري بعيدًا!")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><center><b>صُنع بواسطة المبرمجة جوري 👑</b></center>", unsafe_allow_html=True)
