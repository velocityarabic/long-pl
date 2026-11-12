"""VELOCITY LONGFORM - 16:9 chapter lesson, brand and motion constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30

TARGET_CHAPTERS = 8
PHRASES_PER_CHAPTER = 7
TARGET_PHRASES = TARGET_CHAPTERS * PHRASES_PER_CHAPTER

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY POLISH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "POLISH"
HANDLE = "@velocitypolish"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {'code': 'pl',
 'name': 'Polish',
 'native_name': 'Polski',
 'history_key': 'polish',
 'english_voice': 'en-US-AvaNeural',
 'english_fallback_voice': 'en-US-GuyNeural',
 'native_voice': 'pl-PL-MarekNeural',
 'native_fallback_voice': 'pl-PL-ZofiaNeural',
 'native_engine': 'edge',
 'native_lang_code': 'pl',
 'english_rate': '-4%',
 'native_rate': '-10%',
 'english_pitch': '+0Hz',
 'native_pitch': '+0Hz',
 'native_label': 'POLSKI',
 'translit_label': 'SAY IT LIKE',
 'flag': 'pl',
 'greeting': 'Cześć!',
 'encouragement': 'Świetnie!',
 'rtl': False,
 'char_tiles': False,
 'script_font': '',
 'glyphs': 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż'}
# ==== LANGUAGE PACK END ====

# ==== CATEGORIES START ====
CATEGORIES = {'Motivation': 'Motywacja',
 'Love': 'Miłość',
 'Success': 'Sukces',
 'Wisdom': 'Mądrość',
 'Happiness': 'Szczęście',
 'Self Improvement': 'Samorozwój',
 'Gratitude': 'Wdzięczność',
 'Friendship': 'Przyjaźń',
 'Hope': 'Nadzieja',
 'Creativity': 'Kreatywność',
 'Inner Peace': 'Wewnętrzny Spokój',
 'Confidence': 'Pewność Siebie',
 'Perseverance': 'Wytrwałość',
 'Inspiration': 'Inspiracja',
 'Positive Life': 'Pozytywne Życie',
 'Courage': 'Odwaga',
 'Kindness': 'Życzliwość',
 'Patience': 'Cierpliwość',
 'Forgiveness': 'Przebaczenie',
 'Strength': 'Siła',
 'Joy': 'Radość',
 'Balance': 'Równowaga',
 'Growth': 'Rozwój',
 'Purpose': 'Cel',
 'Mindfulness': 'Uważność',
 'Travel & Airport': 'Podróże i lotnisko',
 'Ordering Food & Dining': 'Zamawianie jedzenia i jedzenie w restauracji',
 'Shopping & Prices': 'Zakupy i ceny',
 'Asking for Directions': 'Pytanie o drogę',
 'Hotel & Accommodation': 'Hotel i zakwaterowanie',
 'Daily Routine': 'Codzienna rutyna',
 'Meeting People & Greetings': 'Poznawanie ludzi i powitania',
 'Emergency & Health': 'Sytuacje awaryjne i zdrowie',
 'Public Transportation': 'Transport publiczny',
 'Work & Office': 'Praca i biuro',
 'Weather & Small Talk': 'Pogoda i small talk',
 'Coffee Shop & Bakery': 'Kawiarnia i piekarnia',
 'Family & Home': 'Rodzina i dom',
 'Hobbies & Free Time': 'Hobby i czas wolny',
 'Dating & Romance': 'Randki i romans',
 'Phone Calls & Messages': 'Rozmowy telefoniczne i wiadomości',
 'Banking & Money': 'Bankowość i pieniądze',
 'Doctor & Pharmacy': 'Lekarz i apteka',
 'Sports & Fitness': 'Sport i fitness',
 'Celebrations & Parties': 'Uroczystości i przyjęcia',
 'Feelings & Emotions': 'Uczucia i emocje',
 'Agreeing & Disagreeing': 'Zgadzanie się i niezgadzanie się',
 'Making Plans': 'Planowanie',
 'Common Native Slang': 'Popularny slang rodzimy',
 'Cultural Traditions': 'Tradycje kulturowe'}
# ==== CATEGORIES END ====

CATEGORY_NAMES = list(CATEGORIES.keys())

AI_MODEL = os.getenv("AI_MODEL", "openai/gpt-5.4-nano")
AI_FALLBACK_MODEL = os.getenv("AI_FALLBACK_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 7.2
CHAPTER_INTRO_DURATION = 4.4
OUTRO_DURATION = 13.0

EN_CARD_IN = 0.70
GAP_EN_NATIVE = 0.60
NATIVE_CARD_LEAD = 0.40
GAP_BEFORE_REPEAT = 1.00
TAIL_HOLD = 1.30

# ---------------------------------------------------------------- palette

INK = "#30303A"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#7C5CFF"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

# ==== HASHTAGS START ====
HASHTAGS = ['#learnpolish',
 '#polishlessons',
 '#polishforbeginners',
 '#languagelearning',
 '#polishvocabulary',
 '#velocitypolish',
 '#dailypolish',
 '#polish',
 '#learnlanguages',
 '#speakpolish']
# ==== HASHTAGS END ====
