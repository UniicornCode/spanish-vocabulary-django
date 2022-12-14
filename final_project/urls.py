"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from SpanishVocabularyApp.views import home, categories, visit_spain, vocabulary, quiz, quiz_results
from final_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('categories/', categories, name="categories"),
    path('visit-spain/', visit_spain, name="visit-spain"),
    path('vocabulary/<slug:category>/', vocabulary, name="vocabulary"),
    path('vocabulary/', vocabulary, name="vocabulary"),
    path('quiz/', quiz, name="quiz"),
    path('quiz-results/', quiz_results, name="quiz-results")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
