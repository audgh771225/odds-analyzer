
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(layout="wide")
st.title("동일배당 분석기 (일반 + 핸디캡)")

team_home = st.text_input("홈팀명", "유르고르덴스")
team_away = st.text_input("원정팀명", "첼시")
score = st.text_input("스코어", "1 : 2")

st.subheader("일반 배당 및 구매율")
gen_odds = [st.number_input(f"일반 {r} 배당", value=v) for r, v in zip(['패', '무', '승'], [4.20, 3.50, 1.80])]
gen_buy = [st.number_input(f"일반 {r} 구매율 (%)", value=v) for r, v in zip(['패', '무', '승'], [15.0, 20.0, 65.0])]
gen_stats = [20, 20, 60]

st.subheader("핸디 배당 및 구매율")
hdc_odds = [st.number_input(f"핸디 {r} 배당", value=v) for r, v in zip(['패', '무', '승'], [3.20, 3.50, 1.90])]
hdc_buy = [st.number_input(f"핸디 {r} 구매율 (%)", value=v) for r, v in zip(['패', '무', '승'], [10.0, 25.0, 65.0])]
hdc_stats = [20, 30, 50]

colors = ['#cc0000', '#888888', '#0066cc']
labels = ['패', '무', '승']
circle_pos = [0.25, 0.5, 0.75]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))
for ax in axs:
    ax.axis("off")

# 일반
ax = axs[0]
ax.text(0.5, 0.95, "[ 일반 동일배당 분석기 ]", ha='center', fontsize=15, fontweight='bold')
ax.text(0.05, 0.91, f"{team_home}   {score}   {team_away}", fontsize=11)
ax.text(0.05, 0.88, "일반 배당: " + " / ".join([f"{l} {v}" for l, v in zip(labels, gen_odds)]), fontsize=11)
ax.text(0.05, 0.85, "일반 구매율:", fontsize=11, fontweight='bold')
x = 0.05
for val, lab, col in zip(gen_buy, labels, colors):
    w = val * 0.004
    ax.add_patch(patches.Rectangle((x, 0.82), w, 0.025, facecolor=col))
    ax.text(x + w + 0.01, 0.8325, f"{lab} {val:.1f}% 구매율", fontsize=10)
    x += w + 0.04

ax.text(0.5, 0.77, "과거 동일 일반배당 결과", ha='center', fontsize=11)
for l, p, c, xp in zip(labels, gen_stats, colors, circle_pos):
    ax.add_patch(patches.Wedge((xp, 0.69), 0.06, 0, 360 * p / 100, facecolor=c))
    ax.add_patch(patches.Circle((xp, 0.69), 0.06, fill=False, edgecolor='gray'))
    ax.text(xp, 0.69, f"{p}%", ha='center', va='center', fontsize=11, color='white' if p > 50 else 'black')
    ax.text(xp, 0.655, f"{l} ({p}%)", ha='center', fontsize=9)

# 핸디
ax = axs[1]
ax.text(0.5, 0.95, "[ 핸디캡 동일배당 분석기 ]", ha='center', fontsize=15, fontweight='bold')
ax.text(0.05, 0.91, f"{team_home}   {score}   {team_away}", fontsize=11)
ax.text(0.05, 0.88, "핸디 배당: " + " / ".join([f"{l} {v}" for l, v in zip(labels, hdc_odds)]), fontsize=11)
ax.text(0.05, 0.85, "핸디 구매율:", fontsize=11, fontweight='bold')
x = 0.05
for val, lab, col in zip(hdc_buy, labels, colors):
    w = val * 0.004
    ax.add_patch(patches.Rectangle((x, 0.82), w, 0.025, facecolor=col))
    ax.text(x + w + 0.01, 0.8325, f"{lab} {val:.1f}% 구매율", fontsize=10)
    x += w + 0.04

ax.text(0.5, 0.77, "과거 동일 핸디배당 결과", ha='center', fontsize=11)
for l, p, c, xp in zip(labels, hdc_stats, colors, circle_pos):
    ax.add_patch(patches.Wedge((xp, 0.69), 0.06, 0, 360 * p / 100, facecolor=c))
    ax.add_patch(patches.Circle((xp, 0.69), 0.06, fill=False, edgecolor='gray'))
    ax.text(xp, 0.69, f"{p}%", ha='center', va='center', fontsize=11, color='white' if p > 50 else 'black')
    ax.text(xp, 0.655, f"{l} ({p}%)", ha='center', fontsize=9)

st.pyplot(fig)
