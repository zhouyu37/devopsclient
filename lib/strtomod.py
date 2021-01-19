import importlib
def StrToMod(path):
    model_path,class_name = path.rsplit(".",1)
    model=importlib.import_module(model_path)
    cls = getattr(model,class_name)
    return cls