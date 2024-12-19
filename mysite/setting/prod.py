from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-05_j_ipj_hjn9_)c0+_&uz@*@u1h0g#p+7j+kq=)#*hqv_w)ju'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mkomid67.ir','www.mkomid67.ir']

# INSTALLED_APPS =[]

# site framework
SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mkomidir_travel',
		'USER': 'mkomidir_omid',
		'PASSWORD': 'P2umM7n6ssGW',
		'HOST':'localhost',
		'PORT':'3306',
	}
}

MEDIA_ROOT = '/home/mkomidir/public_html/media'
STATIC_ROOT = '/home/mkomidir/public_html/static'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


# EMAIL Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'omidweb67@gmail.com'
EMAIL_HOST_PASSWORD = 'zktu hcfl pzjk gjox'

##### Secuity

## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

## X-Frame-Options
X_FRAME_OPTIONS = 'DENY'

#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True

## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

# maintenance
MAINTENANCE_MODE = True

