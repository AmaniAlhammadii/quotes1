import pandas as pd
import random
import gradio as gr

# تحميل بيانات الاقتباسات
quotes = pd.read_csv('quotes.csv')

# دالة لتوليد اقتباس
def display_quote():
    return random.choice(quotes['text'].tolist())

# إنشاء واجهة Gradio
interface = gr.Interface(
    fn=display_quote, 
    outputs='text', 
    title='Quote Generator', 
    description='Click the button to generate a random quote!'
)

# تشغيل الواجهة
interface.launch()