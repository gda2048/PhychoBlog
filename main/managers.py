from django.db import models


class PeopleQueryMixin(object):
    def delete(self):
        for person in self.all():
            person.delete()


class PeopleQuerySet(PeopleQueryMixin, models.QuerySet):
    pass


class PeopleManager(PeopleQueryMixin, models.Manager):
    def get_query_set(self):
        return PeopleQuerySet(self.model, using=self._db)
