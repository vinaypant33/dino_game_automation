# Dino Game Automation

A Python automation script that plays Chrome's offline "Dino Game" (chrome://dino/) automatically using screen-pixel detection and simulated keypresses.

## How It Works
- Launches a Chrome browser session via Selenium and navigates to `chrome://dino/`.
- Takes continuous screenshots with `pyautogui` and inspects specific pixel coordinates on screen to detect approaching obstacles (cacti, birds).
- Simulates `space` (jump) or `down` (duck) keypresses using the `keyboard` library based on detected obstacles.
- Can be stopped at any time with `Ctrl+Q`.

## Tech Stack
- Python
- Selenium (browser automation)
- PyAutoGUI (screen capture & pixel detection)
- keyboard (simulated key events)

## How to Run
1. Install dependencies:
   ```
   pip install selenium pyautogui keyboard
   ```
2. Ensure Chrome and a matching ChromeDriver are installed.
3. Run the script:
   ```
   python main.py
   ```
4. The script opens Chrome, navigates to the Dino Game, and starts playing automatically.

## Notes
This is a practice project built to experiment with screen-based automation, pixel detection, and simulated keyboard/mouse control — a fun exploration of automation concepts using Selenium and PyAutoGUI.
