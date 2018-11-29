from djangoapp.djangoapp import settings

if __name__ == '__main__':
    basePath = settings.BASE_DIR
    print(basePath)
    staticPath = settings.STATIC_URL
    print(staticPath)