# Pomodoro Timer  
**A customizable productivity timer with usage statistics**  

## Overview  
The **Pomodoro Timer** is a desktop application designed to boost productivity by alternating focus and break sessions. It features a fully customizable interface, personalized time settings, and comprehensive usage tracking, enabling users to maximize productivity.

---

## Features  
### 🕒 Timer Modes  
- **Focus Mode**: Helps you stay productive during work or study sessions.  
- **Break Mode**: Encourages necessary rest between focus sessions.  
- **Auto Switch**: Automatically transitions between focus and break modes when after one mode ends.

### 🎨 Customization  
- Select from **5 unique color themes** for a personalized experience.  
- Customizable focus and break durations  

### 📊 Usage Statistics  
- Tracks **daily usage time**, **monthly totals**, and highlights the **best performance** day of the month.  
- Usage data is stored and retrieved from an SQL database for long-term tracking.  

---

## Technologies Used  
### 🛠 Languages  
- **Python**  
- **SQL**  

### 💻 Frameworks and Tools  
- **PyQt**: For creating the user interface and managing layouts.  
- **SQLite**: For storing and retrieving usage statistics.  
- **Git**: For version control.  

---

## How It Works  
1. **Customizable Timer**: Users set their desired focus and break durations.  
2. **Seamless Operation**: The app switches automatically between modes when a session ends.  
3. **Data Tracking**: The app stores session data in a database for analytics and progress tracking.  
4. **View Statistics**: Users can view their daily and monthly usage stats, along with their best performance day.  

---

### Demo

https://github.com/user-attachments/assets/20817f06-d53b-44eb-a9ad-3912eccb9c57

<img width="350" alt="Screenshot 2024-12-02 at 10 44 29 PM" src="https://github.com/user-attachments/assets/fa9d71b8-6e33-4934-8874-080c72b20b57">

<img width="350" alt="Screenshot 2024-12-02 at 10 45 01 PM" src="https://github.com/user-attachments/assets/1a7ba626-2ecc-48e9-aa10-6bffb06436ba">

<img width="350" alt="Screenshot 2024-12-02 at 10 45 33 PM" src="https://github.com/user-attachments/assets/091337ba-770c-4d2c-b45e-b8654485705e">

<img width="350" alt="Screenshot 2024-12-02 at 10 45 13 PM" src="https://github.com/user-attachments/assets/5d7fcb26-c2e9-4ec0-8d9d-fe97d88b92d0">

<img width="351" alt="Screenshot 2024-12-02 at 10 45 23 PM" src="https://github.com/user-attachments/assets/8113efcf-eb84-43a3-b935-1c11b7d0bed4">


---

## Installation  

1. Install Python version 3.11
2. Install PyQt6
3. Intall Pygame (used only for sound effects)
4. Clone the repository, change to cloned directory and run timer_gui.py with python 3.11:  
   ```bash
   git clone https://github.com/yourusername/pomodoro-timer.git
   cd pomodoro-timer
   python3.11 timer_gui.py
