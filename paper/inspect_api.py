from _bootstrap import bootstrap_asymptoticFunction
bootstrap_asymptoticFunction()

import inspect
import pkgutil
import importlib
import asymptoticFunction


def iter_modules(pkg):
    prefix = pkg.__name__ + "."
    for m in pkgutil.walk_packages(pkg.__path__, prefix):
        yield m.name


def list_callables(mod):
    funcs = []
    classes = []

    for name, obj in inspect.getmembers(mod):
        if inspect.isfunction(obj):
            funcs.append((name, obj))
        elif inspect.isclass(obj):
            classes.append((name, obj))

    return funcs, classes


def safe_import(name):
    try:
        return importlib.import_module(name)
    except Exception as e:
        return e


def print_module_api(mod_name, mod):
    print(f"\n=== {mod_name} ===")

    if isinstance(mod, Exception):
        print(f"  [IMPORT ERROR] {mod}")
        return

    funcs, classes = list_callables(mod)

    if not funcs and not classes:
        print("  (no public callables)")
        return

    if funcs:
        print("  functions:")
        for name, obj in funcs:
            try:
                sig = inspect.signature(obj)
            except Exception:
                sig = "(signature unavailable)"
            print(f"    {mod_name}.{name}{sig}")

    if classes:
        print("  classes:")
        for name, obj in classes:
            try:
                sig = inspect.signature(obj)
            except Exception:
                sig = "(signature unavailable)"
            print(f"    {mod_name}.{name}{sig}")


def main():
    print("\n=== INSPECTING asymptoticFunction API ===")

    for mod_name in iter_modules(asymptoticFunction):
        mod = safe_import(mod_name)
        print_module_api(mod_name, mod)


if __name__ == "__main__":
    main()
