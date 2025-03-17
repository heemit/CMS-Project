from django.db                          import models
from django.utils.text                  import slugify
from grape_js.models                    import GrapeJsHTMLField

# Simple History Model
from simple_history.models              import HistoricalRecords
# Model Utils
from model_utils                        import FieldTracker

# Page Model
class Page(models.Model):
    url         =   models.SlugField(max_length=255, unique=True, help_text="Unique URL identifier")
    content     =   GrapeJsHTMLField()
    show_header =   models.BooleanField(default=True)
    show_footer =   models.BooleanField(default=True)
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now=True)

    history     =   HistoricalRecords()
    tracker     =   FieldTracker()

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.url)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.url
