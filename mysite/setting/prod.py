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
SITE_ID = 1

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

# '/home/currentuser_cpanel/public_html ...
MEDIA_ROOT = '/home/mkomidir/public_html/media'
STATIC_ROOT = '/home/mkomidir/public_html/static'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# EMAIL Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'omidweb67@gmail.com'
EMAIL_HOST_PASSWORD = 'zktu hcfl pzjk gjox'


MAINTENANCE_MODE = True