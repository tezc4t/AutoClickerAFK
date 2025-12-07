## 🖱️ Anti-AFK AutoClicker for Online Infiltration Games

This project provides a simple yet effective **AutoClicker** designed to bypass Anti-AFK (Away From Keyboard) systems in online games, especially those requiring long waiting periods (such as looting or event queues) which might lead to disconnection due to inactivity (e.g., in games like *Sea of Thieves* - SOT).

### ⚠️ Disclaimer

**The use of any third-party software, including auto-clickers, may violate the game's Terms of Service and could result in warnings, suspensions, or permanent bans on your account.**

**Use this software at your own risk.** The author of this project is not responsible for any consequences arising from its use. This project is provided for educational purposes and as a proof of concept.

---

## Features

* **Quick Toggle** : Use a dedicated hotkey to easily start and stop the auto-clicking function.
* **Configurable Interval** : Allows setting the click frequency (in milliseconds) to simulate ongoing activity.
* **Randomized Mode (Recommended)** : Includes an option to introduce slight random variation in the clicking time, making the activity less predictable and potentially harder for certain Anti-AFK systems to detect.

---

## 🛠️ Installation and Configuration

### Prerequisites

* [**Python 3**](https://www.python.org/downloads/) (Required to run the script, if applicable).
* The following Python libraries (if using a Python script):
    * `pynput` : For mouse simulation and keyboard listening.
    * `time` : For timing and delays.
    * `random` : (Optional) For randomized mode.

```bash
# Example dependency installation if using Python
pip install pynput
