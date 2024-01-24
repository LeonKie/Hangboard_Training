# Handboard Training Script Readme

This script facilitates interval endurance training on a handboard, incorporating sounds and messages for each phase. The training consists of sets of workouts and rest periods.

## Prerequisites:
- Python environment
- Libraries: playsound, time, winsound, prompt_toolkit

## Usage:
Ensure the required libraries are installed.

```bash
pip install playsound prompt_toolkit
```
Run the script using a Python interpreter.

```bash
python handboard_training.py
```
Follow the prompts during the training session.

## Features:

Plays sound cues for the start, notice, goal achievement, and session end.
Displays progress bars for both workout and rest periods.
Provides details about the current and upcoming workouts.
Training Structure:

- Three sets of 10-second 20mm hand hangs, followed by 50 seconds of rest.
- Three sets of 10-second 3-finger hangs, followed by 50 seconds of rest.
- One set of 2-finger pocket hangs (middle and ring fingers), followed by 50 seconds of rest.
- One set of 2-finger pocket hangs (index and middle fingers), followed by 50 seconds of rest.
- One set of 4-finger 20mm hangs, followed by 50 seconds of rest.
- One set of 4-finger 40mm hangs, followed by 50 seconds of rest.
- The session concludes with a notification.

## Note:

Adjust the duration and type of workouts as needed.
Ensure sound files (start.wav, notice.wav, goal.wav, end.wav) are available in the script directory.
Feel free to customize the script for your specific handboard training needs.
