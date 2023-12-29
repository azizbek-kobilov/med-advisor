from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/')),
    prefix_default_language=False
)

# Media Assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
