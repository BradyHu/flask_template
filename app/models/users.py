import datetime

from mongoengine import *
from flask_login import UserMixin
from .tasks import TaskModel


class UserModel(DynamicDocument, UserMixin):
    password = StringField(required=True)
    username = StringField(max_length=25, required=True, unique=True)
    email = StringField(max_length=30)

    name = StringField()
    online = BooleanField(default=False)
    last_seen = DateTimeField()

    is_admin = BooleanField(default=False)

    preferences = DictField(default={})
    permissions = ListField(defualt=[])

    @property
    def tasks(self):
        self._update_last_seen()
        if self.is_admin:
            return TaskModel.objects
        return TaskModel.objects(Q(owner=self.username))

    def can_view(self, model):
        if model is None:
            return False

        return model.can_view(self)

    def can_download(self, model):
        if model is None:
            return False

        return model.can_download(self)

    def can_delete(self, model):
        if model is None:
            return False
        return model.can_delete(self)

    def can_edit(self, model):
        if model is None:
            return False

        return model.can_edit(self)

    def _update_last_seen(self):
        self.update(last_seen=datetime.datetime.utcnow())