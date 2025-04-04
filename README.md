"# Key-Logger" 


This is a keylogger script that captures real-time keystrokes and automatically sends the logs via email for easy tracking.

🔍 How it works:

The script runs in the background by hiding the console window (on Windows) to remain undetected.

It uses the keyboard module to capture every keystroke and stores them in a buffer.

When the "Enter" key is pressed, the captured keystrokes are sent via secure email using Gmail's SMTP service (via port 587 and STARTTLS encryption).

If the "Escape" key is pressed, the program stops logging and exits.

Final logs are saved to a text file before the program exits, just in case the script is interrupted unexpectedly.

🔐 Why this project?

This was a great opportunity to dive deeper into system-level programming and email protocols in Python. I got hands-on experience with concepts like handling keyboard events, email automation, and interacting with operating system libraries to hide processes.

⚠️ Disclaimer: This project is for educational purposes only. I do not condone or encourage any malicious use of this technology.
