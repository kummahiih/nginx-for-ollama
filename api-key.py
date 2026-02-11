import secrets

def generate_api_key(length=32):
    # Generates a URL-safe text string
    return secrets.token_urlsafe(length)

# print it in a form that is easy to use as nginx configuration
new_key = generate_api_key()
print(f'set $OLLAMA_API_TOKEN "Bearer {new_key}";')