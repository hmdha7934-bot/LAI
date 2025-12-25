 import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة LAI التعليمية", page_icon="🧪", layout="centered")

# تنسيق CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="st-"] { direction: rtl; text-align: right; font-family: 'Cairo', sans-serif; }
    .stApp { background-color: #ffffff; }
    .welcome-box { text-align: center; padding: 40px; border-radius: 25px; background: #e0f7fa; border: 2px solid #00acc1; }
    .stButton > button { background: #00acc1; color: white; border-radius: 12px; font-weight: bold; width: 100%; height: 3em; }
    .innovation-box { background: #fff3e0; border: 2px solid #fb8c00; padding: 25px; border-radius: 15px; margin-top: 20px; }
    .question-style { background: #f9f9f9; padding: 15px; border-radius: 10px; border-right: 5px solid #00acc1; margin-bottom: 10px; }
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
    st.markdown("<h4>المنصة الأولى لتمكين مهاراتك العلمية والريادية</h4>")
    if st.button("تفعيل محرك الذكاء الاصطناعي 🚀"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. بنك الأسئلة المكثف ---
quiz_data = {
    "لغتي": [
        ("ما هي علامة رفع الأسماء الخمسة؟", ["الواو", "الألف", "الضمة"]),
        ("نوع الأسلوب في 'ما أجمل السماء!':", ["تعجب", "استفهام", "نداء"]),
        ("الهمزة في كلمة 'اسم' هي همزة:", ["وصل", "قطع", "متطرفة"]),
        ("الاسم المجرور بعد حرف الجر يسمى:", ["مضافاً إليه", "اسماً مجروراً", "نعتاً"]),
        ("مرادف كلمة 'الجود':", ["الكرم", "الشجاعة", "الصدق"])
    ],
    "رياضيات": [
        ("ما هو ناتج 15 × 3؟", ["45", "35", "55"]),
        ("جذر العدد 64 هو:", ["8", "7", "6"]),
        ("قيمة (2^3) هي:", ["8", "6", "9"]),
        ("مجموع زوايا الشكل الرباعي:", ["360", "180", "90"]),
        ("الرقم 7 في العدد 1725 يمثل خانة:", ["المئات", "العشرات", "الألوف"])
    ],
    "حاسب": [
        ("الذاكرة التي تفقد محتواها عند انقطاع التيار:", ["RAM", "ROM", "HDD"]),
        ("أي مما يلي يعد نظام تشغيل؟", ["Windows", "Python", "Google"]),
        ("لغة تستخدم لبناء هيكل صفحات الويب:", ["HTML", "C++", "Java"]),
        ("جهاز يربط شبكات الحاسب ببعضها:", ["الراوتر", "الشاشة", "الطابعة"]),
        ("تعتبر الصور والفيديوهات من أنواع:", ["البيانات", "الأجهزة", "البرامج"])
    ],
    "انقلش": [
        ("___ you like coffee?", ["Do", "Does", "Is"]),
        ("The opposite of 'Fast' is:", ["Slow", "Quick", "Early"]),
        ("Past of 'Write' is:", ["Wrote", "Written", "Writes"]),
        ("A person who cures people is a:", ["Doctor", "Teacher", "Pilot"]),
        ("We use 'An' before:", ["Orange", "Book", "Car"])
    ],
    "علوم": [
        ("ما هو العنصر الكيميائي ورمزه O؟", ["أكسجين", "ذهب", "حديد"]),
        ("تتحول المادة من غاز إلى سائل بعملية:", ["التكثف", "التبخر", "الانصهار"]),
        ("الوحدة الأساسية لبناء الكائنات الحية:", ["الخلية", "العضو", "النسيج"]),
        ("قوة تجذب الأجسام نحو الأرض:", ["الجاذبية", "المغناطيسية", "الاحتكاك"]),
        ("كوكب زحل يشتهر بوجود:", ["حلقات", "براكين", "أنهار"])
    ]
}

# عرض الاختبار التتابعي
subjects = list(quiz_data.keys())
for i, sub in enumerate(subjects):
    if st.session_state.page == f"quiz_{sub}":
        st.markdown(f"### 📚 مادة {sub}: تقييم المستوى")
        with st.form(f"form_{sub}"):
            score = 0
            for j, (q, opts) in enumerate(quiz_data[sub]):
                ans = st.radio(f"{j+1}. {q}", opts, key=f"{sub}_{j}")
                if ans == opts[0]: score += 1
            if st.form_submit_button("انتقال للمادة التالية ➡️"):
                st.session_state.scores[sub] = score
                st.session_state.page = f"quiz_{subjects[i+1]}" if i+1 < len(subjects) else "final_report"
                st.rerun()

# --- 3. التقرير النهائي ---
if st.session_state.page == "final_report":
    st.balloons()
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"<div class='welcome-box'><h2>🎉 تهانينا! لقد اجتزتِ الاختبار بنجاح</h2>"
                f"<h3>مادة القوة لديكِ هي: {strongest}</h3></div>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 🚀 مُبتكر: بوابتك نحو الريادة")
    st.info("أنتِ الآن على بعد خطوة واحدة من الحصول على فكرتكِ الريادية المعتمدة على ذكائكِ.")
    if st.button("الذهاب إلى مُبتكر 💡"):
        st.session_state.page = "innovator"
        st.rerun()

# --- 4. صفحة مُبتكر (الأسئلة العلمية والريادية) ---
if st.session_state.page == "innovator":
    st.markdown("<div class='innovation-box'>", unsafe_allow_html=True)
    st.title("💡 مختبر الابتكار العلمي")
    st.write("أجيبي على هذه الأسئلة العلمية لكي يحدد LAI نوع الابتكار المناسب لكِ:")
    
    with st.form("innovator_form"):
        st.markdown("**[سؤال علمي 1]** ما هي الخطوة الأولى في المنهج العلمي؟")
        q1 = st.radio("", ["الملاحظة وطرح السؤال", "تحليل البيانات", "وضع الاستنتاج"])
        
        st.markdown("**[سؤال علمي 2]** أي من التالي يعتبر تقنية مستدامة؟")
        q2 = st.radio("", ["الطاقة الشمسية", "الوقود الأحفوري", "المحركات التقليدية"])
        
        st.markdown("**[سؤال ريادي]** ما هو المجال الذي تودين وضع بصمتكِ فيه؟")
        interest = st.selectbox("", ["التقنية", "البيئة", "الصحة", "التعليم", "الطاقة"])
        
        submit_innovation = st.form_submit_button("احصلي على فكرتكِ الأولى نحو الريادة ✨")
        
        if submit_innovation:
            with st.spinner("LAI يحلل مهاراتكِ العلمية والريادية..."):
                time.sleep(2)
                strongest = max(st.session_state.scores, key=st.session_state.scores.get)
                
                # منطق توليد الأفكار
                if interest == "التقنية":
                    idea = f"مشروع 'الخوارزمي الصغير' لدمج علوم {strongest} مع الذكاء الاصطناعي."
                elif interest == "البيئة":
                    idea = f"ابتكار نظام 'الري الذكي' القائم على معادلات {strongest} لتوفير المياه."
                elif interest == "الصحة":
                    idea = f"تطبيق 'نبض الذكاء' لتحليل مؤشرات {strongest} في الأجهزة الطبية."
                else:
                    idea = f"منصة 'ريادة {strongest}' لتقديم حلول في مجال {interest}."
                
                st.success(f"✅ فكرتكِ المقترحة: {idea}")
                st.markdown(f"**شرح الفكرة:** يعتمد هذا المشروع على نقاط قوتكِ في {strongest} ويطبقها في مجال {interest} لحل مشكلة عالمية بطريقة علمية.")
    
    st.markdown("</div>", unsafe_allow_html=True)
    if st.button("العودة للبداية"):
        st.session_state.page = "welcome"
        st.rerun()

st.markdown("<br><center><b>صُنع بواسطة المبرمجة جوري 👑</b></center>", unsafe_allow_html=True)
