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