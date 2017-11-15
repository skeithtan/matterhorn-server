from django.contrib.auth import user_logged_in
from django.db.models import Model, DateTimeField, Manager, QuerySet, ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
COLLEGES = (
    ('CCS', 'College of Computer Science'),
    ('RVRCOB', 'Ramon V del Rosario College of Business'),
    ('CLA', 'College of Liberal Arts'),
    ('SOE', 'School of Economics'),
    ('GCOE', 'Gokongwei College of Engineering'),
    ('COL', 'College of Law'),
    ('BAGCED', 'Brother Andrew Gonzales College of Education')
)


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(archived_at=timezone.now())

    def undelete(self):
        return super(SoftDeletionQuerySet, self).update(archived_at=None, user=None)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(archived_at=None)

    def dead(self):
        return self.exclude(archived_at=None)


class SoftDeletionManager(Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        self.archived_only = kwargs.pop('archived_only', False)

        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(archived_at=None)

        if self.archived_only:
            return SoftDeletionQuerySet(self.model).filter(archived_at__isnull=False)

        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(Model):
    archived_at = DateTimeField(blank=True, null=True)
    objects = SoftDeletionManager()
    current = SoftDeletionManager(alive_only=False)
    archived = SoftDeletionManager(archived_only=False)
    user = ForeignKey(User, null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.archived_at = timezone.now()
        self.user = kwargs['user']
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()

    def undelete(self):
        self.archived_at = None
        self.user = None
        self.save()
