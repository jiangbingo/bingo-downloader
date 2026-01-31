#!/usr/bin/env python3
"""
Test script for security features
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_imports():
    """Test that all security modules can be imported"""
    print("Testing imports...")
    try:
        from web.backend.security import (
            api_key_middleware,
            verify_api_key,
            get_api_key_from_header,
            rate_limit_middleware,
            encrypt_data,
            decrypt_data,
            generate_encryption_key,
        )
        print("✅ All security modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False


def test_encryption():
    """Test encryption and decryption"""
    print("\nTesting encryption...")
    try:
        from web.backend.security.encryption import (
            encrypt_data,
            decrypt_data,
            generate_encryption_key,
            get_encryption_status,
        )

        # Test encryption
        key = generate_encryption_key()
        test_data = "This is a test cookie string"
        encrypted = encrypt_data(test_data, key)
        decrypted = decrypt_data(encrypted, key)

        assert decrypted == test_data, "Decrypted data doesn't match original"
        print("✅ Encryption/decryption works correctly")

        # Test status
        status = get_encryption_status()
        print(f"   Encryption enabled: {status['encryption_enabled']}")
        print(f"   Cookie expiration: {status['cookie_expiration_hours']} hours")

        return True
    except Exception as e:
        print(f"❌ Encryption test failed: {e}")
        return False


def test_rate_limit():
    """Test rate limiter"""
    print("\nTesting rate limiter...")
    try:
        from web.backend.security.rate_limit import rate_limiter
        import asyncio

        async def run_test():
            # Test basic rate limiting
            client_id = "test-client-1"
            for i in range(10):
                allowed, retry_after = await rate_limiter.is_allowed(client_id)
                assert allowed, f"Request {i+1} should be allowed"

            print("✅ Rate limiter works correctly")
            print(f"   Limit: {rate_limiter.requests} requests per {rate_limiter.window} seconds")

        asyncio.run(run_test())
        return True
    except Exception as e:
        print(f"❌ Rate limiter test failed: {e}")
        return False


def test_auth():
    """Test API key authentication"""
    print("\nTesting API key authentication...")
    try:
        from web.backend.security.auth import verify_api_key

        # Test with auth disabled (default)
        result = verify_api_key("any-key")
        assert result == True, "Should return True when auth is disabled"
        print("✅ API key authentication works correctly")
        print("   Note: Auth is disabled by default. Enable with API_KEY_ENABLED=true")

        return True
    except Exception as e:
        print(f"❌ Auth test failed: {e}")
        return False


def test_config():
    """Test configuration"""
    print("\nTesting configuration...")
    try:
        from web.backend.config import (
            API_KEY_ENABLED,
            RATE_LIMIT_ENABLED,
            RATE_LIMIT_REQUESTS,
            RATE_LIMIT_WINDOW,
            CORS_ORIGINS,
            COOKIE_EXPIRATION_HOURS,
        )

        print(f"   API_KEY_ENABLED: {API_KEY_ENABLED}")
        print(f"   RATE_LIMIT_ENABLED: {RATE_LIMIT_ENABLED}")
        print(f"   RATE_LIMIT_REQUESTS: {RATE_LIMIT_REQUESTS}")
        print(f"   RATE_LIMIT_WINDOW: {RATE_LIMIT_WINDOW}")
        print(f"   CORS_ORIGINS: {CORS_ORIGINS}")
        print(f"   COOKIE_EXPIRATION_HOURS: {COOKIE_EXPIRATION_HOURS}")
        print("✅ Configuration loaded successfully")

        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("  Bingo Downloader Web - Security Test Suite")
    print("=" * 60)

    tests = [
        ("Imports", test_imports),
        ("Configuration", test_config),
        ("Encryption", test_encryption),
        ("Rate Limiting", test_rate_limit),
        ("API Key Auth", test_auth),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} test crashed: {e}")
            results.append((name, False))

    # Summary
    print("\n" + "=" * 60)
    print("  Test Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"  {status}: {name}")

    print()
    print(f"  Total: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 All tests passed! Security features are working correctly.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
