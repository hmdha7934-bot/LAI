import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة LAI التعليمية", page_icon="🎓", layout="centered")

# تنسيق CSS لضمان عدم انعكاس الكلام ودعم اللغة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="st-"] {
        direction: rtl;
        text-align: right;
        font-family: 'Cairo', sans-serif;
    }
    .stApp { background-color: #ffffff; }
    
    /* تصميم البطاقة الترحيبية */
    .welcome-box {
        text-align: center;
        padding: 40px;
        border-radius: 25px;
        background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
        border: 2px solid #10a37f;
        box-shadow: 0 10px 20px rgba(16, 163, 127, 0.1);
    }
    
    /* تصميم الأزرار */
    .stButton > button {
        background: #10a37f;
        color: white;
        border-radius: 12px;
        width: 100%;
        height: 3.5em;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
    }
    
    /* تنسيق الراديو (الأسئلة) */
    .stRadio > div { direction: rtl; text-align: right; }
    
    .report-card {
        background: #f8f9fa;
        border-right: 8px solid #10a37f;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الحالة
if 'page' not in st.session_state: st.session_state.page = "welcome"
if 'scores' not in st.session_state: st.session_state.scores = {"لغتي": 0, "رياضيات": 0, "حاسب": 0, "انقلش": 0, "علوم": 0}

# --- 1. الصفحة الترحيبية ---
if st.session_state.page == "welcome":
    st.markdown("<div class='welcome-box'>", unsafe_allow_html=True)
    # صورة طالبة جديدة
    st.image("https://img.freepik.com/free-vector/cute-girl-studying-with-laptop-cartoon-vector-icon-illustration-people-technology-icon-concept_138676-4402.jpg", width=250)
    st.markdown("<h1 style='color: #10a37f;'>أهلاً بكِ في منصة LAI</h1>", unsafe_allow_html=True)
    st.markdown("<h3>أنا مساعدكِ الذكي، سأقوم بتحليل مهاراتكِ الدراسية وتطويرها.</h3>", unsafe_allow_html=True)
    if st.button("تفعيل الذكاء الاصطناعي وابدأ الاختبار 🚀"):
        st.session_state.page = "quiz_لغتي"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. بنك الأسئلة (5 لكل مادة) ---
questions = {
    "لغتي": [
        ("ما هي علامة الرفع الأصلية؟", ["الضمة", "الفتحة", "الكسرة"]),
        ("الكلمة التي تدل على 'فعل' هي:", ["يشرح", "المعلم", "في"]),
        ("جمع كلمة 'طالبة' هو:", ["طالبات", "طلاب", "طالبون"]),
        ("الجملة الاسمية تبدأ بـ:", ["اسم", "فعل", "حرف"]),
        ("مرادف كلمة 'جميل':", ["وسيم", "قبيح", "صغير"])
    ],
    "رياضيات": [
        ("ما ناتج 12 × 12؟", ["144", "124", "134"]),
        ("مجموع زوايا المثلث يساوي:", ["180", "90", "360"]),
        ("العدد الأولي من بين هذه الأعداد هو:", ["7", "4", "9"]),
        ("ما قيمة 25% من العدد 100؟", ["25", "50", "10"]),
        ("مساحة المربع = طول الضلع في:", ["نفسه", "2", "4"])
    ],
    "حاسب": [
        ("تعتبر لوحة المفاتيح وحدة:", ["إدخال", "إخراج", "تخزين"]),
        ("أصغر وحدة تخزين بيانات هي:", ["البت (Bit)", "الميجابايت", "الكيلوبايت"]),
        ("برنامج يستخدم للعروض التقديمية:", ["باوربوينت", "إكسل", "وورد"]),
        ("مخترع لغة بايثون هو:", ["جيدو فان روسم", "بيل جيتس", "ستيف جوبز"]),
        ("الإنترنت هو شبكة:", ["عالمية", "محلية", "خاصة"])
    ],
    "انقلش": [
        ("Choose the correct: '___ are playing'", ["They", "He", "I"]),
        ("Past tense of 'Go' is:", ["Went", "Gone", "Goes"]),
        ("Which one is a 'Fruit'?", ["Apple", "Carrot", "Bread"]),
        ("Capital of Saudi Arabia is:", ["Riyadh", "Jeddah", "Dammam"]),
        ("The color of the sky is:", ["Blue", "Red", "Green"])
    ],
    "علوم": [
        ("أقرب كوكب للشمس هو:", ["عطارد", "الزهرة", "المريخ"]),
        ("تسمى الطبقة الخارجية للأرض:", ["القشرة", "اللب", "الوشاح"]),
        ("عملية تحول السائل إلى غاز تسمى:", ["تبخر", "تجمد", "تكثف"]),
        ("الغاز الذي نتنفسه هو:", ["الأكسجين", "نيتروجين", "ثاني أكسيد الكربون"]),
        ("المادة التي لها شكل ثابت وحجم ثابت هي:", ["الصلبة", "السائلة", "الغازية"])
    ]
}

# --- 3. عرض الاختبار مادة مادة ---
subjects = list(questions.keys())
for i, sub in enumerate(subjects):
    if st.session_state.page == f"quiz_{sub}":
        st.markdown(f"<h2 style='text-align:center; color:#10a37f;'>📝 اختبار مادة: {sub}</h2>", unsafe_allow_html=True)
        st.write("---")
        with st.form(f"form_{sub}"):
            score = 0
            for j, (q, opts) in enumerate(questions[sub]):
                ans = st.radio(f"{j+1}. {q}", opts, key=f"{sub}_{j}")
                if ans == opts[0]: score += 1 # الخيار الأول هو الصحيح
            
            if st.form_submit_button("المادة التالية ➡️"):
                st.session_state.scores[sub] = score
                st.session_state.page = f"quiz_{subjects[i+1]}" if i+1 < len(subjects) else "final_report"
                st.rerun()

# --- 4. صفحة التقرير النهائي ---
if st.session_state.page == "final_report":
    st.balloons()
    st.markdown("<h1 style='text-align:center;'>📊 تقرير LAI الذكي</h1>", unsafe_allow_html=True)
    
    strongest = max(st.session_state.scores, key=st.session_state.scores.get)
    weakest = min(st.session_state.scores, key=st.session_state.scores.get)

    # نقاط القوة
    st.markdown(f"<div class='report-card'><h3>🌟 مادة التميز: {strongest}</h3>", unsafe_allow_html=True)
    st.write(f"مذهل! لقد حققتِ أعلى الدرجات في {strongest}. يرى الذكاء الاصطناعي أنكِ تمتلكين مستقبلاً باهراً في هذا المجال.")
    st.info("💡 نصيحة لتنمية مهاراتك: حاولي قراءة كتب إثرائية خارج المنهج في هذه المادة.")
    st.markdown("</div>", unsafe_allow_html=True)

    # نقاط الضعف
    st.markdown(f"<div class='report-card' style='border-color: #ff4b4b;'><h3>📈 مادة للتطوير: {weakest}</h3>", unsafe_allow_html=True)
    st.write(f"بناءً على النتائج، مادة {weakest} تحتاج لتركيز إضافي. تذكري أن الخطأ هو أول خطوة للنجاح!")
    st.warning("🛠️ خطة التحسين: ابدأي بمراجعة الدروس الأساسية لمدة 20 دقيقة يومياً واستخدمي الخرائط الذهنية.")
    st.markdown("</div>", unsafe_allow_html=True)

    # الجدول الدراسي
    st.markdown("### 📅 جدول المذاكرة المقترح")
    st.table({
        "الفترة": ["الصباح (تركيز)", "المساء (مراجعة)", "الليل (إبداع)"],
        "الخطة": [f"مراجعة {weakest}", f"حل تمارين {weakest}", f"مشروع في {strongest}"]
    })

    if st.button("إعادة البدء 🔄"):
        st.session_state.page = "welcome"
        st.session_state.scores = {k: 0 for k in st.session_state.scores}
        st.rerun()

st.markdown("<br><center>صُنع بكل فخر بواسطة <b>الجوري</b> 👑</center>", unsafe_allow_html=True)
