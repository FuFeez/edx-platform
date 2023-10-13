# -*- coding: utf-8 -*-
"""
URLs for course_access_groups.
"""


from rest_framework import routers

from .views import (
    CourseViewSet,
    CourseAccessGroupViewSet,
    MembershipViewSet,
    MembershipRuleViewSet,
    PublicCourseViewSet,
    UserViewSet,
    GroupCourseViewSet,
)

router = routers.SimpleRouter()

router.register(
    r'courses',
    CourseViewSet,
    basename='courses',
)

router.register(
    r'course-access-groups',
    CourseAccessGroupViewSet,
    basename='course-access-groups',
)

router.register(
    r'memberships',
    MembershipViewSet,
    basename='memberships',
)

router.register(
    r'membership-rules',
    MembershipRuleViewSet,
    basename='membership-rules',
)

router.register(
    r'public-courses',
    PublicCourseViewSet,
    basename='public-courses',
)

router.register(
    r'users',
    UserViewSet,
    basename='users',
)

router.register(
    r'group-courses',
    GroupCourseViewSet,
    basename='group-courses',
)

urlpatterns = router.urls
