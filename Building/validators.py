from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.utils.translation import ugettext as _


class MaxSizeValidator(MaxValueValidator):
    message = _('Twój plik przekracza maksymalny rozmiar pliku wynoszący %(limit_value) MB.')

    def __call__(self, value):
        cleaned = self.clean(value.size)
        params = {'limit_value': self.limit_value, 'show_value': cleaned, 'value': value}
        if self.compare(cleaned, self.limit_value * 1024 * 1024):
            raise ValidationError(self.message, code=self.code, params=params)
