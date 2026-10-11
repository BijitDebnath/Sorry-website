"""
A heartfelt "I'm sorry" website for Sneha (Misti Doi) 💗
Made by Bijit — built with Python + Streamlit, designed for phones.

Run:   pip install streamlit
       streamlit run app.py
"""

import random
import streamlit as st
import streamlit.components.v1 as components

# ─────────────────────────────────────────────────────────────
#  ✏️  EDIT YOUR WORDS HERE — make them truly yours, Bijit
# ─────────────────────────────────────────────────────────────
HER_NAME = "Sneha"
NICKNAME = "Misti Doi"
YOUR_NAME = "Bijit"

APOLOGY_PARAGRAPHS = [
    f"Dear {HER_NAME},",
    "I have been thinking about what happened, and I want to say this plainly: "
    "I am sorry. I hurt your feelings, and that is on me.",
    "I am not going to explain it away or tell you why it wasn't that bad. "
    "What matters is that you were hurt, and you didn't deserve it.",
    "I wish I had thought before I spoke. I wish I had stopped to see how it "
    "would feel on your side. I didn't, and I understand if you are still upset.",
    "You are one of the best things in my life. Hurting you is the last thing "
    "I ever want to do, and I am truly sorry that I did.",
    "Take all the time you need. Whenever you are ready to talk, I'll be "
    "right here, and I'll just listen.",
    f"With all my heart,<br>{YOUR_NAME} 💗",
]

REASONS = [
    ("🌷", "Your smile",
     "It can fix my worst day in a second, and I miss it when it's gone."),
    ("🍮", "You're my Misti Doi",
     "Sweet, warm and comforting. Nobody else feels like home the way you do."),
    ("🫶", "Your kind heart",
     "You care deeply about people, and that is something rare and beautiful."),
    ("✨", "You make ordinary days special",
     "Even the smallest moments become memories when you are in them."),
    ("🌙", "You are real with me",
     "You tell me when something hurts. That honesty is a gift, and I want to deserve it."),
    ("💗", "Just you",
     f"Not for one thing in particular. It's simply you, {HER_NAME}."),
]

SECRET_LETTERS = [
    ("💌", "Open when you're still upset",
     "It's okay to be upset. Your feelings are valid, and you don't have to "
     "hurry to forgive me. I'll be here, patient and listening, for as long "
     "as it takes."),
    ("🌙", "Open when you miss me",
     "I miss you too, more than I can say. Whatever the distance between us "
     "right now, you are on my mind and in my heart."),
    ("🍮", "A Misti Doi special",
     "If I could, I'd bring you a whole earthen pot of the sweetest misti "
     "doi. But nothing in it would be as sweet as you."),
    ("📝", "Things I've learned",
     "That your feelings come first when I'm in the wrong. That 'sorry' means "
     "more with change behind it. And that I should listen before I answer."),
    ("🎁", "A tiny surprise", "SURPRISE"),
    ("🤗", "A big virtual hug", "HUG"),
]

PROMISES = [
    ("👂", "I will listen", "Really listen, without interrupting or getting defensive."),
    ("🌱", "I will learn", "From this, so I hurt you less and understand you more."),
    ("🤝", "I will show it", "Not just with words. You'll see it in how I act every day."),
]

FINAL_MESSAGE = (
    f"{HER_NAME}, thank you for reading all of this. Whether you forgive me "
    "today or need more time, I understand. I just want you to know how much "
    f"you matter to me, my {NICKNAME}."
)

# ─────────────────────────────────────────────────────────────
#  Page setup
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=f"For {HER_NAME} 💗",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

TOTAL_STEPS = 5

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Nunito:wght@400;600;700&display=swap');
:root{--rose:#e0507a;--rose-deep:#b83263;--blush:#ffe3ec;--petal:#fff5f8;--plum:#4a1d3a;--caramel:#c98a4b;}
html,body,.stApp{background:linear-gradient(170deg,#ffe9f0 0%,#ffd1e0 55%,#ffc2d6 100%)!important;color:var(--plum);font-family:'Nunito',sans-serif;}
#MainMenu,header,footer,[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stStatusWidget"]{display:none!important;visibility:hidden;}
.block-container{max-width:460px!important;padding:1.4rem 1.1rem 4rem!important;}
h1,h2,h3{font-family:'Dancing Script',cursive!important;color:var(--rose-deep)!important;text-align:center;font-weight:700!important;}
.title{font-family:'Dancing Script',cursive;font-size:3.1rem;line-height:1.1;color:var(--rose-deep);text-align:center;margin:0.4rem 0;}
.heading{font-family:'Dancing Script',cursive;font-size:2.2rem;line-height:1.15;color:var(--rose-deep);text-align:center;margin:0.2rem 0 1rem;}
.sub{text-align:center;font-size:1.05rem;line-height:1.6;color:var(--plum);opacity:.85;}
.big-emoji{text-align:center;font-size:4.2rem;margin:.6rem 0 0;animation:beat 1.6s ease-in-out infinite;}
.pot{text-align:center;font-size:3.4rem;margin-top:1rem;}
.dots{display:flex;justify-content:center;gap:8px;margin:0 0 1.2rem;}
.dot{width:9px;height:9px;border-radius:50%;background:#f3b4c8;}
.dot.on{background:var(--rose);width:22px;border-radius:6px;}
.letter{background:var(--petal);border-radius:18px;padding:1.4rem 1.3rem;margin:.4rem 0 1.2rem;border:1.5px solid #f6bfd1;box-shadow:0 10px 28px rgba(184,50,99,.14);font-size:1.06rem;line-height:1.75;}
.letter p{margin:0 0 .95rem;}
.letter p:last-child{margin-bottom:0;}
.letter p:first-child{font-family:'Dancing Script',cursive;font-size:1.7rem;color:var(--rose-deep);}
.reason{background:var(--petal);border-radius:16px;padding:1rem 1.1rem;margin:0 0 .8rem;border-left:5px solid var(--rose);box-shadow:0 6px 18px rgba(184,50,99,.1);}
.reason b{color:var(--rose-deep);font-size:1.08rem;}
.reason span{display:block;margin-top:.25rem;line-height:1.55;}
.revealed{background:var(--petal);border-radius:18px;padding:1.3rem;margin:1rem 0;border:1.5px dashed var(--rose);text-align:center;line-height:1.7;font-size:1.05rem;animation:pop .5s ease;}
.revealed .t{font-family:'Dancing Script',cursive;font-size:1.6rem;color:var(--rose-deep);display:block;margin-bottom:.3rem;}
.hug{font-size:5rem;display:block;animation:hug 1.2s ease-in-out infinite;}
.promise{display:flex;gap:.8rem;align-items:flex-start;background:var(--petal);border-radius:16px;padding:.9rem 1rem;margin-bottom:.7rem;box-shadow:0 6px 18px rgba(184,50,99,.1);}
.promise .e{font-size:1.7rem;}
.promise b{color:var(--rose-deep);}
.sign{font-family:'Dancing Script',cursive;font-size:1.9rem;color:var(--rose-deep);text-align:center;margin-top:1rem;}
.stButton>button{width:100%;min-height:3.2rem;border-radius:999px;border:none;background:linear-gradient(135deg,#f0709a,#d83b72);color:#fff;font-family:'Nunito',sans-serif;font-weight:700;font-size:1.05rem;box-shadow:0 8px 20px rgba(216,59,114,.35);transition:transform .15s;}
.stButton>button:hover,.stButton>button:focus,.stButton>button:active{color:#fff;border:none;transform:scale(1.02);}
.stButton>button p{font-size:1.05rem;}
.heart{position:fixed;bottom:-40px;z-index:0;pointer-events:none;opacity:0;animation:rise linear infinite;}
@keyframes rise{0%{transform:translateY(0) translateX(0) rotate(0deg);opacity:0;}10%{opacity:.85;}100%{transform:translateY(-115vh) translateX(28px) rotate(25deg);opacity:0;}}
@keyframes beat{0%,100%{transform:scale(1);}50%{transform:scale(1.14);}}
@keyframes pop{0%{transform:scale(.92);opacity:0;}100%{transform:scale(1);opacity:1;}}
@keyframes hug{0%,100%{transform:scale(1) rotate(-4deg);}50%{transform:scale(1.18) rotate(4deg);}}
@media (prefers-reduced-motion:reduce){.heart,.big-emoji,.hug{animation:none;}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────
def floating_hearts(count: int = 16, seed: int = 7) -> None:
    """Soft hearts drifting up the screen."""
    rng = random.Random(seed)
    glyphs = ["💗", "💖", "💕", "🌷", "💞", "🌸"]
    spans = []
    for _ in range(count):
        spans.append(
            f'<span class="heart" style="left:{rng.randint(2, 94)}%;'
            f"font-size:{rng.randint(16, 34)}px;"
            f"animation-duration:{rng.randint(7, 14)}s;"
            f'animation-delay:{rng.uniform(0, 9):.1f}s;">{rng.choice(glyphs)}</span>'
        )
    st.markdown("".join(spans), unsafe_allow_html=True)


def progress_dots(step: int) -> None:
    dots = "".join(
        f'<div class="dot{" on" if i == step else ""}"></div>'
        for i in range(1, TOTAL_STEPS + 1)
    )
    st.markdown(f'<div class="dots">{dots}</div>', unsafe_allow_html=True)


def scroll_to_top() -> None:
    """Phones keep their scroll position between screens, so reset it."""
    components.html(
        "<script>const m=window.parent.document.querySelector('section.main')"
        "||window.parent.document.querySelector('[data-testid=\"stMain\"]');"
        "if(m){m.scrollTo(0,0);}window.parent.scrollTo(0,0);</script>",
        height=0,
    )


def go(step: int) -> None:
    st.session_state.step = step


# ─────────────────────────────────────────────────────────────
#  State
# ─────────────────────────────────────────────────────────────
if "step" not in st.session_state:
    st.session_state.step = 0
if "opened" not in st.session_state:
    st.session_state.opened = None
if "seen" not in st.session_state:
    st.session_state.seen = set()

step = st.session_state.step
scroll_to_top()
floating_hearts(seed=step + 3)

if step > 0:
    progress_dots(step)

# ─────────────────────────────────────────────────────────────
#  Step 1 — Welcome
# ─────────────────────────────────────────────────────────────
if step == 0:
    st.markdown('<div style="height:7vh"></div>', unsafe_allow_html=True)
    st.markdown('<div class="big-emoji">💗</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="title">Hey, {HER_NAME}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<p class="sub">my {NICKNAME} 🍮<br><br>'
        "I made something small, just for you.<br>"
        "Please take a minute to look through it.</p>",
        unsafe_allow_html=True,
    )
    st.markdown('<div style="height:2rem"></div>', unsafe_allow_html=True)
    st.button("Begin 💗", on_click=go, args=(1,), key="begin")

# ─────────────────────────────────────────────────────────────
#  Step 2 — The apology
# ─────────────────────────────────────────────────────────────
elif step == 1:
    st.markdown('<div class="heading">I\'m so sorry 🥺</div>', unsafe_allow_html=True)
    body = "".join(f"<p>{p}</p>" for p in APOLOGY_PARAGRAPHS)
    st.markdown(f'<div class="letter">{body}</div>', unsafe_allow_html=True)
    st.button("Next 🌷", on_click=go, args=(2,), key="to_reasons")

# ─────────────────────────────────────────────────────────────
#  Step 3 — Reasons she is special
# ─────────────────────────────────────────────────────────────
elif step == 2:
    st.markdown(
        f'<div class="heading">Why you matter to me 🌷</div>'
        f'<p class="sub">My {NICKNAME}, here are a few reasons.</p><div style="height:.8rem"></div>',
        unsafe_allow_html=True,
    )
    for emoji, title, text in REASONS:
        st.markdown(
            f'<div class="reason"><b>{emoji} {title}</b><span>{text}</span></div>',
            unsafe_allow_html=True,
        )
    st.markdown('<div style="height:.4rem"></div>', unsafe_allow_html=True)
    st.button("Secret letters 💌", on_click=go, args=(3,), key="to_letters")

# ─────────────────────────────────────────────────────────────
#  Step 4 — Secret letters
# ─────────────────────────────────────────────────────────────
elif step == 3:
    st.markdown('<div class="heading">Secret letters 💌</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub">Tap a button to open a letter. You can open them all.</p>',
        unsafe_allow_html=True,
    )
    st.markdown('<div style="height:.6rem"></div>', unsafe_allow_html=True)

    for i, (emoji, label, _) in enumerate(SECRET_LETTERS):
        if st.button(f"{emoji}  {label}", key=f"letter_{i}"):
            st.session_state.opened = i
            st.session_state.seen.add(i)

    opened = st.session_state.opened
    if opened is not None:
        emoji, label, text = SECRET_LETTERS[opened]
        if text == "HUG":
            st.markdown(
                '<div class="revealed"><span class="hug">🫂</span>'
                f'<span class="t">A big hug for you</span>'
                f"Squeezing you tight from here, {HER_NAME}. "
                "I'll give you the real one whenever you want it.</div>",
                unsafe_allow_html=True,
            )
        elif text == "SURPRISE":
            st.balloons()
            st.markdown(
                '<div class="revealed"><span class="hug">🎁</span>'
                f'<span class="t">Surprise!</span>'
                "A date that's all yours: your favourite food, your choice of "
                "place, and I'll plan nothing except being fully there with you. "
                "(And yes, there will be misti doi. 🍮)</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="revealed"><span class="t">{emoji} {label}</span>{text}</div>',
                unsafe_allow_html=True,
            )

    st.markdown('<div style="height:.8rem"></div>', unsafe_allow_html=True)
    if len(st.session_state.seen) >= 1:
        st.button("One last thing 🫶", on_click=go, args=(4,), key="to_final")

# ─────────────────────────────────────────────────────────────
#  Step 5 — The final message
# ─────────────────────────────────────────────────────────────
else:
    st.balloons()
    st.markdown('<div class="heading">My promise to you 🫶</div>', unsafe_allow_html=True)
    for emoji, title, text in PROMISES:
        st.markdown(
            f'<div class="promise"><div class="e">{emoji}</div>'
            f"<div><b>{title}</b><br>{text}</div></div>",
            unsafe_allow_html=True,
        )
    st.markdown(
        f'<div class="letter" style="margin-top:1rem"><p style="font-family:inherit;font-size:1.06rem;color:inherit">{FINAL_MESSAGE}</p></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="sign">Always yours,<br>{YOUR_NAME} 💗</div><div class="pot">🍮</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div style="height:1.2rem"></div>', unsafe_allow_html=True)
    st.button("Read it again 💗", on_click=go, args=(0,), key="restart")
