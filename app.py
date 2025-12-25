import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة LAI التعليمية", page_icon="💡", layout="centered")

# تنسيق CSS احترافي
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { direction: rtl; text-align: right; font-family: 'Cairo', sans-serif; }
    .stApp { background-color: #ffffff; }
    .welcome-box { text-align: center; padding: 40px; border-radius: 25px; background: #e0f4f8; border: 2px solid #00acc1; }
    .report-card { background: #f8f9fa; border-right: 8px solid #10a37f; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    .innovation-box { background: #fff3e0; border: 2px solid #fb8c00; padding: 25px; border-radius: 15px; margin-top: 20px; }
    .stButton > button { background: #00acc1; color: white; border-radius: 12px; font-weight: bold; width: 100%; height: 3em; }
    .advice-section { background: #e8f5e9; padding: 15px; border-radius: 10px; border-right: 5px solid #2e7d32; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = "login"
if 'user_name' not in st.session_state: st.session_state.user_name = ""
if 'is_finished' not in st.session_state: st.session_state.is_finished = False
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- بنك الأسئلة (5 لكل مادة) ---
quiz_data = {
    "لغتي": [("علامة رفع الأسماء الخمسة؟", ["الواو", "الألف"]), ("'ما أجمل السماء' أسلوب؟", ["تعجب", "نداء"]), ("همزة 'اسم'؟", ["وصل", "قطع"]), ("جمع 'قلم'؟", ["أقلام", "قلمون"]), ("الفاعل يكون؟", ["مرفوعاً", "منصوباً"])],
    "رياضيات": [("15 × 3؟", ["45", "35"]), ("جذر 64؟", ["8", "6"]), ("2^3 تساوي؟", ["8", "6"]), ("زوايا المربع؟", ["360", "180"]), ("نصف الـ 100؟", ["50", "25"])],
    "حاسب": [("ذاكرة مؤقتة؟", ["RAM", "ROM"]), ("نظام تشغيل؟", ["Windows", "Word"]), ("لغة الويب؟", ["HTML", "C++"]), ("يربط الشبكات؟", ["راوتر", "فأرة"]), ("أصغر وحدة تخزين؟", ["Bit", "Byte"])],
    "انقلش": [("I ___ a student", ["am", "is"]), ("Opposite of 'Fast'?", ["Slow", "Quick"]), ("Past of 'Go'?", ["Went", "Goes"]), ("Who cures people?", ["Doctor", "Pilot"]), ("We say: ___ Apple", ["An", "A"])],
    "علوم": [("رمز الأكسجين؟", ["O", "H"]), ("تحول السائل لغاز؟", ["تبخر", "تجمد"]), ("مركز المجموعة الشمسية؟", ["الشمس", "الأرض"]), ("قوة الجذب؟", ["الجاذبية", "الاحتلاك"]), ("تتنفس الأسماك بـ؟", ["الخياشيم", "الرئة"])]
}

# --- صفحة تسجيل الدخول ---
if st.session_state.page == "login":
    if st.session_state.is_finished:
        st.warning(f"عذراً {st.session_state.user_name}، لقد أتممتِ الاختبار مسبقاً.")
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

# --- صفحة الترحيب ---
elif st.session_state.page == "welcome":
    st.markdown(f"<div class='welcome-box'><h2>مرحباً المبدعة {st.session_state.user_name}</h2>", unsafe_allow_html=True)
    st.write("أنا LAI، مساعدكِ الذكي. سنقوم بتحليل مهاراتكِ واقتراح فكرة ريادية تناسبكِ.")
    if st.button("ابدأي رحلة التعلم والابتكار 🏁"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- صفحات الاختبار ---
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

# --- صفحة التقرير النهائي ---
elif st.session_state.page == "final_report":
    st.balloons()
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    weakest = min(st.session_state.scores, key=st.session_state.scores.get)
    
    st.markdown(f"## 📊 تقرير الأداء للطالبة: {st.session_state.user_name}")
    
    # تفصيل نقاط القوة
    st.markdown(f"<div class='report-card'><h3>🌟 نقطة قوتكِ: {strongest}</h3>", unsafe_allow_html=True)
    st.write("**كيف تزيدينها؟**")
    st.write(f"1. ابحثي عن مواضيع متقدمة في {strongest} خارج المنهج.\n2. ساعدي زميلاتكِ في فهم هذه المادة لترسيخ معلومتكِ.\n3. طبقي مفاهيم {strongest} في مشاريعكِ اليومية.")
    st.markdown("</div>", unsafe_allow_html=True)

    # تفصيل نقاط الضعف
    st.markdown(f"<div class='report-card' style='border-color: #f44336;'><h3>📉 مادة تحتاج تطوير: {weakest}</h3>", unsafe_allow_html=True)
    st.write("**كيف تحسنينها؟**")
    st.write(f"1. خصصي 30 دقيقة يومياً لمراجعة أساسيات {weakest}.\n2. شاهدي دروس التوضيح في منصة عين.\n3. استخدمي الخرائط الذهنية لتسهيل الحفظ.")
    st.markdown(f"<a href='https://ien.edu.sa/' target='_blank' style='color:#f44336; font-weight:bold;'>🔗 اضغطي هنا للانتقال لمنصة عين التعليمية</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("الذهاب إلى مختبر مُبتكر 💡"):
        st.session_state.page = "innovator"
        st.rerun()

# --- صفحة مُبتكر المحدثة ---
elif st.session_state.page == "innovator":
    st.session_state.is_finished = True
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown("<div class='innovation-box'>", unsafe_allow_html=True)
    st.title("💡 مختبر مُبتكر للريادة والابتكار")
    st.write("لأنكِ متميزة، أجيبي على هذه الأسئلة العلمية لنرسم ملامح مشروعكِ:")
    
    with st.form("innovator_form"):
        st.write("**1. ما هو أكثر تحدي يواجهكِ في مدرستكِ؟**")
        q1 = st.selectbox("", ["صعوبة الوصول للمعلومات", "التنظيم والوقت", "البيئة المدرسية"])
        st.write("**2. أي نوع من المشاريع تفضلين؟**")
        q2 = st.radio("", ["تطبيق ذكي", "جهاز ملموس", "خدمة مجتمعية"])
        st.write("**3. ما هو المجال الذي يثير فضولكِ؟**")
        interest = st.selectbox("", ["التقنية", "البيئة", "الصحة", "التعليم", "الطاقة"])
        
        if st.form_submit_button("استخرج فكرتي الريادية ✨"):
            st.success(f"أهلاً بالمبتكرة {st.session_state.user_name}! إليكِ فكرتكِ الحصرية:")
            st.markdown(f"### فكرة المشروع: 'منصة {interest} الذكية'")
            st.write(f"**الشرح:** دمج مهاراتكِ في **{strongest}** لإنشاء حل ذكي في مجال **{interest}**. مثلاً إذا كنتِ قوية في الرياضيات، ستقوم المنصة بحساب الأثر البيئي أو الصحي بدقة.")
            st.write(f"**أين يمكنكِ تنفيذها؟** يمكنكِ البدء في مسابقة 'إبداع' الوطنية، أو تقديم الفكرة لإدارة موهبة.")
            st.markdown("<div class='advice-section'><b>💡 نصيحة LAI الذهبية:</b> الابتكار لا يعني الكمال، ابدأي بنموذج بسيط وطوريه مع الوقت. ثقي بذكائكِ!</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><center><b>صُنع بواسطة المبرمجة جوري 👑</b></center>", unsafe_allow_html=True)
