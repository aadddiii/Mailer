import re
import socket

def is_valid_email(email):
    # Email format validation using regular expression
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def is_valid_domain(email):
    # Domain verification by trying to establish a connection to the mail server
    domain = email.split('@')[1]
    try:
        records = socket.getaddrinfo(domain, 25)
        return True
    except socket.gaierror:
        return False
    except socket.timeout:
        raise Exception("DNS query timeout")
    except Exception as e:
        raise Exception(f"DNS query failed: {e}")

def validate_email_list(email_list):
    # Validates a list of email addresses
    invalid_emails = []

    for email in email_list:
        email = email.strip()
        if not is_valid_email(email):
            invalid_emails.append(email)
        elif not is_valid_domain(email):
            invalid_emails.append(email)

    return invalid_emails
