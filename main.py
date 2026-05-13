import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Dashboard", layout="centered")

# ضع الـ ID الخاص بملفك هنا
SHEET_ID = '1LDYmzCAbxuUYOZtzLMo5nW-n6Xx455WyYwx1d241c-4'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

def main():
    st.markdown("<h2 style='text-align: center; color: #4A90E2;'>📊 ملخص حالة الإنجاز</h2>", unsafe_allow_html=True)
    st.write("---")

    try:
        # قراءة البيانات
        df = pd.read_csv(URL)
        
        # 1. إجمالي عدد الشقق
        total_apartments = 70
        
        # 2. حساب عدد "Yes" في العمود L (العمود رقم 11 في البرمجة)
        # ملاحظة: iloc[:, 11] تعني العمود L
        done_count = (df.iloc[:, 11].astype(str).str.strip().str.lower() == 'yes').sum()
        
        # 3. حساب المتبقي
        remaining = total_apartments - done_count

        # عرض الأيقونات (العدادات)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: #1e2130; padding: 20px; border-radius: 15px; border-top: 5px solid #4A90E2; text-align: center;'>
                <p style='color: #888; font-size: 18px; margin: 0;'>إجمالي الشقق</p>
                <h1 style='color: white; margin: 10px 0;'>{total_apartments}</h1>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div style='background-color: #1e2130; padding: 20px; border-radius: 15px; border-top: 5px solid #2ECC71; text-align: center;'>
                <p style='color: #888; font-size: 18px; margin: 0;'>المكتمل (L)</p>
                <h1 style='color: #2ECC71; margin: 10px 0;'>{done_count}</h1>
                <p style='color: #E74C3C; font-size: 14px; margin: 0;'>المتبقي: {remaining}</p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error("تأكد من صلاحيات مشاركة ملف قوقل شيت")

if __name__ == "__main__":
    main()
