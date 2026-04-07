import os
import logging
from flask import Flask
from threading import Thread

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR) # إخفاء رسائل السيرفر المزعجة

@app.route('/')
def home():
    return "Bot is running perfectly!"

def run():
    # Render يعطينا البورت تلقائياً، وإذا لم يجد نستخدم 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    """تشغيل خادم الويب في مسار منفصل (Thread) لكي لا يوقف البوت"""
    t = Thread(target=run)
    t.start()
