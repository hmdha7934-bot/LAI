import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة LAI التعليمية", page_icon="🎓", layout="centered")

# تنسيق CSS لدعم اللغة العربية والجمالية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="st-"] {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    .stApp { background-color: #ffffff; }
    
    .welcome-box {
        text-align: center;
        padding: 40px;
        border-radius: 25px;
        background: linear-gradient(135deg, #e0f2f1 0%, #ffffff 100%);
        border: 2px solid #10a37f;
    }
    
    .stButton > button {
        background: #10a37f;
        color: white;
        border-radius: 12px;
        font-weight: bold;
    }
    
    .report-card {
        background: #f8f9fa;
        border-right: 8px solid #10a37f;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    
    .advice-box {
        background: #fff8e1;
        border: 1px dashed #ffb300;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- 1. الصفحة الترحيبية ---
if st.session_state.page == "welcome":
    st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)
    # صورة جديدة ومناسبة
    st.image("https://img.freepik.com/free-vector/hand-drawn-back-school-background_23-2149033374.jpg", width=350)
    st.markdown("<h1 style='color: #10a37f;'>مرحباً بكِ في منصة LAI</h1>", unsafe_allow_html=True)
    st.markdown("<h4>المستقبل يبدأ من هنا.. حللي مهاراتك مع ذكاء جوري الاصطناعي</h4>", unsafe_allow_html=True)
    if st.button("تفعيل LAI وابدأي الاختبار 🚀"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. بنك الأسئلة والروابط ---
questions = {
    "لغتي": [("علامة الرفع الأصلية؟", ["الضمة", "الفتحة"]), ("نوع 'يقرأ'؟", ["فعل", "اسم"]), ("جمع 'كتاب'؟", ["كتب", "كتابون"]), ("ضد 'الصدق'؟", ["الكذب", "الأمانة"]), ("الفاعل يكون دائماً؟", ["مرفوعاً", "منصوباً"])],
    "رياضيات": [("12×12؟", ["144", "124"]), ("زوايا المثلث؟", ["180", "360"]), ("نصف الـ 50؟", ["25", "20"]), ("5+5×2؟", ["15", "20"]), ("العدد الزوجي هو؟", ["2", "3"])],
    "حاسب": [("وحدة الإدخال؟", ["الفأرة", "الشاشة"]), ("اختصار الذكاء الاصطناعي؟", ["AI", "VR"]), ("عقل الحاسب؟", ["المعالج", "الرام"]), ("لغة برمجة؟", ["Python", "Word"]), ("شبكة عالمية؟", ["الإنترنت", "المحلية"])],
    "انقلش": [("I ___ happy", ["am", "is"]), ("Past of 'Eat'?", ["Ate", "Eaten"]), ("Color of grass?", ["Green", "Red"]), ("Plural of 'Boy'?", ["Boys", "Boies"]), ("Opposite of 'Hot'?", ["Cold", "Warm"])],
    "علوم": [("كوكب المريخ لونه؟", ["أحمر", "أزرق"]), ("غاز التنفس؟", ["أكسجين", "نيتروجين"]), ("أقرب كوكب؟", ["عطارد", "الأرض"]), ("حالة الثلج؟", ["صلبة", "سائلة"]), ("مصدر الضوء؟", ["الشمس", "القمر"])]
}

# --- 3. عرض الاختبار ---
subjects = list(questions.keys())
for i, sub in enumerate(subjects):
    if st.session_state.page == f"quiz_{sub}":
        st.markdown(f"<h2 style='text-align:center; color:#10a37f;'>📝 اختبار مادة: {sub}</h2>", unsafe_allow_html=True)
        with st.form(f"form_{sub}"):
            score = 0
            for j, (q, opts) in enumerate(questions[sub]):
                ans = st.radio(f"{j+1}. {q}", opts, key=f"{sub}_{j}")
                if ans == opts[0]: score += 1
            if st.form_submit_button("المادة التالية ➡️"):
                st.session_state.scores[sub] = score
                st.session_state.page = f"quiz_{subjects[i+1]}" if i+1 < len(subjects) else "final_report"
                st.rerun()

# --- 4. التقرير النهائي ---
if st.session_state.page == "final_report":
    st.balloons()
    st.markdown("<h1 style='text-align:center;'>📊 نتائج ذكاء جوري</h1>", unsafe_allow_html=True)
    
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    weakest = min(st.session_state.scores, key=st.session_state.scores.get)

    st.markdown(f"<div class='report-card'><h3>🌟 أنتِ مبدعة في: {strongest}</h3>", unsafe_allow_html=True)
    st.write("نصيحة LAI: مهاراتك هنا استثنائية! حاولي البحث عن تحديات أصعب لتكوني عالمة في هذا المجال.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='report-card' style='border-color: #ff4b4b;'><h3>📈 مادة تحتاج مراجعة: {weakest}</h3>", unsafe_allow_html=True)
    st.write(f"لا تقلقي يا بطلة، مادة {weakest} ستصبح سهلة مع التدريب اليومي.")
    
    # قسم النصائح
    st.markdown("<div class='advice-box'><b>💡 نصائح LAI الذهبية:</b><br>"
                "1. ابدأي بالمذاكرة في مكان هادئ وبعيد عن الجوال.<br>"
                "2. استخدمي الألوان في تلخيص دروسكِ.<br>"
                "3. اشرحي ما تعلمتِهِ لأي شخص، فهذا يثبت المعلومة 100%.</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 📅 جدول المذاكرة الذكي")
    st.table({"اليوم": ["الأحد", "الاثنين", "الثلاثاء"], "التركيز": [f"مراجعة {weakest}", f"تمارين {weakest}", f"إبداع في {strongest}"]})

    if st.button("إعادة الاختبار 🔄"):
        st.session_state.page = "welcome"
        st.session_state.scores = {k: 0 for k in st.session_state.scores}
        st.rerun()

st.markdown("<br><center><b>صُنع بواسطة المبرمجة جوري 👑</b></center>", unsafe_allow_html=True)
