# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
from collections import OrderedDict
from mangrove.form_model.validator_types import ValidatorTypes
from mangrove.utils.types import is_empty

def case_insensitive_lookup(values, code):
    for fieldcode in values:
        if fieldcode.lower() == code.lower():
            return values[fieldcode]
    return None

class MandatoryValidator(object):

    def get_mandatory_fields(self, fields):
        return [field for field in fields if field.is_required()]


    def validate(self,values,fields, dbm=None):
        errors = OrderedDict()
        mandatory_fields = self.get_mandatory_fields(fields)
        for field in mandatory_fields:
            if is_empty(case_insensitive_lookup(values, field.code)):
                errors[field.code] = "Answer for question " + str(field.code) + " is required"
        return errors

    def to_json(self):
        return dict(cls=ValidatorTypes.MANDATORY)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return True
        return False

