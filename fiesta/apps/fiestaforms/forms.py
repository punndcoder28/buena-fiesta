from __future__ import annotations

from django.forms import DateInput as DjDateInput, Form, ModelForm
from django.utils.translation import gettext_lazy as _


class DateInput(DjDateInput):
    input_type = "date"


class BaseModelForm(ModelForm):
    template_name = "fiestaforms/classic.html"
    submit_text: str = _("Save")

    @property
    def base_form_class(self):
        return BaseModelForm


class BaseForm(Form):
    template_name = "fiestaforms/classic.html"
    submit_text: str = _("Submit")

    @property
    def base_form_class(self):
        return BaseForm
