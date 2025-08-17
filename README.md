# Recruiter Outreach Email Generator

A Python tool that automates the process of generating personalized outreach emails and possible recruiter email addresses for job applications.

## Features

- **Personalized Email Generation**: Creates customized outreach emails using templates with placeholders
- **Recruiter Email Discovery**: Generates multiple possible email patterns for recruiters based on their name and company domain
- **Easy Command Line Interface**: Simple CLI for quick email generation
- **Template-Based System**: Uses customizable email templates with `{{COMPANY}}` and `{{NAME}}` placeholders

## Email Patterns Generated

The tool generates these common recruiter email patterns:

1. `firstlast@domain.com` (e.g., johnsmith@company.com)
2. `first.last@domain.com` (e.g., john.smith@company.com)
3. `f[1-3]last@domain.com` (e.g., jsmith, josmith, johsmith@company.com)
4. `first@domain.com` (e.g., john@company.com)
5. `last@domain.com` (e.g., smith@company.com)

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd recutier-outrearch
   ```

## Usage

### Basic Usage

**Generate email with arguments:**

```bash
python generate.py <recruiter_first_name> <recruiter_last_name> <company_domain> <company_name>
```

**Examples:**

```bash
python generate.py john smith google.com Google
python generate.py sarah jones apple.com Apple
python generate.py mike brown amazon.com Amazon
```

**Use defaults:**

```bash
python generate.py
```

### Output

The tool will display:

1. **Generated Email**: Personalized subject and body
2. **Possible Recruiter Emails**: List of email patterns to try

Example output:

```
Generating email for: john smith at Google
Company domain: google.com

==================================================
GENERATED EMAIL
==================================================
Subject: Software Engineering Intern - Ethan McFarland
--------------------------------------------------
Body:
Hi john,

My name is Ethan and I'm currently studying Computer Science...
==================================================

==================================================
POSSIBLE RECRUITER EMAILS
==================================================
1. johnsmith@google.com
2. john.smith@google.com
3. jsmith@google.com
4. josmith@google.com
5. johsmith@google.com
6. john@google.com
7. smith@google.com
==================================================
```

## Email Template

The tool uses `email.txt` as a template with these placeholders:

- `{{NAME}}` → Recruiter's first name
- `{{COMPANY}}` → Company name

Example template:

```
Software Engineering Intern - Ethan McFarland

Hi {{NAME}},

My name is Ethan and I'm currently studying Computer Science at the University of Toronto.
I have been using {{COMPANY}} for just under a decade now and absolutely love it!

...
```

## Functions

### `generate_ourtreach_email(first_name, company)`

Generates personalized email content by reading from `email.txt` and replacing placeholders.

### `generate_rectuiter_email(first_name, last_name, company_domain)`

Generates a list of possible recruiter email addresses based on common patterns.

## File Structure

```
recutier-outrearch/
├── generate.py          # Main script
├── email.txt           # Email template
├── README.md          # This file
```

## Customization

- **Email Template**: Edit `email.txt` to customize your outreach message
- **Email Patterns**: Modify `generate_rectuiter_email()` to add/remove email patterns
- **Default Values**: Change the default recruiter/company info in the main section
