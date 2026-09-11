import google.generativeai as genai
import streamlit as st

st.set_page_config(
    page_title="مولد محتوى السوشيال ميديا", page_icon="📱", layout="centered"
)

st.title("📱 مولد محتوى السوشيال ميديا الذكي")
st.write(
    "أنشئ منشورات احترافية وجذابة لمنصات التواصل الاجتماعي خلال ثوانٍ معدودة."
)

api_key = st.text_input(
    "أدخل مفتاح Gemini API الخاص بك:", type="password", help="انسخ المفتاح وضعه هنا"
)

if api_key:
  genai.configure(api_key=api_key)

  platform = st.selectbox(
      "اختر المنصة المستهدفة:",
      ["فيسبوك (Facebook)", "إنستغرام (Instagram)", "إكس / تويتر (X)"],
  )

  tone = st.selectbox(
      "اختر نبرة الصوت للمحتوى:",
      ["إعلاني / تسويقي", "تعليمي / معلوماتي", "تحفيزي / تفاعلي", "فكاهي / خفيف"],
  )

  topic = st.text_area(
      "ما هي فكرة أو موضوع المنشور باختصار؟",
      placeholder="مثال: الإعلان عن دورة تدريبية جديدة في البرمجة للمبتدئين...",
  )

  if st.button("توليد المحتوى 🚀", type="primary"):
    if topic.strip():
      with st.spinner("جاري صياغة المحتوى بالذكاء الاصطناعي..."):
        try:
          model = genai.GenerativeModel("gemini-1.5-flash")
          prompt = (
              f"أنت خبير تسويق إلكتروني وصانع محتوى محترف. اكتب منشوراً لمنصة {platform} "
              f"حول الموضوع التالي: '{topic}'. "
              f"يجب أن تكون نبرة الصوت: {tone}. "
              f"اجعل النص جذاباً، منظماً، ويحتوي على إيموجي مناسبة، وأضف وسوم (Hashtags) ممتازة في النهاية باللغة العربية."
          )
          response = model.generate_content(prompt)
          st.success("تم توليد المحتوى بنجاح! 🎉")
          st.markdown("### 📝 النتيجة النهائية:")
          st.markdown(response.text)
        except Exception as e:
          st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
    else:
      st.warning("الرجاء كتابة فكرة المنشور أولاً.")
else:
  st.info("الرجاء إدخال مفتاح Gemini API في الحقل بالأعلى لتفعيل التطبيق.")
  
