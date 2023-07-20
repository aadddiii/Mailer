import tkinter as tk
from tkinter import ttk
from tkinter import font

def open_help_menu():
    help_window = tk.Toplevel()
    help_window.title("Help Menu")
    help_window.geometry("600x400")

    # Create a canvas to hold the notebook and add a vertical scrollbar
    canvas = tk.Canvas(help_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(help_window, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to scroll with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a frame inside the canvas to hold the notebook
    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    # Create a notebook to organize the help content with tabs for each step
    notebook = ttk.Notebook(frame)

    # Step 1: Enter Your Email Credentials
    step1_frame = ttk.LabelFrame(notebook, text="Step 1: Enter Your Email Credentials")
    step1_text ="""
    In this step, you will provide your Gmail credentials to enable the Email Automator application to send emails on your behalf. It's essential to use an app-specific password instead of your regular Gmail password for enhanced security.

    1. Open the Email Automator Application:
        - Launch the Email Automator application on your computer. You can do this by running the provided script or executing the main app file.

    2. Enter Your Gmail Address:
        - In the "Your Email" field, type your Gmail address from which you want to send the emails.
        - Ensure that you enter the correct Gmail address associated with the Gmail account you wish to use for sending emails.

    3. Use an App-Specific Password:
        - In the "Your Password" field, you should **NOT** enter your regular Gmail account password.
        - Gmail requires you to use an app-specific password when using third-party applications like the Email Automator to send emails through your Gmail account.
        - To generate an app-specific password, visit the following link: [Generate App Password](https://support.google.com/accounts/answer/185833?hl=en).
        - This link will guide you through the steps to create a unique app password specifically for the Email Automator application.

    **Important Note:**
    - Using an app-specific password enhances the security of your Gmail account. It ensures that the Email Automator has limited access to your account and cannot access your main Gmail password.
    - After generating the app-specific password, enter it into the "Your Password" field in the Email Automator application.

    4. Proceed to the Next Steps:
        - Once you have entered your Gmail address and the app-specific password, you are now ready to proceed to the next steps of the Email Automator application.
        - Continue with "Step 2: Add Recipient Email Addresses" to enter the email addresses of the recipients to whom you want to send the emails.
    """
    step1_label = ttk.Label(step1_frame, text=step1_text, wraplength=500, justify="left")
    step1_label.pack(padx=10, pady=5)

    # Step 2: Add Recipient Email Addresses
    step2_frame = ttk.LabelFrame(notebook, text="Step 2: Add Recipient Email Addresses")
    step2_text = """
    In this step, you will enter the email addresses of the recipients to whom you want to send the emails.

    1. Enter Recipient Email Addresses:
        - In the "Receiver Email(s)" field, type the email addresses of the recipients you want to send the emails to.
        - Separate multiple email addresses with commas if you want to send the same email to multiple recipients.

    2. Personalize Email Messages (Optional):
        - If you want to personalize the email messages for each recipient, you can use the "Personalized Email(s)" field.
        - For each recipient email address, you can enter their respective names in the "Personalized Email(s)" field.
        - The Email Automator will replace the [Name] placeholder in the email subject and body with the corresponding names you provide.

    **Example:**
        If you have the following:
        - Receiver Email(s): john@example.com, jane@example.com
        - Personalized Email(s): John Doe, Jane Smith

        The email sent to john@example.com will have the subject and body with "John Doe" in place of [Name],
        and the email sent to jane@example.com will have "Jane Smith" in place of [Name].

    3. Continue to Compose Your Email:
        - Once you have added the recipient email addresses, you can proceed to "Step 3: Compose Your Email" to write the subject and body of your email.
    """
    step2_label = ttk.Label(step2_frame, text=step2_text, wraplength=500, justify="left")
    step2_label.pack(padx=10, pady=5)

    # Step 3: Compose Your Email
    step3_frame = ttk.LabelFrame(notebook, text="Step 3: Compose Your Email")
    step3_text = """
    In this step, you will compose the email you want to send to the recipients.

    1. Enter Email Subject:
        - In the "Subject" field, type the subject of your email.
    
    2. Compose Email Message:
        - In the "Message" field, type the main body of your email.
    
    3. Choose Email Format (Optional):
        - You can choose to send the email in plain text or HTML format using the "Send as HTML" checkbox.
        - If selected, the Email Automator will treat the email message as HTML content.

    4. Preview Your Email (Optional):
        - If you want to preview your email before sending, you can click the "Preview Email" button.
        - A new window will display the email message as it will appear to the recipients.

    5. Validate Your Email Addresses:
        - Before sending, you can click the "Validate Emails" button to check the validity of the entered email addresses.
        - The Email Automator will verify if the email addresses have a correct format and if their domains are valid.

    6. Send Your Email:
        - Click the "Send Emails" button to send the composed email to the specified recipients.

    **Note:** 
        - You can always go back to previous steps using the tabs above to review or make changes.
        - After sending the emails, you will receive a success message indicating that the emails were sent successfully.

    Congratulations! You have now successfully used the Email Automator application to send personalized emails to your recipients.
    """
    step3_label = ttk.Label(step3_frame, text=step3_text, wraplength=500, justify="left")
    step3_label.pack(padx=10, pady=5)

    # Add the tabs to the notebook
    notebook.add(step1_frame, text="Step 1")
    notebook.add(step2_frame, text="Step 2")
    notebook.add(step3_frame, text="Step 3")

    # Pack the notebook to fill the frame inside the canvas
    notebook.pack(fill=tk.BOTH, expand=True)

    # Configure aesthetic improvements
    font_style = font.Font(family="Arial", size=11)
    notebook.configure(style="Custom.TNotebook")
    step1_frame.configure(style="Custom.TLabelframe")
    step2_frame.configure(style="Custom.TLabelframe")
    step3_frame.configure(style="Custom.TLabelframe")
    step1_label.configure(font=font_style)
    step2_label.configure(font=font_style)
    step3_label.configure(font=font_style)

    # Apply custom styles
    style = ttk.Style()
    style.configure("Custom.TNotebook", background="#f0f0f0", borderwidth=0)
    style.configure("Custom.TLabelframe", background="#f0f0f0", borderwidth=2)
    style.map("Custom.TLabelframe",
              background=[("active", "#e0e0e0"), ("!active", "#f0f0f0")],
              highlightcolor=[("active", "#e0e0e0"), ("!active", "#f0f0f0")],
              relief=[("active", "groove"), ("!active", "flat")])

if __name__ == "__main__":
    # Test the help menu by calling the function
    root = tk.Tk()
    root.title("Email Automator")
    root.geometry("400x300")

    help_button = tk.Button(root, text="Help", command=open_help_menu)
    help_button.pack(pady=20)

    root.mainloop()
