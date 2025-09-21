# Security Measures Implemented

## HTTPS Configuration

- Redirected all HTTP traffic to HTTPS using `SECURE_SSL_REDIRECT = True`.
- Enabled HSTS with a 1-year duration and subdomain inclusion.

## Secure Cookies

- Enforced secure cookies with `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`.

## Security Headers

- Implemented:
  - `X_FRAME_OPTIONS = 'DENY'` to prevent clickjacking.
  - `SECURE_CONTENT_TYPE_NOSNIFF` to block MIME-type sniffing.
  - `SECURE_BROWSER_XSS_FILTER` to enable XSS protection.

## Deployment Configuration

- Configured Nginx to redirect HTTP to HTTPS and serve the site securely.
- SSL/TLS certificates issued by Let's Encrypt.

## Recommendations

- Regularly review and update the SSL certificates.
- Monitor security headers for compliance with evolving best practices.
