import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة LAI التعليمية", page_icon="🧪", layout="centered")

# تنسيق CSS لدعم العربية والجمالية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { direction: rtl; text-align: right; font-family: 'Cairo', sans-serif; }
    .stApp { background-color: #ffffff; }
    .welcome-box { text-align: center; padding: 40px; border-radius: 25px; background: #e0f7fa; border: 2px solid #00acc1; }
    .stButton > button { background: #00acc1; color: white; border-radius: 12px; font-weight: bold; width: 100%; height: 3em; }
    .report-card { background: #f8f9fa; border-right: 8px solid #10a37f; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    .innovation-box { background: #fff3e0; border: 2px solid #fb8c00; padding: 25px; border-radius: 15px; margin-top: 20px; }
    .link-style { color: #007c91; font-weight: bold; text-decoration: none; display: block; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- 1. الصفحة الترحيبية ---
if st.session_state.page == "welcome":
    st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/scientists-concept-illustration_114360-1011.jpg", width=400)
    st.markdown("<h1 style='color: #007c91;'>ابدأ رحلتك مع LAI</h1>", unsafe_allow_html=True)
    st.markdown("<h4>المنصة الأولى لتمكين مهاراتك العلمية والريادية بواسطة المبرمجة جوري</h4>")
    if st.button("تفعيل محرك الذكاء الاصطناعي 🚀"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. بنك الأسئلة ---
quiz_data = {
    "لغتي": [("علامة رفع الأسماء الخمسة؟", ["الالواو", "الألف"]), ("'ما أجمل السماء!' أسلوب؟", ["تعجب", "استفهام"]), ("همزة 'اسم' هي؟", ["وصل", "قطع"]), ("الاسم بعد حرف الجر؟", ["مجرور", "مرفوع"]), ("مرادف 'الجود'؟", ["الكرم", "البخل"])],
    "رياضيات": [("15 × 3؟", ["45", "35"]), ("جذر 64؟", ["8", "6"]), ("2^3 تساوي؟", ["8", "6"]), ("زوايا الرباعي؟", ["360", "180"]), ("7 في 1700 هي؟", ["مئات", "عشرات"])],
    "حاسب": [("ذاكرة تفقد محتواها؟", ["RAM", "ROM"]), ("نظام تشغيل؟", ["Windows", "Word"]), ("لغة بناء الويب؟", ["HTML", "C++"]), ("يربط الشبكات؟", ["راوتر", "شاشة"]), ("الفيديو يعتبر؟", ["بيانات", "أجهزة"])],
    "انقلش": [("___ you like tea?", ["Do", "Does"]), ("Opposite of 'Fast'?", ["Slow", "Quick"]), ("Past of 'Write'?", ["Wrote", "Written"]), ("Who cures people?", ["Doctor", "Pilot"]), ("We say: ___ Orange", ["An", "A"])],
    "علوم": [("رمز الأكسجين؟", ["O", "H"]), ("غاز إلى سائل؟", ["تكثف", "تبخر"]), ("وحدة بناء الكائن؟", ["الخلية", "العضو"]), ("قوة تجذبنا للأرض؟", ["الجاذبية", "الاحتكاك"]), ("كوكب له حلقات؟", ["زحل", "المريخ"])]
}

subjects = list(quiz_data.keys())
for i, sub in enumerate(subjects):
    if st.session_state.page == f"quiz_{sub}":
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

# --- 3. التقرير النهائي (نقاط القوة، الضعف، النصائح، الجدول، الروابط) ---
if st.session_state.page == "final_report":
    st.balloons()
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    weakest = min(st.session_state.scores, key=st.session_state.scores.get)
    
    st.markdown("<h2 style='text-align:center;'>📊 تقرير LAI الشامل</h2>", unsafe_allow_html=True)
    
    # نقاط القوة
    st.markdown(f"<div class='report-card'><h3>🌟 نقطة القوة: {strongest}</h3>", unsafe_allow_html=True)
    st.write(f"أنتِ متميزة جداً في {strongest}. ذكاؤكِ في هذا المجال هو مفتاحكِ للابتكار.")
    st.markdown(f"<a class='link-style' href='https://ien.edu.sa/'>🔗 اضغطي هنا لمحتوى إثرائي في {strongest}</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # نقاط الضعف
    st.markdown(f"<div class='report-card' style='border-color: #f44336;'><h3>📉 مادة للتطوير: {weakest}</h3>", unsafe_allow_html=True)
    st.write(f"تحتاجين لتركيز إضافي في {weakest}. LAI أعد لكِ مصادر للمراجعة.")
    st.markdown(f"<a class='link-style' style='color:#f44336;' href='https://ien.edu.sa/'>📚 مراجعة دروس {weakest} عبر عين</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # النصائح والجدول
    st.info("💡 **نصيحة LAI:** تذكري أن الاستمرارية سر النجاح. خصصي وقتكِ الأكبر للمادة التي تحتاج تطوير.")
    st.markdown("### 📅 جدولك الدراسي المقترح")
    st.table({"اليوم": ["الأحد", "الاثنين", "الثلاثاء"], "التركيز": [f"مراجعة {weakest}", f"حل تمارين {weakest}", f"إبداع في {strongest}"]})

    if st.button("الذهاب إلى مُبتكر 💡"):
        st.session_state.page = "innovator"
        st.rerun()

# --- 4. صفحة مُبتكر (الريادة) ---
if st.session_state.page == "innovator":
    st.markdown("<div class='innovation-box'>", unsafe_allow_html=True)
    st.title("💡 مختبر مُبتكر")
    st.write("أجيبي على الأسئلة العلمية للحصول على فكرتك الريادية:")
    with st.form("innovator_form"):
        st.markdown("**[سؤال علمي]** ما هي أول خطوات البحث العلمي؟")
        q1 = st.radio("", ["الملاحظة", "الاستنتاج"])
        st.markdown("**[سؤال ريادي]** ما هو المجال المفضل؟")
        interest = st.selectbox("", ["التقنية", "البيئة", "الصحة", "التعليم", "الطاقة"])
        if st.form_submit_button("احصلي على فكرتك ✨"):
            st.success(f"✅ فكرتك: مشروع ذكي يدمج {strongest} في مجال {interest}!")
            st.write("شرح: هذا المشروع سيحدث ثورة في السوق لأنه يستخدم قوة تحليل المعلومات لديكِ.")
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("العودة للبداية"):
        st.session_state.page = "welcome"
        st.rerun()

st.markdown("<br><center><b>صُنع بواسطة المبرمجة جوري 👑</b></center>", unsafe_allow_html=True)
