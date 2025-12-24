import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="LAI Learning Game", page_icon="🎮")

# تعريف "حالة اللعبة" للتنقل بين الصفحات
if 'stage' not in st.session_state:
    st.session_state.stage = "welcome"
if 'scores' not in st.session_state:
    st.session_state.scores = {}

# --- دالة مساعدة لعرض النتائج ---
def move_to(next_stage):
    st.session_state.stage = next_stage
    st.rerun()

# --- 1. صفحة البداية ---
if st.session_state.stage == "welcome":
    st.title("🤖 نظام LAI للتحليل الذكي")
    st.image("https://img.freepik.com/free-vector/educational-video-game-concept_23-2148523390.jpg", width=400)
    st.write("### هل أنتِ مستعدة لبدء رحلة التحدي؟")
    st.info("سنجري اختباراً سريعاً في 5 مجالات لنكتشف مواهبكِ!")
    if st.button("🚀 ابدأ اللعبة الآن"):
        move_to("science")

# --- 2. مادة العلوم ---
elif st.session_state.stage == "science":
    st.header("🔬 المرحلة 1: العلوم")
    q1 = st.radio("ما هو الغاز الذي تتنفسه الكائنات الحية لتعيش؟", ["الأكسجين", "نيتروجين", "ثاني أكسيد الكربون"])
    if st.button("تأكيد الإجابة والانتقال للرياضيات ➡️"):
        st.session_state.scores['العلوم'] = 1 if q1 == "الأكسجين" else 0
        move_to("math")

# --- 3. مادة الرياضيات ---
elif st.session_state.stage == "math":
    st.header("🔢 المرحلة 2: الرياضيات")
    q2 = st.number_input("إذا كان معك 5 تفاحات وأكلت 2، ثم اشتريت 4، كم أصبح معك؟", value=0)
    if st.button("تأكيد الإجابة والانتقال للإسلامية ➡️"):
        st.session_state.scores['الرياضيات'] = 1 if q2 == 7 else 0
        move_to("islamic")

# --- 4. مادة التربية الإسلامية ---
elif st.session_state.stage == "islamic":
    st.header("🕌 المرحلة 3: التربية الإسلامية")
    q3 = st.radio("ما هو الركن الثاني من أركان الإسلام؟", ["الشهادتان", "الصلاة", "الحج"])
    if st.button("تأكيد الإجابة والانتقال للإنجليزي ➡️"):
        st.session_state.scores['الإسلامية'] = 1 if q3 == "الصلاة" else 0
        move_to("english")

# --- 5. مادة اللغة الإنجليزية ---
elif st.session_state.stage == "english":
    st.header("🔤 المرحلة 4: English")
    q4 = st.selectbox("Choose the correct fruit name:", ["Apple 🍎", "Book 📖", "Car 🚗"])
    if st.button("تأكيد الإجابة والانتقال للمهارات الرقمية ➡️"):
        st.session_state.scores['اللغة الإنجليزية'] = 1 if q4 == "Apple 🍎" else 0
        move_to("digital")

# --- 6. المهارات الرقمية (الحاسب) ---
elif st.session_state.stage == "digital":
    st.header("💻 المرحلة 5: المهارات الرقمية")
    q5 = st.radio("ما هو الجزء المسؤول عن 'عقل' الكمبيوتر؟", ["الشاشة", "المعالج (CPU)", "الفأرة"])
    if st.button("🏁 إنهاء اللعبة ورؤية التحليل"):
        st.session_state.scores['المهارات الرقمية'] = 1 if q5 == "المعالج (CPU)" else 0
        move_to("final_report")

# --- 7. التقرير النهائي والتحليل الشامل ---
elif st.session_state.stage == "final_report":
    st.title("📊 تقرير تحليل المستوى النهائي")
    
    total_score = sum(st.session_state.scores.values())
    st.balloons()
    
    # عرض الدرجات في جدول أنيق
    st.table([st.session_state.scores])
    
    # تحديد نقاط الضعف
    weak_subjects = [sub for sub, score in st.session_state.scores.items() if score == 0]
    
    if not weak_subjects:
        st.success("ما شاء الله! أنتِ مبدعة في كل المجالات. ننصحكِ بمشاريع ابتكارية متقدمة.")
    else:
        st.warning(f"تحليل LAI: أنتِ ممتازة، ولكن تحتاجين لتركيز أكثر في: {', '.join(weak_subjects)}")
        
        st.write("### 📚 مصادر مقترحة لكِ:")
        for sub in weak_subjects:
            if sub == "العلوم":
                st.write("- [قناة عين للعلوم](https://www.youtube.com/user/ienchannel)")
            elif sub == "الرياضيات":
                st.write("- [تدريبات جدول الضرب](https://www.math-drills.com)")
            # يمكن إضافة روابط لكل مادة هنا

    if st.button("🔄 إعادة المحاولة"):
        st.session_state.stage = "welcome"
        st.session_state.scores = {}
        st.rerun()
