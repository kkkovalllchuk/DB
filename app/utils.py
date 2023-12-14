def get_primary_key(model):
    return model._meta.pk.column
