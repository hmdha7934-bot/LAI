import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="LAI | المنصة التعليمية", page_icon="🎓", layout="centered")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #333; font-family: 'Arial'; }
    .welcome-card { text-align: center; padding: 50px; border-radius: 20px; background: #f0fdf4; border: 2px solid #10a37f; }
    .stButton > button { background-color: #10a37f; color: white; border-radius: 20px; width: 100%; height: 3em; font-size: 18px; }
    .report-card { background: #f8f9fa; border-right: 10px solid #10a37f; padding: 20px; border-radius: 10px; direction: rtl; }
    .ai-advice { background: #fff4e5; border-right: 10px solid #ff9800; padding: 15px; border-radius: 10px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة (State Management)
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- 1. الصفحة الترحيبية ---
if st.session_state.page == "welcome":
    st.markdown("<div class='welcome-card'>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3462/3462151.png", width=150) # صورة شخصية طالبة
    st.markdown("<h1 style='color: #10a37f;'>مرحباً بكِ في منصة LAI</h1>", unsafe_allow_html=True)
    st.write("أنا مساعدكِ الذكي، سأقوم بتحليل أدائكِ الدراسي ومساعدتكِ لتكوني الأفضل!")
    if st.button("ابدأ الرحلة التعليمية 🚀"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. نظام الاختبار التتابعي ---
subjects = ["لغتي", "رياضيات", "حاسب", "انقلش", "علوم"]
questions = {
    "لغتي": [("مبتدأ جملة 'العلمُ نورٌ' هو:", ["العلم", "نور"]), ("نوع التنوين في 'كتابٌ':", ["ضم", "فتح"])],
    "رياضيات": [("9 × 9 يساوي:", ["81", "72"]), ("ناتج 100 ÷ 4:", ["25", "50"])],
    "حاسب": [("وحدة المعالجة المركزية هي:", ["CPU", "RAM"]), ("تعتبر الفأرة وحدة:", ["إدخال", "إخراج"])],
    "انقلش": [("Opposite of 'Happy':", ["Sad", "Angry"]), ("She ___ playing:", ["is", "am"])],
    "علوم": [("مركز المجموعة الشمسية:", ["الشمس", "الأرض"]), ("تتنفس الأسماك بواسطة:", ["الخياشيم", "الرئتين"])]
}

for i, sub in enumerate(subjects):
    if st.session_state.page == f"quiz_{sub}":
        st.markdown(f"<h2 style='text-align:right;'>📝 اختبار مادة: {sub}</h2>", unsafe_allow_html=True)
        with st.form(f"form_{sub}"):
            score = 0
            for q, opts in questions[sub]:
                ans = st.radio(q, opts)
                if ans == opts[0]: score += 1
            
            if st.form_submit_button("المادة التالية ➡️"):
                st.session_state.scores[sub] = score
                next_page = f"quiz_{subjects[i+1]}" if i+1 < len(subjects) else "final_report"
                st.session_state.page = next_page
                st.rerun()

# --- 3. صفحة التقرير النهائي الذكي ---
if st.session_state.page == "final_report":
    st.markdown("<h2 style='text-align:center;'>📊 تقرير LAI المخصص لكِ</h2>", unsafe_allow_html=True)
    
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    weakest = min(st.session_state.scores, key=st.session_state.scores.get)

    # عرض نقاط القوة
    st.markdown(f"<div class='report-card'><h3>🌟 نقطة قوتكِ: {strongest}</h3>", unsafe_allow_html=True)
    st.write(f"أنتِ متميزة جداً في {strongest}! ذكاؤكِ في هذا المجال يسمح لكِ بالابتكار.")
    st.markdown("<b>كيف تنمينها؟</b><br>نصيحة LAI: شاركي في المسابقات المدرسية وقومي بشرح الدروس لزميلاتكِ لترسيخ المعلومة أكثر.", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # عرض نقاط الضعف
    st.markdown(f"<div class='report-card' style='border-color: #ff4b4b; margin-top: 20px;'><h3>📈 مادة تحتاج تطوير: {weakest}</h3>", unsafe_allow_html=True)
    st.write(f"لاحظتُ وجود بعض التحديات في {weakest}. لا بأس، هذا جزء من التعلم!")
    st.markdown(f"<b>خطة التحسين:</b><br>1. مراجعة القواعد الأساسية لـ {weakest}.<br>2. حل تمرين واحد يومياً قبل النوم.<br>3. مشاهدة فيديوهات شرح تفاعلية.", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # الشروحات والنصائح (AI Advice)
    st.markdown("<div class='ai-advice'><b>💡 نصيحة LAI العامة:</b><br>تذكري أن العقل مثل العضلة، ينمو بالتدريب. خصصي وقتاً للراحة لتنشيط ذاكرتكِ.</div>", unsafe_allow_html=True)

    # جدول المذاكرة التعليمي
    st.write("---")
    st.markdown("### 📅 جدولكِ التعليمي المخصص (بناءً على تحليلي)")
    
    st.table({
        "اليوم": ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس"],
        "مادة التركيز (ضعيفة)": [weakest, weakest, "مراجعة شاملة", weakest, "اختبار تجريبي"],
        "مادة الإبداع (قوية)": [strongest, "مشروع علمي", strongest, "قراءة إثرائية", strongest]
    })

    if st.button("إعادة التحليل من جديد 🔄"):
        st.session_state.page = "welcome"
        st.session_state.scores = {k: 0 for k in st.session_state.scores}
        st.rerun()

st.markdown("<center style='color:#999; margin-top:50px;'>تطوير: الجوري 👑 - منصة LAI التعليمية</center>", unsafe_allow_html=True)
