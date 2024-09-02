from rest_framework.routers import DefaultRouter

from django.urls import path, include
from admins.api.urls import admin_router
from blogs.api.urls import blog_router
from feedbacks.api.urls import feedback_router
from heros.api.urls import hero_router
from medias.api.urls import media_router
from volunteers.api.urls import volunteer_router
from categories.api.urls import categories_router


router = DefaultRouter()

router.registry.extend(admin_router.registry)
router.registry.extend(blog_router.registry)
router.registry.extend(feedback_router.registry)
router.registry.extend(hero_router.registry)
router.registry.extend(media_router.registry)
router.registry.extend(volunteer_router.registry)
router.registry.extend(categories_router.registry)

urlpatterns = [
    path("", include(router.urls))
]
