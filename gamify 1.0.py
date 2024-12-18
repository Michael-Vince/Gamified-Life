import random
import time

# Game Variables
xp = 0
level = 1
tasks = [
    "Complete Logo Design",
    "Create Motion Graphic",
    "Work on UI Design",
    "Submit Project to Client",
    "Do 10 Push-ups",
    "Take a Walk (15 minutes)",
    "Drink Water (1 Glass)",
    "Meditation (10 minutes)",
    "Read a Book (30 minutes)",
    "Journal Your Thoughts",
    "Take a Break (Relax)",
    "Practice Gratitude"
]
completed_tasks = []
xp_needed_for_level_up = 1000

# Function to display current stats with retro-style
def display_stats():
    print("\n====================")
    print("   GAMIFIED LIFE   ")
    print("====================")
    print(f" Level: {level}")
    print(f" XP: [{xp}/{xp_needed_for_level_up}]")
    print(f" Completed Tasks: {len(completed_tasks)}")
    print("====================")

# Task function to handle task completion and reward XP
def complete_task(task):
    global xp, level
    xp_earned = random.randint(50, 200)  # XP earned can vary by task

    print(f"\nWorking on: {task}")
    time.sleep(2)  # Simulate task duration
    print(f"Task Completed! You've earned {xp_earned} XP.\n")

    xp += xp_earned
    completed_tasks.append(task)
    check_level_up()

# Function to check if the player has leveled up
def check_level_up():
    global xp, level, xp_needed_for_level_up

    if xp >= xp_needed_for_level_up:
        level += 1
        xp -= xp_needed_for_level_up  # Reset XP for next level
        xp_needed_for_level_up += 500  # Increase XP needed for next level
        print("\n🎉 LEVEL UP! 🎉")
        print(f"New Level: {level}\n")

# Retro motivational feedback for work-related tasks
def task_completed_message():
    messages = [
        "Great job! You're crushing it! 💪",
        "Awesome work! The world needs your designs! 🌟",
        "You're on fire! Keep up the amazing work! 🔥",
        "Mission complete! You're one step closer to greatness! 🚀",
    ]
    print(f"\n{random.choice(messages)}\n")

# Retro motivational feedback for health-related tasks
def health_completed_message():
    messages = [
        "You're getting stronger every day! 💪",
        "Your body and mind are thriving! 🌱",
        "Taking care of yourself is key to success! 🧘‍♂️",
        "Amazing! You're building a healthy routine! 🏃‍♂️",
        "Keep it up! You're becoming the best version of yourself! ✨"
    ]
    print(f"\n{random.choice(messages)}\n")

# Special task for relaxation with a timer
def take_a_break():
    print("\nTime to relax! Please take a 5-minute break.")
    print("You can get up, stretch, breathe deeply, or just relax.")
    
    # Simulating a 5-minute break (300 seconds)
    for remaining_time in range(5, 0, -1):
        print(f"\nRelaxation time remaining: {remaining_time} minute(s)")
        time.sleep(60)  # Waiting for 1 minute
    print("\nRelaxation complete! You've earned 100 XP for taking a break.\n")
    global xp
    xp += 100
    health_completed_message()

# Main Game Loop
def game_loop():
    global xp, level

    print("\n====================")
    print("WELCOME TO THE GAME!")
    print("====================\n")

    display_stats()

    while True:
        print("\n--- Choose a Task ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        try:
            choice = int(input("\nSelect a task number (1-12) or 0 to exit: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("\nThanks for playing! Stay motivated!")
            break

        if 1 <= choice <= len(tasks):
            selected_task = tasks[choice - 1]
            if selected_task not in completed_tasks:
                if selected_task == "Take a Break (Relax)":
                    take_a_break()
                else:
                    complete_task(selected_task)
                
                # Check if the task is a health-related task
                if "Push-ups" in selected_task or "Walk" in selected_task or "Drink Water" in selected_task or "Meditation" in selected_task:
                    health_completed_message()
                else:
                    task_completed_message()
            else:
                print(f"\nYou've already completed: {selected_task}.\n")

        display_stats()

# Starting the game
if __name__ == "__main__":
    game_loop()
