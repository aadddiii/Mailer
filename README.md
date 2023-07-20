# Email Automator

Email Automator is a Python desktop application that allows users to send personalized emails to multiple recipients using their Gmail account. The application has a user-friendly interface that guides users through the process of composing and sending emails.

## Features

- Securely send personalized emails using your Gmail account.
- Validate email addresses for correct format and domain existence.
- Compose emails with the option to format the content as HTML.
- Preview the email before sending.
- Step-by-step guide to help users navigate through the process.

## Requirements

To run the Email Automator application, you need the following:

- Python 3.6+
- Tkinter (included with Python)
- smtplib (included with Python)
- email (included with Python)

## Installation

1. Clone the repository or download the ZIP file.
2. Install the required Python packages: tkinter, smtplib, email

## Usage

1. Run the `Mailer.py` script:

2. The application window will open with three steps:

   - Step 1: Enter Your Email Credentials
   - Step 2: Add Recipient Email Addresses
   - Step 3: Compose Your Email

3. Follow the on-screen instructions in each step to enter your email credentials, recipient email addresses, and compose your email.

4. Click the "Validate Emails" button in Step 2 to verify the validity of the entered email addresses.

5. Optionally, you can click the "Preview Email" button in Step 3 to see how the composed email will appear.

6. Finally, click the "Send Emails" button in Step 3 to send the personalized emails to the recipients.

**Note:** To send emails, you need to allow less secure apps in your Gmail settings. Alternatively, use a Gmail App Password to authenticate the application. Instructions for generating an app password can be found [here](https://support.google.com/accounts/answer/185833?hl=en).


## Contributing

Contributions to the Email Automator project are welcome. If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial use.
