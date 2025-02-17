from django.db import models

### ABSTRACT MODELS

# class SchoolMember(models.Model):
#     name = models.CharField(max_length=60)
#
#     class Meta:
#         abstract = True
#
#
# class Student(SchoolMember):
#     name = models.CharField(max_length=60)
#
#
# class Teacher(SchoolMember):
#     name = models.CharField(max_length=60)


#### PROXY MODELS

# STORY_TYPES = (
#     ('f', 'Feature'),
#     ('i', 'Infographic'),
#     ('g', 'Gallery'),
# )
#
# class Story(models.Model):
#     type = models.CharField(max_length=1, choices=STORY_TYPES)
#     title = models.CharField(max_length=100)
#     body = models.TextField(blank=True, null=True)
#     infographic = models.ImageField(blank=True, null=True)
#     link = models.URLField(blank=True, null=True)
#     gallery = models.ForeignKey(Gallery, blank=True, null=True)
#
#
# class FeatureStory(Story):
#     objects = FeatureManager()
#     class Meta:
#         proxy = True
#
# class InfographicStory(Story):
#     objects = InfographicManager()
#     class Meta:
#         proxy = True
#
# class GalleryStory(Story):
#     objects = GalleryManager()
#     class Meta:
#         proxy = True
