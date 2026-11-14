"""From writing the code to directing the work: where Eli Holmes's time goes,
without and with a coding agent (her own estimate, not a measurement).

Run from anywhere: python scripts/fig_agent_time.py
Writes slides/images/fig_agent_time.png.
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt

from talk_style import FULL, INK, INK_SOFT, SERIES, apply_style

OUT = Path(__file__).resolve().parents[1] / "slides" / "images" / "fig_agent_time.png"

# The two pies share no activities, so each is a self-contained chart:
# colours run in the theme's fixed categorical order within each pie, and
# every slice is labelled with its name, so identity never rests on colour.
WITHOUT = {
    "Planning the approach": 20,
    "Writing code": 45,
    "Debugging": 35,
}
WITH = {
    "Defining the task\nand approach": 35,
    "Directing and\nrefining the work": 25,
    "Discussing and\nplanning tests": 25,
    "Reviewing code\nor text": 15,
}

apply_style()
fig, axes = plt.subplots(1, 2, figsize=FULL)

for ax, (title, shares) in zip(axes, [("Without an agent", WITHOUT), ("With an agent", WITH)]):
    wedges, _ = ax.pie(
        list(shares.values()),
        colors=SERIES[: len(shares)],
        startangle=90,
        counterclock=False,
        radius=0.8,
        wedgeprops={"edgecolor": "white", "linewidth": 2},  # 2 px surface gap
    )
    for w, (name, pct) in zip(wedges, shares.items()):
        ang = math.radians((w.theta1 + w.theta2) / 2)
        # Share inside the slice, name just outside it.
        ax.text(0.5 * math.cos(ang), 0.5 * math.sin(ang), f"{pct}%", ha="center",
                va="center", color="white", fontsize=12, fontweight=600)
        x, y = 0.93 * math.cos(ang), 0.93 * math.sin(ang)
        ax.text(x, y, name, ha="left" if x >= 0 else "right", va="center",
                color=INK_SOFT, fontsize=9.5, linespacing=1.15)
    ax.set_title(title, loc="center", fontsize=14, color=INK, pad=4)
    ax.set_xlim(-1.75, 1.75)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect("equal")

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT)
print(f"wrote {OUT}")
