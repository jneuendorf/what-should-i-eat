from django.test import TestCase

from .models import Tag


# Create your tests here.

class TagTests(TestCase):
    """docstring for TagTests."""

    # method name must begin with "test_"
    def test_tag_colors_are_unique(self):
        """Each tag color should only exist once among all tags."""
        colors = (tag.color for tag in Tag.objects.all())

        for color in colors:
            try:
                idx = colors.index(color)
            except Exception as e:
                idx = -1
            self.assertIs(idx >= 0, True)
