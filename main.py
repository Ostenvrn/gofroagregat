# ==========================================================================
# ГОФРОАГРЕГАТ v13.4.1 - Kivy для Android (Схема с анимациями, центрирована)
# Автор: Чернов Александр
# ==========================================================================

from kivy.config import Config
Config.set('graphics', 'orientation', 'portrait')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Line, Ellipse, Rectangle
import random
import threading
import time
from queue import Queue, Empty
from kivy.logger import Logger

# Настройка окна
Window.clearcolor = (0.1, 0.1, 0.1, 1)
Window.fullscreen = 'auto'

# Цвета
COLORS = {
    'work': (0.53, 0.8, 1, 1),
    'problem': (1, 0.4, 0.4, 1),
    'success': (0.4, 1, 0.4, 1),
    'info': (1, 1, 1, 1),
    'karshik': (1, 0.6, 1, 1),
    'brigadier': (1, 0.87, 0, 1),
    'klevar': (1, 0.8, 0, 1),
    'headset': (1, 0.6, 0.8, 1),
    'trainee': (1, 0.53, 0, 1),
    'planner': (1, 0.27, 0.27, 1),
    'otk': (1, 0, 1, 1),
    'birthday': (1, 0.8, 1, 1),
    'ppr': (1, 0.4, 0, 1),
    'raw_quality': (0, 1, 1, 1),
    'quiz': (1, 0.8, 0, 1),
    'chufyr': (1, 0, 0, 1),
    'wet_part': (1, 0.53, 0, 1),
    'dry_part': (1, 0.27, 0.27, 1),
    'defect': (1, 0.27, 0, 1),
    'smoke': (0.8, 0.8, 0.8, 1),
    'order': (0.5, 1, 0.5, 1),
    'cancel': (1, 0.5, 0.5, 1),
    'pallet': (0.8, 0.6, 1, 1),
}

# Константы
LOG_DELAY = 0.8
BRIGADE_CHANGE_INTERVAL = 50
MAX_LOG_ENTRIES = 200
LOG_QUEUE_PROCESS_INTERVAL = 0.1

# Данные
KARSHIK_NAMES = ["Андрей", "Виталик", "Яша"]
KLEEVAR_NAMES = ["Саша", "Паша", "Лёша"]

BRIGADES = [
    {"name": "Бригада 1"}, 
    {"name": "Бригада 2"}, 
    {"name": "Бригада 3"}, 
    {"name": "Бригада 4"}
]

ORDER_TYPES = ["ВГ", "ПЭТ", "Плёнка", "Бумага"]

HEADSET_CHATTER = [
    "«Слышь, а помнишь вчера...»", "«Опять с заказами чудит...»",
    "«Стажёр опять что-то натворил...»", "«Кто клей спустил в канализацию?»",
    "«Слышь, а давай после смены пивка?»", "«А помнишь, как стажёр в клей упал?»",
    "«Кто вчера забыл выключить агрегат?»", "«Опять кассету менять...»",
    "«Кто-нибудь видел мой гаечный ключ?»", "«Скоро там обед? Я есть хочу...»",
    "«О, смотри, карщик едет!»", "«Опять битый ролик привезли!»",
    "«Кто рулон не закрепил?»", "«Слышь, а когда зарплата?»",
    "«Опять этот со своими заказами...»", "«Смотри, какой брак пошёл!»",
    "«Кто-нибудь знает, где наладчик?»", "«Опять листоукладчик забился...»",
    "«Слышь, а давай после смены шашлыки?»", "«Я вчера так устал, еле встал...»",
    "«Кто клей недоварил?»", "«Опять расклей пошёл!»",
    "«Слышь, а кто сегодня на хвосте?»", "«Я вчера на даче был...»",
    "«Опять обрыв на лицевом!»", "«Кто модуль не проверил?»",
    "«Слышь, а у тебя есть закурить?»", "«Я вчера в гараж ездил...»",
    "«Опять эти ракушки забились...»", "«Кто релёвки перепутал?»",
    "«Я вчера фильм смотрел, уснул...»", "«Опять корабление!»",
    "«Слышь, а давай в шахматы?»", "«Я вчера в баню ходил...»",
    "«Опять просечки!»", "«Кто натяжение не проверил?»",
    "«Опять замятие!»", "«Слышь, а давай после смены на рыбалку?»",
    "«Опять брак пошёл!»", "«Я вчера в лотерею выиграл!»",
    "«Кто релёвки не выставил?»", "«Опять перегрев!»",
    "«Я вчера на концерт ходил...»", "«Опять клей протёк!»",
    "«Слышь, а давай в карты?»", "«У меня сын в школу пошёл...»",
    "«Опять этот дождь...»", "«Слышь, а у тебя тёща как?»",
    "«Кто-нибудь знает, когда отпуск?»", "«Опять выходной перенесли...»",
    "«Слышь, а давай после смены в кафе?»", "«Я вчера на футбол ходил...»",
    "«Кто сегодня на мойке?»", "«Опять смену продлили...»",
    "«Я вчера в деревню ездил...»", "«Кто-нибудь видел мой телефон?»",
    "«Опять Wi-Fi не ловит...»", "«Слышь, а давай в кино?»",
    "«Я вчера пиво пил, голова болит...»", "«Кто-нибудь знает, где столовая?»",
    "«Опять обед задержали...»", "«Слышь, а давай в домино?»",
    "«Я вчера на охоту ездил...»", "«Опять вентиляция не работает...»",
    "«Я вчера в театр ходил...»", "«Кто-нибудь видел мою кружку?»",
    "«Опять чай остыл...»", "«Я вчера на выставку ходил...»",
    "«Опять свет мигает...»", "«Я вчера в цирк ходил...»",
    "«Кто-нибудь знает, где курить можно?»", "«Опять курилку закрыли...»",
    "«Слышь, а давай в бильярд?»", "«Я вчера в музей ходил...»",
    "«Опять пол скользкий...»", "«Я вчера в парк ходил...»",
    "«Кто-нибудь видел мои перчатки?»", "«Опять руки мёрзнут...»",
    "«Слышь, а давай в сауну?»", "«Я вчера в спортзал ходил...»",
    "«А помнишь, как стажёр в клей упал?»", "«Смотри, опять крыса бегает!»",
    "«Я вчера так храпел...»", "«Опять эта в короткой юбке...»",
    "«Слышь, а кто вчера песни орал?»", "«Я вчера пельменей наелся...»",
    "«Смотри, карщик ролик уронил!»", "«Слышь, а давай в караоке?»",
    "«Я вчера кота мыл...»", "«Опять эта муха летает!»",
    "«Слышь, а давай в боулинг?»", "«Я вчера суп пересолил...»",
    "«Опять этот сквозняк!»", "«Я вчера в очереди стоял...»",
    "«Смотри, клеевар клей разлил!»", "«Слышь, а давай на каток?»",
    "«Я вчера в пробке стоял...»", "«Опять эта сирена!»",
    "«Я вчера в парикмахерскую ходил...»", "«Смотри, релёвщик релёвки перепутал!»",
    "«Слышь, а давай в тир?»", "«Я вчера в аптеку ходил...»",
    "«Опять этот запах клея!»", "«Смотри, хвостовик брак пропустил!»",
    "«Опять этот шум!»", "«Смотри, модульщик просечки поймал!»",
    "«Слышь, а давай в бассейн?»", "«Я вчера в автосервис ездил...»",
    "«Опять эта пыль!»", "«Смотри, лицевик обрыв поймал!»",
    "«Слышь, а давай в ресторан?»", "«Я вчера в обувной ходил...»",
]

CHUFYR_PHRASE = "«Чуфрь-Чуфырь-Чуфырь!»"

QUIZ_QUESTIONS = {
    "Модуль": [
        {"question": "За что отвечает модульщик?", "answers": ["За гофру и внутренний слой", "За упаковку", "За доставку", "За бухгалтерию"], "correct": 0},
        {"question": "Что такое гофрокассета?", "answers": ["Инструмент для гофрирования", "Коробка", "Деталь конвейера", "Тип клея"], "correct": 0},
        {"question": "Что делать при засоре клеевого узла?", "answers": ["Прочистить узел", "Добавить клей", "Увеличить скорость", "Игнорировать"], "correct": 0},
        {"question": "Сколько слоёв в пятислойке?", "answers": ["5", "3", "2", "7"], "correct": 0},
        {"question": "Какой профиль только в первом модуле?", "answers": ["Е", "В", "С", "ВС"], "correct": 0}
    ],
    "Склейка": [
        {"question": "За что отвечает склейщик?", "answers": ["За лицевой слой", "За варку клея", "За гофру", "За упаковку"], "correct": 0},
        {"question": "Что делает склейщик при обрыве лицевого слоя?", "answers": ["Перезаправляет рулон", "Варит новый клей", "Зовёт модульщика", "Ничего"], "correct": 0},
        {"question": "Какой слой обслуживает склейщик?", "answers": ["Лицевой", "Гофрированный", "Внутренний", "Все слои"], "correct": 0},
        {"question": "Что проверяет склейщик?", "answers": ["Натяжение лицевого слоя", "Температуру клея", "Скорость конвейера", "Влажность"], "correct": 0},
        {"question": "Кто варит клей?", "answers": ["Клеевар", "Склейщик", "Модульщик", "Бригадир"], "correct": 0}
    ],
    "Релёвки": [
        {"question": "За что отвечает релёвщик?", "answers": ["За релёвки и размеры", "За клей", "За упаковку", "За доставку"], "correct": 0},
        {"question": "Что такое разбежка по слоям?", "answers": ["Смещение слоёв", "Тип клея", "Скорость", "Температура"], "correct": 0},
        {"question": "Что делать при забитой обрези?", "answers": ["Очистить ракушки", "Добавить клей", "Ускорить", "Выключить свет"], "correct": 0},
        {"question": "Какой инструмент у релёвщика?", "answers": ["Нож для релёвок", "Молоток", "Отвёртка", "Кисть"], "correct": 0},
        {"question": "Что такое релёвки?", "answers": ["Линии сгиба", "Тип клея", "Упаковка", "Инструмент"], "correct": 0}
    ],
    "Хвост": [
        {"question": "За что отвечает хвостовик?", "answers": ["За готовый картон", "За сырьё", "За клей", "За зарплату"], "correct": 0},
        {"question": "Что делать при замятии?", "answers": ["Остановить и устранить", "Ускорить", "Игнорировать", "Выключить свет"], "correct": 0},
        {"question": "Что такое корабление?", "answers": ["Искривление листа", "Тип упаковки", "Способ доставки", "Режим"], "correct": 0},
        {"question": "Куда складывают готовый картон?", "answers": ["На поддон", "В ящик", "На пол", "В печь"], "correct": 0},
        {"question": "Что проверяет хвостовик?", "answers": ["Качество на выходе", "Клей", "Сырьё", "Зарплату"], "correct": 0}
    ]
}

WET_PART_PROBLEMS = {
    "лицевой": ["обрыв лицевого слоя", "неправильная натяжка лицевого слоя"],
    "модуль": ["обрыв гофрированного слоя", "обрыв внутреннего слоя", "не нажата кнопка перехода рулона", "засор клеевого узла, залил кассету"]
}

DRY_PART_PROBLEMS = {
    "релёвщик": ["разбежка по слоям", "проблема с релёвками", "неправильный размер картона", "забилась обрезь в ракушки"],
    "хвостовик": ["брак готового картона", "замятие на листоукладчике", "корабление готового картона"]
}


class Order:
    def __init__(self, order_id, order_type, quantity):
        self.id = order_id
        self.type = order_type
        self.quantity = quantity
        self.status = "Новый"
        self.progress = 0
        self._lock = threading.Lock()
    
    def update_progress(self, amount):
        with self._lock:
            self.progress = min(100, self.progress + amount)
            if self.progress >= 100:
                self.status = "Готов"
                return True
            return False


class Palleto:
    def __init__(self, order_id, order_type):
        self.order_id = order_id
        self.type = order_type
        self.boxes = 0
        self.max_boxes = 50
        self.wrapped = False
        self._lock = threading.Lock()
    
    def add_box(self):
        with self._lock:
            if self.boxes < self.max_boxes:
                self.boxes += 1
                return True
            return False
    
    def wrap(self):
        with self._lock:
            self.wrapped = True


class MachineOperator:
    def __init__(self):
        self.defects = 0
        self.total_earned = 0
        self.quiz_correct = 0
        self.quiz_wrong = 0
        self.action_count = 0
        self.workers_smoking = {
            "лицевик": False, 
            "модульщик": False, 
            "релёвщик": False, 
            "хвостовик": False
        }
        self._lock = threading.Lock()
    
    def take_salary(self):
        with self._lock:
            self.total_earned += 100
            return 100
    
    def go_smoke(self, worker):
        with self._lock:
            if worker in self.workers_smoking:
                self.workers_smoking[worker] = True
    
    def return_from_smoke(self, worker):
        with self._lock:
            if worker in self.workers_smoking:
                self.workers_smoking[worker] = False
    
    def is_smoking(self, worker):
        with self._lock:
            return self.workers_smoking.get(worker, False)


class CorrugatorMachine:
    def __init__(self):
        self.wear = 0
        self.glue_level = 100
        self.paper_level = 100
        self.running = False
        self._lock = threading.Lock()
    
    def start(self):
        with self._lock:
            if self.wear < 100 and self.paper_level > 0 and self.glue_level > 0:
                self.running = True
                return True
            return False
    
    def produce(self):
        with self._lock:
            if not self.running:
                return
            self.wear += random.randint(0, 1)
            self.paper_level -= random.randint(1, 2)
            self.glue_level -= random.randint(1, 2)
            if self.paper_level <= 0 or self.glue_level <= 0:
                self.running = False


class Karshik:
    def __init__(self, name):
        self.name = name
        self._lock = threading.Lock()
    
    def deliver_roll(self):
        with self._lock:
            if random.random() < 0.15:
                return "битый"
            return "хороший"


class Klevar:
    def __init__(self, name):
        self.name = name
        self._lock = threading.Lock()
    
    def make_glue(self):
        with self._lock:
            return random.randint(20, 40)


class BorderedBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._update_rect, size=self._update_rect)
        self.border_color = (1, 0.8, 0, 1)
        self.bg_color = (0.05, 0.05, 0.05, 1)
    
    def _update_rect(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(8)])
            Color(*self.border_color)
            Line(
                rounded_rectangle=(
                    self.pos[0], self.pos[1], 
                    self.size[0], self.size[1], 
                    dp(8)
                ), 
                width=2
            )


class AggregateScheme(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animation_offset = 0
        self.running = False
        self.labels = []
        self.blink_state = 0
        Clock.schedule_interval(self._animate, 0.05)
        Clock.schedule_interval(self._blink, 0.3)
        Clock.schedule_once(lambda dt: self.draw_scheme(), 0.1)
    
    def on_size(self, *args):
        self.draw_scheme()
    
    def _animate(self, dt):
        if self.running:
            self.animation_offset += 2
            if self.animation_offset > 20:
                self.animation_offset = 0
            self.draw_scheme()
    
    def _blink(self, dt):
        self.blink_state = 1 - self.blink_state
        self.draw_scheme()
    
    def draw_scheme(self):
        self.canvas.clear()
        self._clear_labels()
        
        w = self.width
        h = self.height
        
        if w <= 0 or h <= 0:
            return
        
        with self.canvas:
            # Фон
            Color(0.1, 0.1, 0.12, 1)
            Rectangle(pos=(0, 0), size=(w, h))
            
            # Рамка схемы с отступами
            margin = 15
            scheme_w = w - 2 * margin
            scheme_h = h - 2 * margin
            
            # Фон схемы
            Color(0.15, 0.15, 0.18, 1)
            Rectangle(pos=(margin, margin), size=(scheme_w, scheme_h))
            
            # Рамка
            Color(0.4, 0.35, 0.2, 1)
            Line(rectangle=(margin, margin, scheme_w, scheme_h), width=2)
            
            # Анимационные линии
            self._draw_animated_lines(margin, scheme_w, scheme_h)
            
            # Детализированная схема с центрированием
            self._draw_detailed_centered(margin, scheme_w, scheme_h)
    
    def _clear_labels(self):
        for label in self.labels:
            self.remove_widget(label)
        self.labels.clear()
    
    def _draw_animated_lines(self, margin, sw, sh):
        if not self.running:
            return
        
        node_h = sh / 12
        node_w = sw * 0.65
        x_start = margin + (sw - node_w) / 2
        y_offset = (sh - 12 * node_h) / 2
        
        start_y = margin + 6 * node_h + y_offset + node_h * 0.5
        end_y = margin + 12 * node_h + y_offset
        line_x = x_start + node_w * 0.5
        
        Color(0.8, 0.6, 0.4, 0.3)
        for i in range(8):
            y_pos = start_y + (i * (end_y - start_y) / 7 + self.animation_offset * 2) % (end_y - start_y)
            if start_y < y_pos < end_y:
                Color(1, 0.8, 0.2, 0.5 + 0.3 * self.blink_state)
                Ellipse(pos=(line_x - 4, y_pos - 4), size=(8, 8))
    
    def _draw_detailed_centered(self, margin, sw, sh):
        node_h = sh / 12
        node_w = sw * 0.65
        x_start = margin + (sw - node_w) / 2
        y_offset = (sh - 12 * node_h) / 2
        
        labels = [
            "5 раскат\nвнутр.",      # 0
            "Модуль 2\nформир.",     # 1
            "4 раскат\nгофра",       # 2
            "3 раскат\nвнутр.",      # 3
            "Модуль 1\nформир.",     # 4
            "2 раскат\nгофра",       # 5
            "1 раскат\nлицевой",     # 6
            "Сушильный\nстол",       # 7
            "Отруб\nбрака",          # 8
            "Релёвки\nножи",         # 9
            "Поперечная\nрезка",     # 10
            "Укладчик"               # 11
        ]
        
        for i in range(12):
            y = margin + i * node_h + y_offset
            
            label = Label(
                text=labels[i],
                font_size=sp(7),
                color=(0.7, 0.7, 0.7, 1),
                size_hint=(None, None),
                size=(sw * 0.22, node_h),
                pos=(margin + 3, y),
                halign='left',
                valign='middle'
            )
            self.add_widget(label)
            self.labels.append(label)
            
            self._draw_node_animated(i, x_start, y, node_w, node_h - 3)
        
        # Анимация картона после сушки
        if self.running:
            Color(0.8, 0.6, 0.4, 0.8)
            start_y = margin + 7 * node_h + y_offset
            end_y = margin + 12 * node_h + y_offset
            for j in range(6):
                card_y = start_y + (j * node_h + self.animation_offset * 1.5) % (end_y - start_y)
                if start_y < card_y < end_y:
                    Rectangle(pos=(x_start + node_w * 0.35, card_y), 
                             size=(node_w * 0.3, node_h * 0.25))
    
    def _draw_node_animated(self, index, x, y, w, h):
        # === РАСКАТЫ ===
        if index in [0, 2, 3, 5, 6]:
            Color(0.3, 0.3, 0.35, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            if self.running:
                rot_offset = (self.animation_offset * 0.5) % 10
                Color(0.6, 0.6, 0.7, 1)
            else:
                rot_offset = 0
                Color(0.4, 0.4, 0.5, 1)
            
            Ellipse(pos=(x + w * 0.15, y + h * 0.2 + rot_offset * 0.3), 
                    size=(w * 0.12, h * 0.6 - rot_offset * 0.3))
            Ellipse(pos=(x + w * 0.45, y + h * 0.2 + rot_offset * 0.3), 
                    size=(w * 0.12, h * 0.6 - rot_offset * 0.3))
            
            Color(0.7, 0.7, 0.7, 1)
            Line(points=[x + w * 0.15, y + h * 0.5, x + w * 0.27, y + h * 0.5], width=1)
            Line(points=[x + w * 0.45, y + h * 0.5, x + w * 0.57, y + h * 0.5], width=1)
            
            if self.running and self.blink_state:
                Color(0.5, 0.5, 0.5, 1)
                Rectangle(pos=(x + w * 0.7, y + h * 0.35), size=(w * 0.1, h * 0.3))
            else:
                Color(0.3, 0.3, 0.3, 1)
                Rectangle(pos=(x + w * 0.7, y + h * 0.35), size=(w * 0.1, h * 0.3))
            
            if self.running:
                Color(0.6, 0.4, 0.3, 0.4)
                for j in range(3):
                    paper_y = y + h * 0.3 + (j * h * 0.3 + self.animation_offset * 0.8) % (h * 0.4)
                    Rectangle(pos=(x + w * 0.9, paper_y), size=(w * 0.08, h * 0.05))
        
        # === МОДУЛИ ===
        elif index in [1, 4]:
            Color(0.2, 0.35, 0.2, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            if self.running:
                rot = self.animation_offset % 10
                Color(0.7, 0.7, 0.3, 1)
            else:
                rot = 0
                Color(0.5, 0.5, 0.3, 1)
            
            Ellipse(pos=(x + w * 0.15, y + h * 0.25 + rot * 0.2), 
                    size=(w * 0.1, h * 0.5))
            Ellipse(pos=(x + w * 0.35, y + h * 0.25 + rot * 0.2), 
                    size=(w * 0.1, h * 0.5))
            
            Color(0.8, 0.6, 0.3, 1)
            Rectangle(pos=(x + w * 0.55, y + h * 0.3), size=(w * 0.15, h * 0.4))
            
            if self.running and self.blink_state:
                Color(0.7, 0.5, 0.3, 1)
            else:
                Color(0.5, 0.3, 0.2, 1)
            Rectangle(pos=(x + w * 0.75, y + h * 0.4), size=(w * 0.15, h * 0.2))
            
            if self.running:
                Color(0.8, 0.6, 0.2, 0.3)
                glue_y = y + h * 0.45 + (self.animation_offset * 0.5) % (h * 0.2)
                Rectangle(pos=(x + w * 0.82, glue_y), size=(w * 0.05, h * 0.05))
        
        # === СУШИЛЬНЫЙ СТОЛ ===
        elif index == 7:
            Color(0.6, 0.4, 0.2, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            if self.running:
                heat = 0.5 + 0.5 * self.blink_state
                Color(1, 0.5 * heat, 0, heat)
            else:
                Color(0.5, 0.3, 0.2, 1)
            
            for j in range(5):
                Rectangle(pos=(x + w * (0.08 + j * 0.18), y + h * 0.2), 
                         size=(w * 0.1, h * 0.6))
            
            if self.running:
                Color(1, 0.5, 0, 0.15)
                for j in range(3):
                    wave_y = y + h * 0.2 + (j * h * 0.3 + self.animation_offset * 1.2) % (h * 0.6)
                    Line(points=[x + w * 0.1, wave_y, x + w * 0.9, wave_y], width=2)
        
        # === ОТРУБ БРАКА ===
        elif index == 8:
            Color(0.6, 0.2, 0.2, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            if self.running and self.blink_state:
                Color(0.9, 0.2, 0.2, 1)
            else:
                Color(0.9, 0.9, 0.9, 1)
            
            Line(points=[x + w * 0.4, y, x + w * 0.4, y + h], width=2)
            Line(points=[x + w * 0.6, y, x + w * 0.6, y + h], width=2)
        
        # === РЕЛЁВКИ ===
        elif index == 9:
            Color(0.5, 0.3, 0.5, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            Color(0.8, 0.8, 0.8, 1)
            for j in range(3):
                knife_x = x + w * (0.25 + j * 0.25)
                Line(points=[knife_x, y + h * 0.2, knife_x, y + h * 0.8], width=2)
            
            if self.running:
                Color(0.9, 0.9, 0.9, 0.5)
                knife_offset = (self.animation_offset * 0.3) % h * 0.5
                Line(points=[x + w * 0.35, y + h * 0.2 + knife_offset, 
                             x + w * 0.35, y + h * 0.8 + knife_offset], width=1)
        
        # === ПОПЕРЕЧНАЯ РЕЗКА ===
        elif index == 10:
            Color(0.3, 0.5, 0.5, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            if self.running:
                Color(0.9, 0.9, 0.9, 1)
                knife_y = y + h * (0.5 + (self.animation_offset * 0.5) % 10 / 10 - 0.5)
                Line(points=[x, knife_y, x + w, knife_y], width=3)
        
        # === УКЛАДЧИК ===
        elif index == 11:
            Color(0.3, 0.3, 0.6, 1)
            Rectangle(pos=(x, y), size=(w, h))
            
            if self.running:
                Color(0.6, 0.6, 0.8, 1)
            else:
                Color(0.4, 0.4, 0.6, 1)
            
            for j in range(3):
                brush_x = x + w * (0.2 + j * 0.25)
                Line(points=[brush_x, y + h * 0.6, brush_x, y + h * 0.9], width=3)
            
            pallet_height = 0.25 + 0.1 * self.blink_state
            Color(0.7, 0.5, 0.3, 1)
            Rectangle(pos=(x + w * 0.3, y + h * 0.05), 
                     size=(w * 0.4, h * pallet_height))
            
            if self.running:
                box_y = y + h * 0.05 + (self.animation_offset * 0.2) % (h * 0.2)
                Color(0.5, 0.3, 0.2, 0.5)
                for j in range(3):
                    Rectangle(pos=(x + w * (0.32 + j * 0.12), box_y), 
                             size=(w * 0.08, h * 0.08))


class FactoryGameKivy(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.log_queue = Queue()
        self.game_thread = None
        self.quiz_popup_open = False
        self.restart_scheduled = False
        self.last_chatter = None
        self.selected_section = None
        self.used_questions = {}
        self.orders = []
        self.current_order = None
        self.order_counter = 0
        self.pallets = []
        self.current_pallet = None
        self.defect_streak = 0
        self.relevek_jam = False
        self.scheme_open = False
    
    def build(self):
        self.operator = MachineOperator()
        self.machine = CorrugatorMachine()
        self.karshik = Karshik(random.choice(KARSHIK_NAMES))
        self.klevar = Klevar(random.choice(KLEEVAR_NAMES))
        self.current_brigade = random.choice(BRIGADES)
        self.running = False
        
        root = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(5))
        
        root.add_widget(Label(
            text="ГОФРОАГРЕГАТ", 
            font_size=sp(24), 
            bold=True, 
            color=(1, 0.8, 0, 1), 
            halign='center', 
            size_hint_y=None, 
            height=dp(40)
        ))
        
        root.add_widget(Label(
            text="Автор: Чернов Александр | v13.4.1", 
            font_size=sp(12), 
            color=(0.7, 0.7, 0.7, 1), 
            halign='center', 
            size_hint_y=None, 
            height=dp(20)
        ))
        
        self.status_label = Label(
            text="Нажмите СТАРТ", 
            font_size=sp(12), 
            color=(1, 1, 1, 1), 
            halign='center', 
            size_hint_y=None, 
            height=dp(70), 
            text_size=(Window.width - dp(20), None)
        )
        root.add_widget(self.status_label)
        
        log_frame = BorderedBox(
            orientation='vertical', 
            size_hint=(1, 1), 
            padding=(dp(10), dp(10))
        )
        
        self.log_scroll = ScrollView(
            size_hint=(1, 1), 
            do_scroll_x=False, 
            do_scroll_y=True
        )
        
        self.log_container = BoxLayout(
            orientation='vertical', 
            size_hint_y=None, 
            spacing=dp(1), 
            padding=(dp(3), dp(3))
        )
        
        self.log_container.bind(
            minimum_height=lambda *x: setattr(
                self.log_container, 
                'height', 
                self.log_container.minimum_height
            )
        )
        
        self.log_scroll.add_widget(self.log_container)
        log_frame.add_widget(self.log_scroll)
        
        self.scroll_down_btn = Button(
            text="НОВЫЕ", 
            font_size=sp(10),
            size_hint=(None, None),
            size=(dp(70), dp(30)),
            pos_hint={'right': 1, 'top': 1},
            background_color=(0.3, 0.3, 0.3, 0.8),
            background_normal='',
            opacity=0,
            disabled=True,
            on_press=lambda x: self.scroll_to_latest()
        )
        log_frame.add_widget(self.scroll_down_btn)
        
        self.log_scroll.bind(scroll_y=self.on_scroll)
        
        root.add_widget(log_frame)
        
        # Строка с кнопками управления
        btn_row = BoxLayout(size_hint_y=None, height=dp(55), spacing=dp(5))
        
        btn_row.add_widget(Button(
            text="СТАРТ", 
            font_size=sp(13), 
            bold=True, 
            background_color=(0.18, 0.35, 0.18, 1), 
            background_normal='', 
            on_press=self.start_game
        ))
        
        btn_row.add_widget(Button(
            text="ПАУЗА", 
            font_size=sp(13), 
            background_color=(0.35, 0.35, 0.18, 1), 
            background_normal='', 
            on_press=self.pause_game
        ))
        
        btn_row.add_widget(Button(
            text="ЗАНОВО", 
            font_size=sp(13), 
            background_color=(0.35, 0.18, 0.18, 1), 
            background_normal='', 
            on_press=self.reset_game
        ))
        
        btn_row.add_widget(Button(
            text="ТЕСТ", 
            font_size=sp(13), 
            bold=True,
            background_color=(0.25, 0.3, 0.4, 1), 
            background_normal='', 
            on_press=self.show_manual_quiz
        ))
        
        root.add_widget(btn_row)
        
        # Строка со схемой
        scheme_row = BoxLayout(size_hint_y=None, height=dp(40), spacing=dp(5))
        
        scheme_row.add_widget(Button(
            text="ПОКАЗАТЬ СХЕМУ",
            font_size=sp(13),
            background_color=(0.2, 0.25, 0.4, 1),
            background_normal='',
            size_hint_x=1,
            on_press=self.show_scheme
        ))
        
        root.add_widget(scheme_row)
        
        Clock.schedule_interval(self._process_log_queue, LOG_QUEUE_PROCESS_INTERVAL)
        Clock.schedule_once(lambda dt: self.show_section_selector(), 0.5)
        
        return root
    
    def show_scheme(self, instance=None):
        self.scheme_open = True
        self.running = False
        
        container = BoxLayout(orientation='vertical', padding=dp(10))
        container.add_widget(Label(
            text="СХЕМА АГРЕГАТА (вид сверху)",
            font_size=sp(14),
            bold=True,
            color=(1, 0.8, 0, 1),
            size_hint_y=None,
            height=dp(30),
            halign='center'
        ))
        
        self.scheme_widget = AggregateScheme(size_hint=(1, 1))
        container.add_widget(self.scheme_widget)
        self.scheme_widget.running = self.machine.running
        self.scheme_widget.draw_scheme()
        
        self.scheme_popup = Popup(
            title="",
            content=container,
            size_hint=(0.95, 0.85),
            auto_dismiss=True,
            title_color=(1, 0.8, 0, 1),
            separator_color=(1, 0.8, 0, 1)
        )
        self.scheme_popup.bind(on_dismiss=lambda x: self._on_scheme_close())
        self.scheme_popup.open()
        Clock.schedule_interval(self.update_scheme, 0.1)
    
    def _on_scheme_close(self):
        self.scheme_open = False
        if hasattr(self, 'scheme_widget'):
            self.scheme_widget.running = False
    
    def update_scheme(self, dt):
        if hasattr(self, 'scheme_widget') and self.scheme_widget:
            self.scheme_widget.running = self.machine.running
    
    def on_pause(self):
        self.running = False
        Logger.info('FactoryGame: App paused')
        return True
    
    def on_resume(self):
        Logger.info('FactoryGame: App resumed')
    
    def on_scroll(self, instance, value):
        if value <= 0.05:
            self.scroll_down_btn.opacity = 0
            self.scroll_down_btn.disabled = True
    
    def scroll_to_latest(self):
        self.log_scroll.scroll_y = 0
        self.scroll_down_btn.opacity = 0
        self.scroll_down_btn.disabled = True
    
    def show_section_selector(self):
        content = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        
        content.add_widget(Label(
            text="Твой участок?", 
            font_size=sp(20), 
            bold=True, 
            color=(1, 0.8, 0, 1), 
            halign='center', 
            size_hint_y=None, 
            height=dp(40)
        ))
        
        for section in ["Модуль", "Склейка", "Релёвки", "Хвост"]:
            btn = Button(
                text=section, 
                font_size=sp(15), 
                color=(1, 1, 1, 1), 
                background_color=(0.25, 0.3, 0.4, 1), 
                background_normal='', 
                size_hint_y=None, 
                height=dp(50)
            )
            btn.bind(on_press=lambda instance, s=section: self.select_section(s))
            content.add_widget(btn)
        
        self.section_popup = Popup(
            title="Выбор участка", 
            content=content, 
            size_hint=(0.85, 0.6), 
            auto_dismiss=False, 
            title_color=(1, 0.8, 0, 1), 
            separator_color=(1, 0.8, 0, 1)
        )
        self.section_popup.open()
    
    def select_section(self, section):
        self.selected_section = section
        self.section_popup.dismiss()
        self.used_questions[section] = []
        self.log(f"Выбран участок: {section}", 'quiz')
        self.update_status()
    
    def show_manual_quiz(self, instance):
        if not self.selected_section:
            self.log("СНАЧАЛА ВЫБЕРИТЕ УЧАСТОК!", 'problem')
            self.show_section_selector()
            return
        
        if self.scheme_open:
            self.log("Закройте схему для прохождения теста", 'problem')
            return
        
        if self.quiz_popup_open:
            return
        
        self.show_quiz()
    
    def show_quiz(self):
        if self.scheme_open:
            return
            
        if self.quiz_popup_open or not self.selected_section:
            return
        
        questions = QUIZ_QUESTIONS.get(self.selected_section, [])
        used = self.used_questions.get(self.selected_section, [])
        available = [i for i in range(len(questions)) if i not in used]
        
        if not available:
            used.clear()
            available = list(range(len(questions)))
        
        q_idx = random.choice(available)
        used.append(q_idx)
        question_data = questions[q_idx]
        
        self.running = False
        self.quiz_popup_open = True
        
        content = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(8))
        
        content.add_widget(Label(
            text=question_data["question"], 
            font_size=sp(16), 
            bold=True, 
            color=(1, 1, 1, 1), 
            halign='center', 
            valign='middle', 
            size_hint_y=None, 
            height=dp(70), 
            text_size=(Window.width - dp(60), None)
        ))
        
        correct_answer = question_data["answers"][question_data["correct"]]
        shuffled_answers = question_data["answers"][:]
        random.shuffle(shuffled_answers)
        
        for answer in shuffled_answers:
            btn = Button(
                text=answer, 
                font_size=sp(14), 
                color=(1, 1, 1, 1), 
                background_color=(0.2, 0.25, 0.35, 1), 
                background_normal='', 
                size_hint_y=None, 
                height=dp(48), 
                halign='center'
            )
            btn.bind(on_press=lambda instance, a=answer, c=correct_answer: self.answer_quiz(a, c))
            content.add_widget(btn)
        
        self.quiz_popup = Popup(
            title=f"Вопрос: {self.selected_section}", 
            content=content, 
            size_hint=(0.9, 0.6), 
            auto_dismiss=False, 
            title_color=(1, 0.8, 0, 1), 
            separator_color=(1, 0.8, 0, 1)
        )
        self.quiz_popup.open()
    
    def answer_quiz(self, selected_answer, correct_answer):
        self.quiz_popup.dismiss()
        self.quiz_popup_open = False
        
        if selected_answer == correct_answer:
            self.operator.quiz_correct += 1
            self.log("ВИКТОРИНА: Правильно!", 'success')
        else:
            self.operator.quiz_wrong += 1
            self.log(f"ВИКТОРИНА: Неправильно. Ответ: {correct_answer}", 'problem')
        
        self.running = True
        self.update_status()
        
        if not self.game_thread or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=self.game_loop, daemon=True)
            self.game_thread.start()
    
    def create_order(self):
        self.order_counter += 1
        order_type = random.choice(ORDER_TYPES)
        quantity = random.randint(100, 1000)
        order = Order(self.order_counter, order_type, quantity)
        self.orders.append(order)
        
        if not self.current_order:
            self.current_order = order
            order.status = "В работе"
            self.log(f"НОВЫЙ ЗАКАЗ #{order.id}: {order.type}, {order.quantity} шт", 'order')
        else:
            self.log(f"Заказ #{order.id} добавлен в очередь: {order.type}, {order.quantity} шт", 'info')
    
    def cancel_order(self):
        if self.orders:
            order = random.choice(self.orders)
            if order.status != "Отгружен":
                order.status = "Отменён"
                self.orders.remove(order)
                self.log(f"ЗАКАЗ #{order.id} ОТМЕНЁН клиентом!", 'cancel')
                
                if order == self.current_order:
                    self.current_order = None
                    if self.orders:
                        self.current_order = self.orders[0]
                        self.current_order.status = "В работе"
                        self.log(f"Начат заказ #{self.current_order.id}: {self.current_order.type}", 'success')
                    else:
                        self.log("Все заказы отменены. Ждём новые...", 'info')
    
    def manual_pallet_loading(self):
        if not self.current_pallet:
            if self.current_order:
                self.current_pallet = Palleto(self.current_order.id, self.current_order.type)
                self.log(f"Хвостовик начал новую палету для заказа #{self.current_order.id}", 'pallet')
        
        if self.current_pallet:
            if self.current_pallet.add_box():
                if self.current_pallet.boxes % 10 == 0:
                    self.log(f"Укладка ВГ: {self.current_pallet.boxes}/{self.current_pallet.max_boxes} коробок", 'pallet')
                
                if self.current_pallet.boxes >= self.current_pallet.max_boxes:
                    self.current_pallet.wrap()
                    self.pallets.append(self.current_pallet)
                    self.log(f"Палета готова! Заказ #{self.current_order.id}: {self.current_pallet.boxes} коробок", 'success')
                    self.current_pallet = None
                    
                    if self.current_order and self.current_order.update_progress(20):
                        self.log(f"ЗАКАЗ #{self.current_order.id} ВЫПОЛНЕН!", 'success')
                        self.orders.remove(self.current_order)
                        self.current_order = None
                        
                        if self.orders:
                            self.current_order = self.orders[0]
                            self.current_order.status = "В работе"
                            self.log(f"Начат заказ #{self.current_order.id}: {self.current_order.type}", 'success')
    
    def defect_jams_relevek(self):
        if random.random() < 0.3:
            self.relevek_jam = True
            self.defect_streak += 1
            self.log(f"БРАК ПРОЛЕТЕЛ! Релёвки забиты! (Проблема #{self.defect_streak})", 'defect')
            self.machine.running = False
            
            if self.defect_streak > 3:
                self.log("КРИТИЧЕСКИЙ ИЗНОС РЕЛЁВОК! Требуется замена!", 'problem')
                self.defect_streak = 0
                self.schedule_restart(5)
            else:
                self.schedule_restart(2)
        else:
            self.log("Брак пойман на выходе!", 'success')
            self.defect_streak = 0
    
    def log(self, message, tag='info'):
        color = COLORS.get(tag, (1, 1, 1, 1))
        self.log_queue.put((message, color))
    
    def _process_log_queue(self, dt):
        try:
            while True:
                message, color = self.log_queue.get_nowait()
                self._add_log_widget(message, color)
        except Empty:
            pass
    
    def _add_log_widget(self, message, color):
        was_at_bottom = self.log_scroll.scroll_y <= 0.05
        
        if len(self.log_container.children) >= MAX_LOG_ENTRIES:
            self.log_container.remove_widget(self.log_container.children[0])
        
        log_label = Label(
            text=message, 
            font_size=sp(13), 
            color=color, 
            halign='left', 
            valign='middle', 
            size_hint_y=None, 
            height=dp(22), 
            text_size=(Window.width - dp(40), dp(22))
        )
        
        self.log_container.add_widget(log_label)
        
        if was_at_bottom:
            Clock.schedule_once(lambda dt: setattr(self.log_scroll, 'scroll_y', 0), 0.05)
        else:
            self.scroll_down_btn.opacity = 1
            self.scroll_down_btn.disabled = False
    
    def get_random_chatter(self):
        available = [p for p in HEADSET_CHATTER if p != self.last_chatter]
        if not available:
            available = HEADSET_CHATTER
        phrase = random.choice(available)
        self.last_chatter = phrase
        return phrase
    
    def update_status(self):
        section = self.selected_section or "Не выбран"
        status = f"Бригада: {self.current_brigade['name']}\n"
        status += f"Участок: {section}\n"
        
        if self.current_order:
            status += f"Заказ #{self.current_order.id}: {self.current_order.type}, {self.current_order.progress}%\n"
        else:
            status += "Нет активных заказов\n"
        
        status += f"Викторина: Правильных: {self.operator.quiz_correct} | Неправильных: {self.operator.quiz_wrong}"
        
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', status), 0)
    
    def start_game(self, instance):
        if self.running:
            return
        
        if not self.selected_section:
            self.log("Сначала выберите участок!", 'problem')
            self.show_section_selector()
            return
        
        self.running = True
        self.log_container.clear_widgets()
        
        self.log("=== НАЧАЛО СМЕНЫ ===", 'info')
        self.log(f"Участок: {self.selected_section}", 'quiz')
        self.log(f"Бригада: {self.current_brigade['name']}", 'brigadier')
        
        self.create_order()
        
        if self.machine.start():
            self.log("Гофроагрегат запущен", 'success')
        else:
            self.log("Ошибка запуска агрегата", 'problem')
        
        if not self.game_thread or not self.game_thread.is_alive():
            self.game_thread = threading.Thread(target=self.game_loop, daemon=True)
            self.game_thread.start()
    
    def pause_game(self, instance):
        self.running = False
        self.log("Работа приостановлена", 'info')
    
    def reset_game(self, instance):
        self.running = False
        time.sleep(0.1)
        
        self.operator = MachineOperator()
        self.machine = CorrugatorMachine()
        self.selected_section = None
        self.used_questions = {}
        self.last_chatter = None
        self.quiz_popup_open = False
        self.restart_scheduled = False
        self.scheme_open = False
        
        self.orders = []
        self.current_order = None
        self.order_counter = 0
        self.pallets = []
        self.current_pallet = None
        self.defect_streak = 0
        self.relevek_jam = False
        
        self.log_container.clear_widgets()
        self.log("Симулятор сброшен", 'info')
        
        Clock.schedule_once(lambda dt: self.show_section_selector(), 0.3)
    
    def change_brigade(self):
        self.operator.action_count = 0
        brigade_idx = BRIGADES.index(self.current_brigade)
        self.current_brigade = BRIGADES[(brigade_idx + 1) % len(BRIGADES)]
        self.karshik = Karshik(random.choice(KARSHIK_NAMES))
        
        self.log(f"=== СМЕНА БРИГАДЫ: {self.current_brigade['name']} ===", 'brigadier')
        self.log("Новый карщик", 'karshik')
    
    def schedule_restart(self, delay=1.5):
        if not self.restart_scheduled:
            self.restart_scheduled = True
            Clock.schedule_once(self._restart_machine, delay)
    
    def _restart_machine(self, dt):
        self.restart_scheduled = False
        if self.running:
            if self.machine.start():
                self.log("Агрегат перезапущен", 'success')
            else:
                self.log("Не удалось перезапустить агрегат", 'problem')
    
    def game_loop(self):
        while self.running:
            try:
                self.operator.action_count += 1
                
                if self.machine.running:
                    self.machine.produce()
                    if random.random() < 0.08:
                        self.log("Агрегат работает...", 'work')
                    
                    if self.current_order and random.random() < 0.1:
                        self.current_order.update_progress(5)
                    
                    if self.current_order and self.current_order.type == "ВГ" and random.random() < 0.15:
                        self.manual_pallet_loading()
                
                if random.random() < 0.05:
                    self.create_order()
                
                if random.random() < 0.02:
                    self.cancel_order()
                
                if self.machine.running and random.random() < 0.04:
                    self.defect_jams_relevek()
                
                if self.operator.action_count >= BRIGADE_CHANGE_INTERVAL:
                    self.change_brigade()
                
                if random.random() < 0.005:
                    self.log(CHUFYR_PHRASE, 'chufyr')
                    self.machine.running = False
                    self.schedule_restart(2)
                
                if random.random() < 0.03:
                    condition = self.karshik.deliver_roll()
                    if condition == "битый":
                        self.log("Карщик привёз БИТЫЙ ролик!", 'defect')
                        self.machine.running = False
                        self.schedule_restart(1.5)
                
                if random.random() < 0.02:
                    section = random.choice(list(WET_PART_PROBLEMS.keys()))
                    worker = "лицевик" if section == "лицевой" else "модульщик"
                    problem = random.choice(WET_PART_PROBLEMS[section])
                    self.log(f"ОБРЫВ: {problem}", 'wet_part')
                    
                    if self.operator.is_smoking(worker):
                        self.log(f"{worker} БРОСАЕТ КУРИЛКУ!", 'smoke')
                        self.operator.return_from_smoke(worker)
                    
                    self.machine.running = False
                    self.schedule_restart(1.5)
                
                if random.random() < 0.02:
                    worker = random.choice(list(DRY_PART_PROBLEMS.keys()))
                    problem = random.choice(DRY_PART_PROBLEMS[worker])
                    self.log(f"ПРОБЛЕМА: {problem}", 'dry_part')
                    self.machine.running = False
                    self.schedule_restart(1.5)
                
                if random.random() < 0.05:
                    worker = random.choice(["лицевик", "модульщик", "релёвщик", "хвостовик"])
                    if not self.operator.is_smoking(worker):
                        self.operator.go_smoke(worker)
                        self.log(f"{worker} ушёл курить", 'smoke')
                
                if random.random() < 0.20:
                    chatter = self.get_random_chatter()
                    self.log(f"Наушники: {chatter}", 'headset')
                
                if random.random() < 0.02:
                    glue = self.klevar.make_glue()
                    self.machine.glue_level = min(100, self.machine.glue_level + glue)
                    self.log(f"Клеевар: +{glue}% клея", 'klevar')
                
                self.update_status()
                
                time.sleep(LOG_DELAY)
                
            except Exception as e:
                Logger.error(f'FactoryGame: Error in game_loop: {e}')
                time.sleep(LOG_DELAY)


if __name__ == '__main__':
    FactoryGameKivy().run()
