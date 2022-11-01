class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        return '; '.join(
            f'{key}={self.__dict__[key]}' for key in self.str_fields
        )

