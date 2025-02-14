import re

def load_sample_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""

# 1. Extracting Email Addresses
def extract_emails(text):
    emails_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(emails_pattern, text)

# 2. Extracting URLs
def extract_urls(text):
    url_pattern = r'https?://[^\s/$.?#].[^\s]*'
    return re.findall(url_pattern, text)

# 3. Extracting Phone Numbers
def extract_phone_numbers(text):
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(phone_pattern, text)

# 4. Extracting Credit Card Numbers
def extract_credit_cards(text):
    credit_card_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    return re.findall(credit_card_pattern, text)

# 5. Extracting HTML Tags
def extract_html_tags(text):
    html_tag_pattern = r'<[^>]+>'
    return re.findall(html_tag_pattern, text)

# 6. Extracting Hashtags
def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)

# 7. Extracting Currency Amounts
def extract_currency_amounts(text):
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)

# 8. Extracting Time
def extract_times(text):
    time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    return re.findall(time_pattern, text)

# Main function
def main():
    index1 = load_sample_text('index1.txt')

    if not index1:
        return  # Stop execution if the file is not found

    print("\nExtracted Emails:", extract_emails(index1))
    print("\nExtracted URLs:", extract_urls(index1))
    print("\nExtracted Phone Numbers:", extract_phone_numbers(index1))
    print("\nExtracted Credit Card Numbers:", extract_credit_cards(index1))
    print("\nExtracted HTML Tags:", extract_html_tags(index1))
    print("\nExtracted Hashtags:", extract_hashtags(index1))
    print("\nExtracted Currency Amounts:", extract_currency_amounts(index1))
    print("\nExtracted Times:", extract_times(index1))

if __name__ == '__main__':
    main()
