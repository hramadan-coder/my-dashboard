import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Real Estate Dashboard", layout="wide")

# اترك هذا الرابط كما هو حالياً، سنقوم بتحديث الـ ID لاحقاً
SHEET_ID = '1LDYmzCAbxuUYOZtzLMo5nW-n6Xx455WyYwx1d241c-4'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

def main():
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📊 لوحة تحكم العقارات</h1>", unsafe_allow_html=True)
    st.write("---")

    try:
        df = pd.read_csv(URL)
        # الكود يسحب البيانات من العمود الثاني (B) إلى العمود رقم 12 (L)
        data_cols = df.iloc[:, 1:12] 
        
        cols = st.columns(3)
        for i, col_name in enumerate(data_cols.columns):
            # حساب عدد الـ Yes في كل عمود
            count = (data_cols[col_name].astype(str).str.strip().str.lower() == 'yes').sum()
            
            with cols[i % 3]:
                st.markdown(f"""
                <div style='background-color: #1e2130; padding: 20px; border-radius: 10px; border-left: 5px solid #4A90E2; margin-bottom: 10px;'>
                    <p style='color: #888; font-size: 14px; margin: 0;'>{col_name}</p>
                    <h2 style='color: white; margin: 0;'>{count} <span style='font-size: 15px;'>مكتمل ✅</span></h2>
                </div>
                """, unsafe_allow_html=True)
                
    except Exception as e:
        st.error("خطأ: تأكد من رابط ملف قوقل شيت وصلاحيات المشاركة")

if __name__ == "__main__":
    main()
