# Урок 0: Налаштування середовища, знайомство з Git і Python

## Мета уроку

Підготувати робоче середовище: встановити необхідні інструменти, написати перший Python-скрипт і навчитися базовому Git-флоу.

---

## 1. Встановлення Homebrew

Homebrew — менеджер пакетів для macOS. Через нього зручно встановлювати більшість інструментів.

В терміналі виконати:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Перевірити, що встановлення пройшло успішно:

```bash
brew --version
```

---

## 2. Встановлення Python

Спочатку перевірити, чи Python вже встановлений:

```bash
which python
python --version
```

Якщо команди не знайдені або версія застаріла — встановити через Homebrew:

```bash
brew install python
```

Перевірити версію:

```bash
python3 --version
```

> Очікуваний результат: `Python 3.1х.x`.

---

## 3. Встановлення VS Code

Завантажити VS Code з офіційного сайту: https://code.visualstudio.com

Або через Homebrew:

```bash
brew install --cask visual-studio-code
```

### Розширення для роботи з Python

Після запуску VS Code встановити розширення (`Cmd+Shift+X`):

1. **Python** (від Microsoft) — підтримка мови, автодоповнення, запуск скриптів
2. **GitLens** (від GitKraken) — розширена робота з Git прямо в редакторі: хто і коли змінив рядок, історія файлу, порівняння гілок

### Автозбереження файлів

Увімкнути автозбереження: `File → Auto Save` (або `Cmd+Shift+P` → ввести `Auto Save` → вибрати **Toggle Auto Save**).

Після цього VS Code зберігатиме файли автоматично після кожної зміни — більше не потрібно натискати `Cmd+S`.

---

## 4. Знайомство з Git

### Що таке Git?

Git — система контролю версій. Вона дозволяє:
- зберігати історію змін у коді
- працювати в команді без конфліктів
- повертатися до попередніх версій

### Ключові поняття

| Поняття | Пояснення |
|---|---|
| **Repository (репозиторій)** | Папка з проєктом, яку відстежує Git |
| **Commit** | Знімок стану файлів у певний момент |
| **Branch (гілка)** | Окрема лінія розробки |
| **Pull Request (PR)** | Запит на злиття гілки з основною |

### Налаштування Git

```bash
git config --global user.name "Ваше Ім'я"
git config --global user.email "your@email.com"
```

---

## 5. Hello World і перший PR

Далі вся робота ведеться в спільному репозиторії курсу: https://github.com/kstamax/web-aqa-lessons

### Крок 1 — Клонувати репозиторій

```bash
git clone https://github.com/kstamax/web-aqa-lessons.git
cd web-aqa-lessons
```

### Крок 2 — Створити власну гілку

```bash
git checkout -b lesson-00
```

### Крок 3 — Створити папку і файл

```bash
mkdir assignments/lesson_00
touch assignments/lesson_00/hello.py
```

Або через UI в VS Code.

Відкрити `hello.py` у VS Code і написати:

```python
print("Hello, World!")
print("Мій перший крок у Web AQA")
```

### Крок 4 — Запустити скрипт

```bash
python3 assignments/lesson_00/hello.py
```

> Очікуваний результат:
> ```
> Hello, World!
> Мій перший крок у Web AQA
> ```

### Крок 5 — Зафіксувати зміни (commit)

```bash
git add assignments/lesson_00/hello.py
git commit -m "lesson 00: add hello world script"
```

### Крок 6 — Відправити (запушити) гілку на GitHub

Спочатку налаштувати автоматичний мапінг локальної гілки на `origin`:

```bash
git config --global push.autoSetupRemote true
```

Після цього достатньо просто:

```bash
git push
```

> `push.autoSetupRemote` — глобальне налаштування, яке автоматично встановлює upstream (`-u origin <гілка>`) при першому пуші нової гілки. Надалі для будь-якої нової гілки `git push` спрацює без додаткових аргументів.

### Крок 7 — Створити Pull Request

1. Перейти до репозиторію: https://github.com/kstamax/web-aqa-lessons
2. Натиснути **"Compare & pull request"**
3. Переконатися, що PR відкривається в гілку `main`
4. Заповнити назву: `lesson 00`
5. Натиснути **"Create pull request"**

---

## Шпаргалка: основні команди Git

```bash
git status              # показати поточний стан
git add <файл>          # додати файл до commit
git add .               # додати всі змінені файли
git commit -m "текст"   # зафіксувати зміни
git push.               # відправити(пушнути) гілку на GitHub
git pull                # отримати зміни з GitHub
git log --oneline       # коротка історія commits
git checkout -b <назва> # створити нову гілку і перейти на неї
```