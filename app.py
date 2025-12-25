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
    .welcome-box { text-align: center; padding: 40px; border-radius: 25px; background: #f0fdf4; border: 2px solid #10a37f; }
    .stButton > button { background: #10a37f; color: white; border-radius: 12px; font-weight: bold; width: 100%; }
    .innovation-box { background: #fff4e5; border: 2px solid #ff9800; padding: 20px; border-radius: 15px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- 1. الصفحة الترحيبية ---
if st.session_state.page == "welcome":
    st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)
    st.image("https://img.freepik.com/free-vector/creative-idea-concept-with-lightbulb_23-2148154943.jpg", width=300)
    st.markdown("<h1 style='color: #10a37f;'>ابدأ رحلتك مع LAI</h1>", unsafe_allow_html=True)
    st.markdown("<h4>منصتكِ الذكية للتعلم والابتكار برؤية المبرمجة جوري</h4>", unsafe_allow_html=True)
    if st.button("انطلق الآن 🚀"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. الأسئلة التعليمية (مختصرة للبرمجة) ---
questions = {
    "لغتي": [("مبتدأ الجملة؟", ["اسم", "فعل"]), ("جمع طالب؟", ["طلاب", "طالبات"])],
    "رياضيات": [("5×5؟", ["25", "20"]), ("10+10؟", ["20", "30"])],
    "حاسب": [("لغة برمجة؟", ["Python", "Word"]), ("وحدة إدخال؟", ["الفأرة", "الشاشة"])],
    "انقلش": [("I ___ cold", ["am", "is"]), ("Color of sky?", ["Blue", "Red"])],
    "علوم": [("مصدر الضوء؟", ["الشمس", "القمر"]), ("تتنفس الأسماك بـ؟", ["الخياشيم", "الرئة"])]
}

subjects = list(questions.keys())
for i, sub in enumerate(subjects):
    if st.session_state.page == f"quiz_{sub}":
        st.markdown(f"### 📝 اختبار: {sub}")
        with st.form(f"form_{sub}"):
            ans1 = st.radio(questions[sub][0][0], questions[sub][0][1])
            ans2 = st.radio(questions[sub][1][0], questions[sub][1][1])
            if st.form_submit_button("التالي"):
                st.session_state.scores[sub] = (1 if ans1 == questions[sub][0][1][0] else 0) + (1 if ans2 == questions[sub][1][1][0] else 0)
                st.session_state.page = f"quiz_{subjects[i+1]}" if i+1 < len(subjects) else "final_report"
                st.rerun()

# --- 3. التقرير النهائي وزر الابتكار ---
if st.session_state.page == "final_report":
    st.balloons()
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"## 🏆 تم الاجتياز بنجاح! مادة قوتكِ هي: {strongest}")
    
    st.write("---")
    st.markdown("### 🚀 مُبتكر: ابدأ فكرتك الأولى نحو الريادة")
    st.write(f"بناءً على تميزك في مادة {strongest}، أنتِ الآن مؤهلة للدخول في مختبر الابتكار.")
    
    if st.button("الذهاب إلى مُبتكر 💡"):
        st.session_state.page = "innovator"
        st.rerun()

# --- 4. صفحة مُبتكر (الريادة) ---
if st.session_state.page == "innovator":
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown("<div class='innovation-box'>", unsafe_allow_html=True)
    st.title("💡 مختبر الابتكار الذكي")
    st.write(f"بما أنكِ مبدعة في **{strongest}**، دعينا نصمم فكرتك الريادية.")
    
    interest = st.selectbox("المجال الذي تهتمين به أكثر؟", ["التقنية", "البيئة", "الصحة", "التعليم", "الطاقة"])
    
    if st.button("احصلي على فكرتك من LAI ✨"):
        with st.spinner("جاري توليد فكرة عبقرية..."):
            time.sleep(2)
            if interest == "التقنية":
                idea = f"تطبيق ذكي يستخدم مهاراتك في {strongest} لتعليم الأطفال البرمجة بأسلوب قصصي."
            elif interest == "البيئة":
                idea = f"جهاز يعمل بتقنيات {strongest} لمراقبة جودة التربة وسقي النباتات تلقائياً."
            else:
                idea = f"منصة تفاعلية تربط مفاهيم {strongest} بحلول مبتكرة في مجال {interest}."
            
            st.success("✅ فكرتك المقترحة:")
            st.markdown(f"**{idea}**")
            st.info(f"**شرح الفكرة:** هذا المشروع يدمج قوتك في {strongest} مع شغفك بـ {interest} ليخلق حلاً ريادياً ينافس عالمياً.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("العودة للرئيسية"):
        st.session_state.page = "welcome"
        st.rerun()

st.markdown("<br><center><b>صُنع بواسطة المبرمجة جوري 👑</b></center>", unsafe_allow_html=True)
