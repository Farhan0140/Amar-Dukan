
from django.core.exceptions import ValidationError


def Validate_File_Size( file ):
    """ Given file must be less than 10 mb"""
    max_size = 10
    max_size_inBYTEs = max_size * 1024 * 1024

    if file.size() > max_size_inBYTEs:      # file.size()   return file size in byte's
        raise ValidationError(f"File size can't be greater than {max_size} MB")

