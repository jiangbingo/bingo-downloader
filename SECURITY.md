# Security Policy

## Supported Versions

Currently, only the latest version of bingo-downloader-skill is supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

### How to Report

1. **Do NOT** create a public issue
2. Send an email to: [security contact email]
3. Include:
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (if known)

### What to Expect

- Initial response within 48 hours
- Detailed confirmation of the vulnerability within 7 days
- Estimated timeline for a fix
- Notification when the fix is released

### Disclosure Policy

We follow responsible disclosure:
- Coordinate with reporters on release timelines
- Public disclosure after fix is released
- Credit to reporters in security advisories

## Security Best Practices

### For Users

1. **Keep yt-dlp updated**:
   ```bash
   make update
   # or
   pip install -U yt-dlp
   ```

2. **Review URLs before downloading**: Only download from trusted sources

3. **Cookie handling**: Be cautious when using browser cookies, as they may contain sensitive authentication tokens

4. **File permissions**: Ensure downloaded files have appropriate permissions

### For Developers

1. **Input validation**: Always validate and sanitize URLs from external sources

2. **Command injection**: Never pass unsanitized input to shell commands

3. **File operations**: Validate file paths to prevent directory traversal

4. **Dependencies**: Regularly update dependencies and review security advisories

## Security Features

- No remote code execution capabilities
- No automatic execution of downloaded files
- Explicit user confirmation for all operations
- Sandboxed download paths (configurable)

## Vulnerability Response Process

1. **Receipt**: Acknowledge vulnerability report within 48 hours
2. **Analysis**: Investigate and reproduce within 7 days
3. **Fix**: Develop and test patch
4. **Release**: Deploy fix with security advisory
5. **Credit**: Acknowledge reporter (with permission)

## Security Advisories

Security advisories will be published on GitHub Security Advisories and include:

- CVE identifier (if applicable)
- Severity rating (CVSS)
- Affected versions
- Fixed versions
- Mitigation steps
- Patch upgrade instructions

## Additional Resources

- [GitHub Security](https://github.com/security)
- [Report a security vulnerability](https://github.com/jiangbingo/bingo-downloader-skill/security/advisories/new)
- [Dependabot alerts](https://github.com/jiangbingo/bingo-downloader-skill/network/alerts)
