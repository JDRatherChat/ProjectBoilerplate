"""
Production-ready Django REST Framework configuration.
"""

REST_FRAMEWORK = {
    # ✅ Permissions: default to authenticated-only
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],

    # ✅ Authentication: remove session for pure API, or keep if admin access is needed
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # Uncomment if you're using token or JWT authentication
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],

    # ✅ Pagination
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,

    # ✅ Renderer: only JSON for production (remove Browsable API for security/performance)
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],

    # ✅ Parsers
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
}
