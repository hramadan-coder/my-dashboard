import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Dashboard", layout="centered")

# ضع الـ ID الخاص بملفك هنا
SHEET_ID = '1LDYmzCAbxuUYOZtzLMo5nW-n6Xx455WyYwx1d241c-4'
URL = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

def main():
    # 1. عنوان الصفحة الرئيسي (الذي يظهر في الأعلى)
    st.markdown("<h2 style='text-align: center; color: #4A90E2;'>📊 متابعة إنجاز الوحدات السكنية</h2>", unsafe_allow_html=True)
    st.write(AREA Dashboard)

    try:
        # قراءة البيانات
        df = pd.read_csv(URL)
        
        total_apartments = 70
        # حساب عدد "Yes" في العمود L
        done_count = (df.iloc[:, 11].astype(str).str.strip().str.lower() == 'yes').sum()
        # حساب المتبقي
        remaining = total_apartments - done_count

        # عرض المربع في المنتصف مع المسميات الجديدة
        st.markdown(f"""
        <div style='background-color: #1e2130; padding: 40px; border-radius: 20 : 8px solid #2ECC71; text-align: center; max-width: 500px; margin: auto;'>
            
            <p style='color: #888; font-size: 20px; margin: 0;'>إجمالي الوحدات المكتملة</p>
            
            <h1 style='color: #2ECC71; font-size: 60px; margin: 15px 0;'>{done_count}</h1>
            
            <div style='background-color: #2c313c; padding: 10px; border-radius: 10px; display: inline-block; width: 100%;'>
                
                <span style='color: #888; font-size: 16px;'>بانتظار الإنجاز: </span>
                <span style='color: #E74C3C; font-size: 20px; font-weight: bold;'>{remaining}</span>
                
                <span style='color: #888; font-size: 14px; margin-left: 10px;'> (من أصل {total_apartments} وحدة)</span>
                
            </div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error("تأكد من صلاحيات مشاركة ملف قوقل شيت")

if __name__ == "__main__":
    main()
