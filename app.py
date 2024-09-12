import pandas as pd
import random
import gradio as gr

# تحميل بيانات الاقتباسات
quotes = pd.read_csv('quotes.csv')

# دالة لتوليد اقتباس
def display_quote():
    return random.choice(quotes['text'].tolist())

# إنشاء واجهة Gradio مع تحديد المدخلات والمخرجات
interface = gr.Interface(
    fn=display_quote, 
    inputs=None,  # لا توجد مدخلات
    outputs='text', 
    title='Quote Generator', 
    description='Click the button to generate a random quote!'
)

# تشغيل الواجهة
interface.launch()