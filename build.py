import os
import shutil
import sys

from distutils.core import Distribution

from setuptools import setup
from setuptools_rust import Binding, RustExtension, build_rust

from subprocess import call


class BuildFailed(Exception):
    pass


def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """

    print("setup_kwargs:", setup_kwargs)

    print("os.curdir:", os.getcwd())
    original_project_dir = os.path.dirname(os.path.realpath(__file__))
    cargo_toml_path = os.path.join(original_project_dir, "dfrs", "Cargo.toml")
    # cargo_toml_path = os.path.join(original_project_dir, "Cargo.toml")
    print("original_project_dir:", original_project_dir)
    print("cargo_toml_path:", cargo_toml_path)

    extension = RustExtension(target="dfrs", path=cargo_toml_path, binding=Binding.NoBinding)
    print(extension)
    lib_name = extension.get_lib_name()
    print("lib_name:", lib_name)

    # https://docs.python.org/3/distutils/apiref.html#distutils.core.Distribution
    dist = Distribution(attrs=setup_kwargs)

    builder = build_rust(dist)
    builder.initialize_options()
    builder.build_extension(extension)
    print("Extension built!")
    print("*********** 0.")
    call(["find", "."])
    print("*********** 1.")

    # raise BuildFailed("Just to see the logs")
