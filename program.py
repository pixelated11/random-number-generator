import customtkinter as ctk
import random
import time

global font 
font = "Arial"
# ── theme ──────────────────────────────────────────────────────────────────
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ── app window ─────────────────────────────────────────────────────────────
app = ctk.CTk()
app.title("Random Number Generator")
app.geometry("480x560")
app.resizable(False, False)

# ── title ──────────────────────────────────────────────────────────────────
ctk.CTkLabel(
    app,
    text="Random Number Generator",
    font=ctk.CTkFont(family=font, size=18, weight="bold"),
).pack(pady=(28, 4))

ctk.CTkLabel(
    app,
    text="by pixelated.",
    font=ctk.CTkFont(family=font, size=12),
    text_color="gray",
).pack(pady=(0, 24))

# ── input frame ────────────────────────────────────────────────────────────
frame = ctk.CTkFrame(app, corner_radius=12)
frame.pack(padx=36, pady=8, fill="x")

ctk.CTkLabel(
    frame,
    text="Starting range",
    font=ctk.CTkFont(family=font, size=13),
).grid(row=0, column=0, padx=20, pady=(18, 4), sticky="w")

start_entry = ctk.CTkEntry(
    frame,
    placeholder_text="e.g. 0",
    font=ctk.CTkFont(family=font, size=14),
    height=40,
    corner_radius=8,
)
start_entry.grid(row=1, column=0, padx=20, pady=(0, 16), sticky="ew")

ctk.CTkLabel(
    frame,
    text="End range",
    font=ctk.CTkFont(family=font, size=13),
).grid(row=2, column=0, padx=20, pady=(4, 4), sticky="w")

end_entry = ctk.CTkEntry(
    frame,
    placeholder_text="e.g. 100",
    font=ctk.CTkFont(family=font, size=14),
    height=40,
    corner_radius=8,
)
end_entry.grid(row=3, column=0, padx=20, pady=(0, 18), sticky="ew")
frame.columnconfigure(0, weight=1)

# ── result label ───────────────────────────────────────────────────────────
result_label = ctk.CTkLabel(
    app,
    text="—",
    font=ctk.CTkFont(family=font, size=52, weight="bold"),
    text_color="#4fc3f7",
)
result_label.pack(pady=20)

status_label = ctk.CTkLabel(
    app,
    text="",
    font=ctk.CTkFont(family=font, size=12),
    text_color="gray",
)
status_label.pack(pady=(0, 8))

# ── generate logic ─────────────────────────────────────────────────────────
def generate():
    start_val = start_entry.get().strip()
    end_val   = end_entry.get().strip()

    if not start_val or not end_val:
        result_label.configure(text="—", text_color="#ef5350")
        status_label.configure(text="Please fill in both fields.")
        return

    try:
        x = int(start_val)
        y = int(end_val)
    except ValueError:
        result_label.configure(text="—", text_color="#ef5350")
        status_label.configure(text="Only whole numbers are allowed.")
        return

    if x >= y:
        result_label.configure(text="—", text_color="#ef5350")
        status_label.configure(text="Starting range must be less than end range.")
        return

    # brief "rolling" animation — matches the original time.sleep feel
    btn.configure(state="disabled")
    status_label.configure(text="Generating…")
    result_label.configure(text_color="#4fc3f7")

    def roll(steps=6):
        if steps > 0:
            result_label.configure(text=str(random.randrange(x, y)))
            app.after(80, roll, steps - 1)
        else:
            final = random.randrange(x, y)
            result_label.configure(text=str(final))
            status_label.configure(text=f"Random number from {x} to {y - 1}")
            btn.configure(state="normal")

    roll()

# ── button ─────────────────────────────────────────────────────────────────
btn = ctk.CTkButton(
    app,
    text="Generate",
    font=ctk.CTkFont(family=font, size=15, weight="bold"),
    height=46,
    corner_radius=10,
    command=generate,
)
btn.pack(padx=36, pady=8, fill="x")

# ── start ──────────────────────────────────────────────────────────────────
app.mainloop()