def generate_ourtreach_email(first_name, company):
    """
    Generate an outreach email by reading from email.txt and replacing placeholders.
    Replace placeholders:
    {{COMPANY}} = company name
    {{NAME}} = first name

    Args:
        first_name (str): The recipient's first name
        company (str): The company name
    
    Returns:
        str: The personalized email content
    """
    # Read the email template from email.txt
    with open('email.txt', 'r', encoding='utf-8') as file:
        email_template = file.read().split('\n')

    subject = email_template[0]

    body = '\n'.join(email_template[1:])
    body = body.replace('{{COMPANY}}', company).replace('{{NAME}}', first_name)
    
    return subject, body

def generate_rectuiter_email(first_name, last_name, company_domain):
    """
    Generate a list of possible recruiter email patterns.
    
    Args:
        first_name (str): The recruiter's first name
        last_name (str): The recruiter's last name
        company_domain (str): The company domain (e.g., 'company.com')
    
    Returns:
        list: List of possible email addresses
    """
    # Clean and normalize inputs
    first_name = first_name.lower().strip()
    last_name = last_name.lower().strip()
    company_domain = company_domain.lower().strip()
    
    # Remove any leading @ if present
    if company_domain.startswith('@'):
        company_domain = company_domain[1:]
    
    possible_emails = []
    
    # Pattern 1: first name + last name
    possible_emails.append(f"{first_name}{last_name}@{company_domain}")
    
    # Pattern 2: first name + dot + last name
    possible_emails.append(f"{first_name}.{last_name}@{company_domain}")
    
    # Pattern 3: first 3 letters of first name + last name
    for i in range(1,4):
        possible_emails.append(f"{first_name[:i]}{last_name}@{company_domain}")
    
    # Pattern 4: first name only
    possible_emails.append(f"{first_name}@{company_domain}")
    
    # Pattern 5: last name only
    possible_emails.append(f"{last_name}@{company_domain}")
    
    # Remove duplicates while preserving order
    seen = set()
    unique_emails = []
    for email in possible_emails:
        if email not in seen:
            seen.add(email)
            unique_emails.append(email)
    
    return unique_emails


if __name__ == "__main__":
    import sys
    
    # Check if arguments are provided
    if len(sys.argv) < 5:
        print("Usage: python generate.py <recruiter_first_name> <recruiter_last_name> <company_domain> <company_name>")
        print("Example: python generate.py john smith microsoft.com Microsoft")
        print("\nOr run without arguments to use defaults:")
        print("python generate.py")
        sys.exit(1)
    
    # Get arguments from command line
    if len(sys.argv) == 5:
        recuiter_first_name = sys.argv[1].lower()
        recuiter_last_name = sys.argv[2].lower()
        company_domain = sys.argv[3].lower()
        company_name = sys.argv[4]
    else:
        # Default values
        recuiter_first_name = "ethan"
        recuiter_last_name = "mcfarland"
        company_domain = "microsoft.com"
        company_name = "Microsoft"
    
    print(f"Generating email for: {recuiter_first_name} {recuiter_last_name} at {company_name}")
    print(f"Company domain: {company_domain}")
    print()
    
    subject, body = generate_ourtreach_email(recuiter_first_name, company_name)

    recruiter_emails = generate_rectuiter_email(recuiter_first_name, recuiter_last_name, company_domain)

    print("=" * 50)
    print("GENERATED EMAIL")
    print("=" * 50)
    print(f"Subject: {subject}")
    print("-" * 50)
    print("Body:")
    print(body)
    print("=" * 50)
    print()
    
    print("=" * 50)
    print("POSSIBLE RECRUITER EMAILS")
    print("=" * 50)
    for i, email in enumerate(recruiter_emails, 1):
        print(f"{i}. {email}")
    print("=" * 50)


