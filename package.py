name = "oiio"

version = "3.0.9.1.hh.1.0.0"

authors = [
    "AcademySoftwareFoundation",
]

description = """Library and tools for reading and writing images"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "libtiff",
    "libjpeg",
    "libpng",
    "freetype",
    # "pugixml-1.14",  # will use bundled-in pugixml
    "tbb-2022.0",
    "pybind11",
    # "ffmpeg",  # ffmpeg was built statically (because of conflicts with Houdini) and OIIO is complaining
    "openexr-3.4",  # will bring imath
    "openvdb-13",
]

private_build_requires = []

variants = [
    ["python-3.11", "ocio-2.5.2", "numpy-2"],
    ["python-3.13", "ocio-2.5.2", "numpy-2"],
]


def commands():
    env.REZ_OIIO_ROOT = "{root}"
    env.OIIO_ROOT = "{root}"
    env.OIIO_LOCATION = "{root}"
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.OIIO_LIBRARY_DIR = "{root}/lib64"
    env.OPENIMAGEIOHOME = "{root}"  # for OpenShadingLanguage
    env.OPENIMAGEIO_ROOT_DIR = "{root}"  # for OpenColorIO

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.CMAKE_MODULE_PATH.append("{root}/lib64/cmake/OpenImageIO")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib64/python3.11/site-packages")
                env.UE_PYTHONPATH.append("{root}/lib64/python3.11/site-packages")
            elif python_ver.minor == 13:
                env.PYTHONPATH.append("{root}/lib64/python3.13/site-packages")
                env.UE_PYTHONPATH.append("{root}/lib64/python3.13/site-packages")


uuid = "repository.OpenImageIO"
build_system = "cmake"
