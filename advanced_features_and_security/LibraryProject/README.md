# LibraryProject - Advanced Features and Security

## Overview
This Django project is part of the ALX Django Learn Lab. It demonstrates advanced features such as:

- Custom User Model
- User Groups and Permissions
- Secured access to views
- CRUD operations on a `Book` model
- Admin interface customization

---

## Models

### CustomUser
- Inherits from Django's `AbstractUser`.
- Additional fields:
  - `date_of_birth` (DateField)
  - `profile_photo` (ImageField)
- Managed by a custom `CustomUserManager`.

### Book
- Fields:
  - `title` (CharField)
  - `author` (CharField)
  - `publication_year` (IntegerField)

---

## Permissions and Groups

Custom permissions are defined on the `Book` model:

- `can_view` — Allows viewing book details.
- `can_create` — Allows creating new book records.
- `can_edit` — Allows editing existing books.
- `can_delete` — Allows deleting books.

Groups are created in Django Admin and assigned permissions:

- **Viewers** — Can view books.
- **Editors** — Can view, create, and edit books.
- **Admins** — Full access, including delete.

---

## Views and Access Control

Permission checks are enforced in views using decorators:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    ...

    ## Permissions and Security Implementation

### Custom Permissions
- Added custom permissions to the `Book` model: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Permissions are enforced in views using `@permission_required('bookshelf.can_view', raise_exception=True)`.

### Groups
- Created groups: Editors, Viewers, Admins.
- Assigned relevant permissions to each group using the Django admin.

### Secure Views
- Used Django ORM for queries (safe from SQL injection).
- Used `BookForm` for create/edit to validate user input.
- Decorated all views with `login_required` and `permission_required` to enforce access control.

### Templates
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

### Security Settings
- `DEBUG = False` in production.
- Set `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF` in `settings.py`.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` set to `True` for HTTPS-only cookies.

### Testing
- Created test users and assigned them to different groups.
- Verified that permissions are enforced correctly when performing actions in the app.

# Security Configurations Implemented

1. **HTTPS Enforcement**
   - `SECURE_SSL_REDIRECT = True`
   - All HTTP requests are redirected to HTTPS.

2. **HSTS**
   - `SECURE_HSTS_SECONDS = 31536000`
   - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
   - `SECURE_HSTS_PRELOAD = True`
   - Ensures browsers only use HTTPS for 1 year and includes subdomains.

3. **Secure Cookies**
   - `SESSION_COOKIE_SECURE = True`
   - `CSRF_COOKIE_SECURE = True`
   - Cookies transmitted only over HTTPS.

4. **Secure Headers**
   - `X_FRAME_OPTIONS = 'DENY'` → prevents clickjacking.
   - `SECURE_CONTENT_TYPE_NOSNIFF = True` → prevents MIME sniffing.
   - `SECURE_BROWSER_XSS_FILTER = True` → enables XSS filtering in browsers.

5. **Deployment**
   - SSL/TLS certificates installed on web server.
   - HTTP requests automatically redirected to HTTPS.

6. **Next Steps**
   - Periodically review SSL certificate expiry.
   - Check all forms and endpoints for secure input handling.