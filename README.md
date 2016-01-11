# django-urllocale
Django app for localize site via url subdirectory: http://sample.org/en/,  http://sample.org/fr/ 

## Set up

#####1. Clone this repo

#####2. Copy `urllocale` app into your django project root

#####3. Add `urllocale` into `INSTALLED_APPS` in your `settings.py`
```python
INSTALLED_APPS = (
    ...
    'urllocale',
)
```

##### 4. Add `'urllocale.middleware.UrlLocaleMiddleware'` after `'django.contrib.sessions.middleware.SessionMiddleware'` and before `'django.middleware.common.CommonMiddleware'` in `settings.py`. 
And make sure that there is no `'django.middleware.locale.LocaleMiddleware'`

```python
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'urllocale.middleware.UrlLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
```

##### 5. Define `LANGUAGES` and `LANGUAGE_CODE` in `settings.py`

```python
LANGUAGES = [
    ('ky', 'Кыргыз'),
    ('ru', 'Русский'),
]

LANGUAGE_CODE = 'ru'
```

##### 6. (Optional) Add `'urllocale.context_processor.urllocale'` into template context proccessors

```python

for django 1.8 ot higher

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'urllocale.context_processor.urllocale'
            ]
        }
    },
]

for django smaller than 1.8

TEMPLATE_CONTEXT_PROCESSORS = [
  "django.contrib.auth.context_processors.auth",
  "django.template.context_processors.debug",
  "django.template.context_processors.i18n",
  "django.template.context_processors.media",
  "django.template.context_processors.static",
  "django.template.context_processors.tz",
  "django.contrib.messages.context_processors.messages",
  'urllocale.context_processor.urllocale'
]

```


## Usage

##### In views

use `locale_reverse` instead of built-in `reverse` function to reverse urls

```python
from urllocale import locale_reverse

...

return redirect(locale_reverse('home'))
```

##### In templates

load `urllocale` tempaletags library and use `locale_url` instead of 'url' to reverse urls. 

```html
{% load i18n urllocale %}

<a href="{% locale_url 'home' %}">Home</a>
```

use `lang_code` context variable to get current language code in templates
```html
{{ lang_code }}
```
