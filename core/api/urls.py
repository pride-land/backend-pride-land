from rest_framework.routers import DefaultRouter

from django.urls import path, include
from admins.api.urls import admin_router
from blogs.api.urls import blog_router
from feedbacks.api.urls import feedback_router
from medias.api.urls import media_router
from volunteers.api.urls import volunteer_router
from accounts.api.urls import staff_router

router = DefaultRouter()

router.registry.extend(staff_router.registry)
router.registry.extend(admin_router.registry)
router.registry.extend(blog_router.registry)
router.registry.extend(feedback_router.registry)
router.registry.extend(media_router.registry)
router.registry.extend(volunteer_router.registry)

urlpatterns = [
    path("", include(router.urls))
]
