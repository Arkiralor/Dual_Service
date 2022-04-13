DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken"
]

CUSTOM_APPS = [
    "ExtAPIs",
    "user"
]

if __name__ == "__main__":
    print("This is a module, not a script.")