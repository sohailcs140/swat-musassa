from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rk#+16(7=lu(3a9u!-s6n3$84s5_uvrd%2j--0a6q%s31r(t71'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_htmx',
    'users',
    'core',
    "app",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    "swat_musassa.middleware.LoginRequiredMiddleware",
]

ROOT_URLCONF = 'swat_musassa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'swat_musassa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',  # Replace with your database name
        'USER': 'root',  # Replace with your MySQL username
        'PASSWORD': 'root',  # Replace with your MySQL password
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',  # Default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

# URL to use when referring to static files
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# for production
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



AUTH_USER_MODEL= "users.User"

LOGIN_REDIRECT_URL = '/'
LOGIN_EXEMPT_URLS = ['login', 'password-reset', 'password-reset-done', 'password_reset_confirm']
LOGOUT_REDIRECT_URL = '/'


# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587 
EMAIL_USE_TLS = True  
EMAIL_USE_SSL = False  
EMAIL_HOST_USER = 'sohailcs140@gmail.com' 
EMAIL_HOST_PASSWORD = 'jnfb rnmc vepy sjiu'  
DEFAULT_FROM_EMAIL = 'sohailcs140@gmail.com'





COUNTRIES_WITH_FLAGS = {
    "Afghanistan": "🇦🇫",
    "Albania": "🇦🇱",
    "Algeria": "🇩🇿",
    "Andorra": "🇦🇩",
    "Angola": "🇦🇴",
    "Antigua and Barbuda": "🇦🇬",
    "Argentina": "🇦🇷",
    "Armenia": "🇦🇲",
    "Australia": "🇦🇺",
    "Austria": "🇦🇹",
    "Azerbaijan": "🇦🇿",
    "Bahamas": "🇧🇸",
    "Bahrain": "🇧🇭",
    "Bangladesh": "🇧🇩",
    "Barbados": "🇧🇧",
    "Belarus": "🇧🇾",
    "Belgium": "🇧🇪",
    "Belize": "🇧🇿",
    "Benin": "🇧🇯",
    "Bhutan": "🇧🇹",
    "Bolivia": "🇧🇴",
    "Bosnia and Herzegovina": "🇧🇦",
    "Botswana": "🇧🇼",
    "Brazil": "🇧🇷",
    "Brunei": "🇧🇳",
    "Bulgaria": "🇧🇬",
    "Burkina Faso": "🇧🇫",
    "Burundi": "🇧🇮",
    "Cabo Verde": "🇨🇻",
    "Cambodia": "🇰🇭",
    "Cameroon": "🇨🇲",
    "Canada": "🇨🇦",
    "Central African Republic": "🇨🇫",
    "Chad": "🇹🇩",
    "Chile": "🇨🇱",
    "China": "🇨🇳",
    "Colombia": "🇨🇴",
    "Comoros": "🇰🇲",
    "Congo (Congo-Brazzaville)": "🇨🇬",
    "Congo (Democratic Republic of the)": "🇨🇩",
    "Costa Rica": "🇨🇷",
    "Croatia": "🇭🇷",
    "Cuba": "🇨🇺",
    "Cyprus": "🇨🇾",
    "Czech Republic": "🇨🇿",
    "Denmark": "🇩🇰",
    "Djibouti": "🇩🇯",
    "Dominica": "🇩🇲",
    "Dominican Republic": "🇩🇴",
    "Ecuador": "🇪🇨",
    "Egypt": "🇪🇬",
    "El Salvador": "🇸🇻",
    "Equatorial Guinea": "🇬🇶",
    "Eritrea": "🇪🇷",
    "Estonia": "🇪🇪",
    "Eswatini": "🇸🇿",
    "Ethiopia": "🇪🇹",
    "Fiji": "🇫🇯",
    "Finland": "🇫🇮",
    "France": "🇫🇷",
    "Gabon": "🇬🇦",
    "Gambia": "🇬🇲",
    "Georgia": "🇬🇪",
    "Germany": "🇩🇪",
    "Ghana": "🇬🇭",
    "Greece": "🇬🇷",
    "Grenada": "🇬🇩",
    "Guatemala": "🇬🇹",
    "Guinea": "🇬🇳",
    "Guinea-Bissau": "🇬🇼",
    "Guyana": "🇬🇾",
    "Haiti": "🇭🇹",
    "Honduras": "🇭🇳",
    "Hungary": "🇭🇺",
    "Iceland": "🇮🇸",
    "India": "🇮🇳",
    "Indonesia": "🇮🇩",
    "Iran": "🇮🇷",
    "Iraq": "🇮🇶",
    "Ireland": "🇮🇪",
    "Israel": "🇮🇱",
    "Italy": "🇮🇹",
    "Jamaica": "🇯🇲",
    "Japan": "🇯🇵",
    "Jordan": "🇯🇴",
    "Kazakhstan": "🇰🇿",
    "Kenya": "🇰🇪",
    "Kiribati": "🇰🇮",
    "Kuwait": "🇰🇼",
    "Kyrgyzstan": "🇰🇬",
    "Laos": "🇱🇦",
    "Latvia": "🇱🇻",
    "Lebanon": "🇱🇧",
    "Lesotho": "🇱🇸",
    "Liberia": "🇱🇷",
    "Libya": "🇱🇾",
    "Liechtenstein": "🇱🇮",
    "Lithuania": "🇱🇹",
    "Luxembourg": "🇱🇺",
    "Madagascar": "🇲🇬",
    "Malawi": "🇲🇼",
    "Malaysia": "🇲🇾",
    "Maldives": "🇲🇻",
    "Mali": "🇲🇱",
    "Malta": "🇲🇹",
    "Marshall Islands": "🇲🇭",
    "Mauritania": "🇲🇷",
    "Mauritius": "🇲🇺",
    "Mexico": "🇲🇽",
    "Micronesia": "🇫🇲",
    "Moldova": "🇲🇩",
    "Monaco": "🇲🇨",
    "Mongolia": "🇲🇳",
    "Montenegro": "🇲🇪",
    "Morocco": "🇲🇦",
    "Mozambique": "🇲🇿",
    "Myanmar": "🇲🇲",
    "Namibia": "🇳🇦",
    "Nauru": "🇳🇷",
    "Nepal": "🇳🇵",
    "Netherlands": "🇳🇱",
    "New Zealand": "🇳🇿",
    "Nicaragua": "🇳🇮",
    "Niger": "🇳🇪",
    "Nigeria": "🇳🇬",
    "North Korea": "🇰🇵",
    "North Macedonia": "🇲🇰",
    "Norway": "🇳🇴",
    "Oman": "🇴🇲",
    "Pakistan": "🇵🇰",
    "Palau": "🇵🇼",
    "Panama": "🇵🇦",
    "Papua New Guinea": "🇵🇬",
    "Paraguay": "🇵🇾",
    "Peru": "🇵🇪",
    "Philippines": "🇵🇭",
    "Poland": "🇵🇱",
    "Portugal": "🇵🇹",
    "Qatar": "🇶🇦",
    "Romania": "🇷🇴",
    "Russia": "🇷🇺",
    "Rwanda": "🇷🇼",
    "Saint Kitts and Nevis": "🇰🇳",
    "Saint Lucia": "🇱🇨",
    "Saint Vincent and the Grenadines": "🇻🇨",
    "Samoa": "🇼🇸",
    "San Marino": "🇸🇲",
    "Sao Tome and Principe": "🇸🇹",
    "Saudi Arabia": "🇸🇦",
    "Senegal": "🇸🇳",
    "Serbia": "🇷🇸",
    "Seychelles": "🇸🇨",
    "Sierra Leone": "🇸🇱",
    "Singapore": "🇸🇬",
    "Slovakia": "🇸🇰",
    "Slovenia": "🇸🇮",
    "Solomon Islands": "🇸🇧",
    "Somalia": "🇸🇴",
    "South Africa": "🇿🇦",
    "South Korea": "🇰🇷",
    "South Sudan": "🇸🇸",
    "Spain": "🇪🇸",
    "Sri Lanka": "🇱🇰",
    "Sudan": "🇸🇩",
    "Suriname": "🇸🇷",
    "Sweden": "🇸🇪",
    "Switzerland": "🇨🇭",
    "Syria": "🇸🇾",
    "Taiwan": "🇹🇼",
    "Tajikistan": "🇹🇯",
    "Tanzania": "🇹🇿",
    "Thailand": "🇹🇭",
    "Timor-Leste": "🇹🇱",
    "Togo": "🇹🇬",
    "Tonga": "🇹🇴",
    "Trinidad and Tobago": "🇹🇹",
    "Tunisia": "🇹🇳",
    "Turkey": "🇹🇷",
    "Turkmenistan": "🇹🇲",
    "Tuvalu": "🇹🇻",
    "Uganda": "🇺🇬",
    "Ukraine": "🇺🇦",
    "United Arab Emirates": "🇦🇪",
    "United Kingdom": "🇬🇧",
    "United States of America": "🇺🇸",
    "Uruguay": "🇺🇾",
    "Uzbekistan": "🇺🇿",
    "Vanuatu": "🇻🇺",
    "Vatican City": "🇻🇦",
    "Venezuela": "🇻🇪",
    "Vietnam": "🇻🇳",
    "Yemen": "🇾🇪",
    "Zambia": "🇿🇲",
    "Zimbabwe": "🇿🇼"
}