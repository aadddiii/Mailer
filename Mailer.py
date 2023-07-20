import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import datetime
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import help_mailer
import email_validator
import email_sender

def validate_emails():
    emails = receiver_email.get()
    email_list = [email.strip() for email in emails.split(',')]
    invalid_emails = email_validator.validate_email_list(email_list)

    if invalid_emails:
        messagebox.showerror("Invalid Emails", f"The following emails are invalid or have non-existent domains:\n{', '.join(invalid_emails)}")
    else:
        messagebox.showinfo("Valid Emails", "All emails are valid and ready to send.")
    
        
def send_emails():
    try:
        user_email_addr = user_email.get()
        user_password_val = user_password.get()
        receiver_email_addrs = [email.strip() for email in receiver_email.get().split(',')]
        names = [name.strip() for name in personalized_email.get().split(',')]

        # Check if the user wants to send the email in HTML format
        is_html_format = html_format_var.get()

        # Send emails using the email_sender module
        success, message = email_sender.send_emails(user_email_addr, user_password_val, receiver_email_addrs, email_subject.get(), email_message.get("1.0", tk.END), is_html_format, names)
        if success:
            messagebox.showinfo("Success", message)
        else:   
            messagebox.showerror("Error", message)

    except Exception as e:
        messagebox.showerror("Error", f"Error sending emails: {e}")
  
        
def preview_email():
    # Preview email message
    preview_window = tk.Toplevel(window)
    preview_window.title("Email Preview")
    preview_window.geometry("600x400")

    preview_text = scrolledtext.ScrolledText(preview_window, wrap=tk.WORD)
    preview_text.pack(fill=tk.BOTH, expand=True)

    # Set the preview text based on the chosen format (plain text or HTML)
    is_html_format = html_format_var.get()
    if is_html_format:
        message_body = email_message.get("1.0", tk.END)
        preview_text.insert(tk.END, message_body, "html")
    else:
        message_body = email_message.get("1.0", tk.END)
        preview_text.insert(tk.END, message_body)

    # Replace [Name] with the first name from personalized_email field
    names = [name.strip().split()[0] for name in personalized_email.get().split(',')]
    name_index = 0
    while "[Name]" in preview_text.get("1.0", tk.END):
        name_to_replace = names[name_index] if name_index < len(names) else ""
        preview_text.mark_set("insert", "1.0")
        preview_text.search("[Name]", "insert", stopindex=tk.END)
        start_index = preview_text.index("insert")
        end_index = f"{start_index}+{len('[Name]')}c"
        preview_text.delete(start_index, end_index)
        preview_text.insert(start_index, name_to_replace)
        name_index += 1

    preview_text.configure(state="disabled")


def clear_fields():
    user_email.delete(0, tk.END)
    user_password.delete(0, tk.END)
    receiver_email.delete(0, tk.END)
    personalized_email.delete(0, tk.END)
    email_subject.delete(0, tk.END)
    email_message.delete("1.0", tk.END)


def import_emails():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            emails_and_names = file.read().strip()

        email_name_pairs = [pair.strip() for pair in emails_and_names.split(',')]

        emails = []
        names = []
        for pair in email_name_pairs:
            if '-' in pair:
                email, name = pair.split('-', 1)
                emails.append(email.strip())
                names.append(name.strip())
            else:
                messagebox.showwarning("Format Error", f"Invalid format in line: {pair}")

        # Update the receiver_email Entry widget with email addresses
        receiver_email.delete(0, tk.END)
        receiver_email.insert(tk.END, ', '.join(emails))

        # Update the personalized_email Entry widget with names only
        personalized_email.delete(0, tk.END)
        personalized_email.insert(tk.END, ', '.join(names))


def save_email_results(successful_emails, unsuccessful_emails):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    filename = f"email_results_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Successful Emails:\n")
        for email in successful_emails:
            file.write(f"{email}\n")

        file.write("\nUnsuccessful Emails:\n")
        for email in unsuccessful_emails:
            file.write(f"{email}\n")


def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def adjust_layout(event):
    window_width = event.width
    window_height = event.height

    if window_width >= 1000 and window_height >= 700:
        input_frame.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        buttons_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        footer_frame.place(relx=1.0, rely=1.0, anchor=tk.SE)
    else:
        input_frame.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
        buttons_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        footer_frame.place(relx=1.0, rely=1.0, anchor=tk.SE)
 
        
def animate_label(label):
    alpha = getattr(label, "alpha", 255)
    if alpha <= 0:
        alpha = 255
    else:
        alpha -= 15

    label.alpha = alpha
    foreground = f"#{alpha:02X}{alpha:02X}{alpha:02X}"
    label.configure(foreground=foreground)
    label.after(100, animate_label, label)


def exit_application():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()
        

window = tk.Tk()
window.title("Email Automator")
window.state("zoomed")
window.configure(bg="#f0f0f0")
window.bind("<Configure>", adjust_layout)

primary_color = "#007BFF" 
secondary_color = "#FFA500"  
background_color = "#F0F0F0"  
text_color = "#333333" 


style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#f0f0f0")
style.configure("TScrollbar", background="#ffffff")
style.configure("Horizontal.TScrollbar", background="#ffffff")
style.configure("Footer.TLabel", background="#303030", foreground="#ffffff", font=("Arial", 12, "bold"))
style.configure("Custom.TButton",
                background=primary_color,
                foreground="#ffffff",
                font=("Arial", 12, "bold"),
                borderwidth=0,
                relief="flat",
                padx=10,
                pady=5)

style.map("Custom.TButton",
          background=[("active", secondary_color),
                      ("pressed", primary_color),
                      ("disabled", "#d3d3d3")])
style.configure("Custom.TEntry",
                fieldbackground="#ffffff", 
                font=("Arial", 12), 
                bordercolor="#d9d9d9",
                borderwidth=1)
style.configure("Custom.TLabel",
                background="#f0f0f0",
                font=("Arial", 12))



# Create a frame for the input fields
input_frame = ttk.Frame(window, padding=20)

# Create labels and entry fields
user_email_label = ttk.Label(input_frame, text="Your Email:", style="Custom.TLabel")
user_email = ttk.Entry(input_frame, width=40, style="Custom.TEntry")

user_password_label = ttk.Label(input_frame, text="Your Password:", style="Custom.TLabel")
user_password = ttk.Entry(input_frame, show="*", width=40, style="Custom.TEntry")

receiver_email_label = ttk.Label(input_frame, text="Receiver Email(s):", style="Custom.TLabel")
receiver_email = ttk.Entry(input_frame, width=60, style="Custom.TEntry")

personalized_email_label = ttk.Label(input_frame, text="Personalized Email(s):", style="Custom.TLabel")
personalized_email = ttk.Entry(input_frame, width=60, style="Custom.TEntry")

subject_label = ttk.Label(input_frame, text="Subject:", style="Custom.TLabel")
email_subject = ttk.Entry(input_frame, width=60, style="Custom.TEntry")

message_label = ttk.Label(input_frame, text="Message:")
email_message = scrolledtext.ScrolledText(input_frame, height=8, width=50, wrap=tk.WORD)

# Create buttons frame
buttons_frame = ttk.Frame(window, padding=20)

# Create buttons
validate_button = ttk.Button(buttons_frame, text="Validate Emails", command=validate_emails, style="Custom.TButton")
import_button = ttk.Button(buttons_frame, text="Import Emails", command=import_emails, style="Custom.TButton")
send_button = ttk.Button(buttons_frame, text="Send Emails", command=send_emails, style="Custom.TButton")
clear_button = ttk.Button(buttons_frame, text="Clear All", command=clear_fields, style="Custom.TButton")
preview_button = ttk.Button(buttons_frame, text="Preview Email", command=preview_email, style="Custom.TButton")
help_button = ttk.Button(buttons_frame, text="Help", command=help_mailer.open_help_menu, style="Custom.TButton")

# Create footer frame
footer_frame = ttk.Frame(window, padding=5)

# Create internet connection indicator
internet_label = ttk.Label(footer_frame, text="Internet:", foreground="#ffffff", background="#303030")
if check_internet_connection():
    internet_status = ttk.Label(footer_frame, text="Connected", foreground="#00ff00", background="#303030")
else:
    internet_status = ttk.Label(footer_frame, text="Disconnected", foreground="#ff0000", background="#303030")

# Position input fields
user_email_label.grid(row=0, column=0, pady=5, sticky=tk.E)
user_email.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

user_password_label.grid(row=1, column=0, pady=5, sticky=tk.E)
user_password.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

receiver_email_label.grid(row=2, column=0, pady=5, sticky=tk.E)
receiver_email.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

personalized_email_label.grid(row=3, column=0, pady=5, sticky=tk.E)
personalized_email.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

subject_label.grid(row=4, column=0, pady=5, sticky=tk.E)
email_subject.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

message_label.grid(row=5, column=0, pady=5, sticky=tk.E)
email_message.grid(row=5, column=1, padx=10, pady=5, columnspan=2, rowspan=2, sticky=tk.W)

# Position buttons
validate_button.grid(row=0, column=0, padx=5, pady=10)
import_button.grid(row=0, column=1, padx=5, pady=10)
send_button.grid(row=1, column=0, padx=5, pady=10)
clear_button.grid(row=1, column=1, padx=5, pady=10)
preview_button.grid(row=0, column=3, padx=5, pady=10)
help_button.grid(row=1, column=3, padx=5)


animated_label = ttk.Label(window, text="EMAIL AUTOMATOR", font=("Arial", 18, "bold"))
animated_label.pack(pady=30)
animate_label(animated_label)


exit_button = tk.Button(window, text="X", bg="#ff0000", font=("Arial", 12, "bold"), relief=tk.FLAT, command=exit_application)
exit_button.place(x=window.winfo_screenwidth() - 30, y=10, anchor=tk.NW)

# Position footer
internet_label.pack(side=tk.LEFT)
internet_status.pack(side=tk.LEFT, padx=5)

# Position frames
input_frame.pack(side=tk.TOP)
buttons_frame.pack(side=tk.TOP)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Add a checkbox to enable HTML format
html_format_var = tk.BooleanVar()
html_format_checkbox = ttk.Checkbutton(input_frame, text="Send as HTML", variable=html_format_var)
html_format_checkbox.grid(row=7, column=0, columnspan=3, pady=5)

window.mainloop()
