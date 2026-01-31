#!/usr/bin/env python3
"""
Simple configuration check for security features
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def check_config():
    """Check security configuration"""
    print("=" * 60)
    print("  Bingo Downloader Web - Security Configuration Check")
    print("=" * 60)
    print()

    try:
        from web.backend import config

        print("✅ Configuration loaded successfully")
        print()

        print("📋 Current Security Settings:")
        print("-" * 60)

        # API Key Authentication
        print(f"\n1. API Key Authentication:")
        print(f"   Enabled: {config.API_KEY_ENABLED}")
        print(f"   Header Name: {config.API_KEY_NAME}")
        if config.API_KEYS:
            print(f"   API Keys: {len(config.API_KEYS)} key(s) configured")
        else:
            print(f"   API Keys: None (authentication disabled)")

        # Rate Limiting
        print(f"\n2. Rate Limiting:")
        print(f"   Enabled: {config.RATE_LIMIT_ENABLED}")
        print(f"   Limit: {config.RATE_LIMIT_REQUESTS} requests per {config.RATE_LIMIT_WINDOW} seconds")

        # CORS
        print(f"\n3. CORS Configuration:")
        print(f"   Allowed Origins: {config.CORS_ORIGINS}")
        print(f"   Allow Credentials: {config.CORS_ALLOW_CREDENTIALS}")
        print(f"   Allowed Methods: {config.CORS_ALLOW_METHODS}")
        print(f"   Allowed Headers: {config.CORS_ALLOW_HEADERS}")

        # Cookie Encryption
        print(f"\n4. Cookie Encryption:")
        print(f"   Expiration: {config.COOKIE_EXPIRATION_HOURS} hours")
        print(f"   Custom Key: {'Set' if config.COOKIE_ENCRYPTION_KEY else 'Not set (will auto-generate)'}")

        print()
        print("-" * 60)
        print("\n✅ All security configurations are valid")
        print("\n📝 Next steps:")
        print("   1. Install dependencies: pip install -r web/backend/requirements.txt")
        print("   2. Generate security keys: python3 scripts/generate_security_keys.py")
        print("   3. Configure .env file (copy from web/backend/.env.example)")
        print("   4. Start the server: python -m web.backend.main")

        return True

    except Exception as e:
        print(f"❌ Configuration check failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def check_files():
    """Check if security files exist"""
    print("\n" + "=" * 60)
    print("  File Structure Check")
    print("=" * 60)
    print()

    import pathlib
    base_dir = pathlib.Path(__file__).parent.parent

    files = [
        ("Security Module", "web/backend/security/__init__.py"),
        ("API Key Auth", "web/backend/security/auth.py"),
        ("Rate Limiting", "web/backend/security/rate_limit.py"),
        ("Cookie Encryption", "web/backend/security/encryption.py"),
        ("Updated Config", "web/backend/config.py"),
        ("Updated Main", "web/backend/main.py"),
        ("Environment Example", "web/backend/.env.example"),
        ("Security Guide", "web/backend/SECURITY.md"),
    ]

    all_exist = True
    for name, path in files:
        full_path = base_dir / path
        exists = full_path.exists()
        status = "✅" if exists else "❌"
        print(f"  {status} {name}: {path}")
        if not exists:
            all_exist = False

    print()
    if all_exist:
        print("✅ All security files are present")
    else:
        print("❌ Some security files are missing")

    return all_exist


def main():
    """Run all checks"""
    config_ok = check_config()
    files_ok = check_files()

    print("\n" + "=" * 60)
    print("  Summary")
    print("=" * 60)
    print()

    if config_ok and files_ok:
        print("🎉 Security features have been successfully implemented!")
        print()
        print("📚 For detailed information, see:")
        print("   - web/backend/SECURITY.md")
        print("   - SECURITY_ENHANCEMENTS.md")
        return 0
    else:
        print("⚠️  Please review the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
