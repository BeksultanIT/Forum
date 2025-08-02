from webapp.forms.base_form import BaseForm
from webapp.models.forums import Forum


class ForumForm(BaseForm):
    class Meta:
        model = Forum
        fields = ('title','description')