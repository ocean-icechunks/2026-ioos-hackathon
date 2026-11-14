"""Where your time goes, without and with a coding agent (Eli Holmes's estimate).

Run from anywhere: python scripts/fig_agent_time.py
Writes slides/images/fig_agent_time.png.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from talk_style import FULL, INK, INK_SOFT, SERIES, apply_style

OUT = Path(__file__).resolve().parents[1] / "slides" / "images" / "fig_agent_time.png"

# One fixed colour per activity, in the theme's categorical order, so the same
# activity has the same colour in both pies.
ACTIVITIES = {
    "Writing and debugging code": SERIES[0],
    "Planning and deciding": SERIES[1],
    "Reading the agent's code": SERIES[2],
    "Checking and adjusting what the agent did": SERIES[3],
}

BEFORE = {"Writing and debugging code": 80, "Planning and deciding": 20}
AFTER = {
    "Planning and deciding": 50,
    "Checking and adjusting what the agent did": 35,
    "Reading the agent's code": 15,
}

apply_style()
fig, axes = plt.subplots(1, 2, figsize=FULL)

for ax, (title, shares) in zip(axes, [("Without an agent", BEFORE), ("With an agent", AFTER)]):
    labels = list(shares)
    wedges, _ = ax.pie(
        list(shares.values()),
        colors=[ACTIVITIES[k] for k in labels],
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 2},  # 2 px surface gap between slices
    )
    # Direct labels: the share inside each slice, in white on the fill.
    for w, (name, pct) in zip(wedges, shares.items()):
        ang = (w.theta1 + w.theta2) / 2
        import math
        x, y = 0.62 * math.cos(math.radians(ang)), 0.62 * math.sin(math.radians(ang))
        ax.text(x, y, f"{pct}%", ha="center", va="center", color="white", fontsize=13, fontweight=600)
    ax.set_title(title, loc="center", fontsize=14, color=INK, pad=6)
    ax.set_aspect("equal")

# One shared legend names every activity, so identity never rests on colour alone.
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in ACTIVITIES.values()]
fig.legend(handles, list(ACTIVITIES), loc="outside lower center", ncol=2, frameon=False,
           fontsize=10.5, labelcolor=INK_SOFT, handlelength=1.2)

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT)
print(f"wrote {OUT}")
