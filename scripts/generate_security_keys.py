#!/usr/bin/env python3
"""
Generate secure API keys and encryption keys for Bingo Downloader Web
"""
import secrets
import base64
import os
import sys
from pathlib import Path


def generate_api_key() -> str:
    """Generate a secure API key"""
    return secrets.token_hex(32)


def generate_encryption_key() -> str:
    """Generate a Fernet-compatible encryption key"""
    return base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()


def print_banner():
    print("=" * 60)
    print("  Bingo Downloader Web - Security Key Generator")
    print("=" * 60)
    print()


def main():
    print_banner()

    # Generate API Key
    print("🔑 Generated API Key:")
    api_key = generate_api_key()
    print(f"   {api_key}")
    print()

    # Generate Encryption Key
    print("🔒 Generated Cookie Encryption Key:")
    enc_key = generate_encryption_key()
    print(f"   {enc_key}")
    print()

    # Configuration examples
    print("=" * 60)
    print("📝 Add these to your .env file:")
    print("=" * 60)
    print()

    print("# API Key Authentication")
    print("API_KEY_ENABLED=true")
    print(f"API_KEYS={api_key}")
    print()

    print("# Cookie Encryption")
    print(f"COOKIE_ENCRYPTION_KEY={enc_key}")
    print("COOKIE_EXPIRATION_HOURS=24")
    print()

    print("# Rate Limiting (already configured by default)")
    print("RATE_LIMIT_ENABLED=true")
    print("RATE_LIMIT_REQUESTS=60")
    print("RATE_LIMIT_WINDOW=60")
    print()

    print("# CORS (configure for your domain)")
    print("CORS_ORIGINS=http://localhost:8000,https://yourdomain.com")
    print()

    print("=" * 60)
    print("✅ Security Configuration Summary")
    print("=" * 60)
    print()
    print("1. API Key Authentication: ENABLED")
    print("   - Include this header in your API requests:")
    print(f"   X-API-Key: {api_key}")
    print()
    print("2. Cookie Encryption: ENABLED")
    print("   - Cookies will be encrypted with the generated key")
    print("   - Cookies expire after 24 hours by default")
    print()
    print("3. Rate Limiting: ENABLED")
    print("   - 60 requests per minute per IP address")
    print()
    print("4. CORS: CONFIGURE MANUALLY")
    print("   - Set CORS_ORIGINS to your frontend domain(s)")
    print()

    print("=" * 60)
    print("📚 For more information, see web/backend/SECURITY.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
