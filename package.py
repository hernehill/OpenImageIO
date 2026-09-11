name = "oiio"

version = "2.5.16.0.hh.1.0.5"

authors = [
    "AcademySoftwareFoundation",
]

description = """Library and tools for reading and writing images"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "libtiff",
    "libjpeg-3.1.4.1.hh.1.0.1",
    "libpng",
    "freetype",
    # "pugixml-1.14",  # will use bundled-in pugixml
    "tbb-2021.9",
    "pybind11",
    "ffmpeg",  # ffmpeg was built statically (because of conflicts with Houdini) and OIIO is complaining
    "openexr-3.1",  # will bring imath
]

private_build_requires = ["visual_studio"]

variants = [
    ["python-3.9", "ocio-2.1.3", "numpy-1.26.4", "openvdb-11"],
    ["python-3.9", "ocio-2.2.1", "numpy-1.26.4", "openvdb-11"],
    ["python-3.9", "ocio-2.3.2", "numpy-1.26.4", "openvdb-11"],
    ["python-3.10", "ocio-2.1.3", "numpy-1.26.4", "openvdb-11"],
    ["python-3.10", "ocio-2.1.3", "numpy-1.26.4", "openvdb-12"],
    ["python-3.10", "ocio-2.2.1", "numpy-1.26.4", "openvdb-11"],
    ["python-3.10", "ocio-2.2.1", "numpy-1.26.4", "openvdb-12"],
    ["python-3.10", "ocio-2.3.2", "numpy-1.26.4", "openvdb-11"],
    ["python-3.10", "ocio-2.3.2", "numpy-1.26.4", "openvdb-12"],
    ["python-3.11", "ocio-2.1.3", "numpy-1.26.4", "openvdb-11"],
    ["python-3.11", "ocio-2.1.3", "numpy-1.26.4", "openvdb-12"],
    ["python-3.11", "ocio-2.2.1", "numpy-1.26.4", "openvdb-11"],
    ["python-3.11", "ocio-2.2.1", "numpy-1.26.4", "openvdb-12"],
    ["python-3.11", "ocio-2.3.2", "numpy-1.26.4", "openvdb-11"],
    ["python-3.11", "ocio-2.3.2", "numpy-1.26.4", "openvdb-12"],
]


def commands():
    env.REZ_OIIO_ROOT = "{root}"
    env.OIIO_ROOT = "{root}"
    env.OIIO_LOCATION = "{root}"
    env.OIIO_INCLUDE_DIR = "{root}/include"
    env.OIIO_LIBRARY_DIR = "{root}/lib"
    env.OPENIMAGEIOHOME = "{root}"  # for OpenShadingLanguage
    env.OPENIMAGEIO_ROOT_DIR = "{root}"  # for OpenColorIO

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.LIB.append("{root}/lib")
    env.CMAKE_MODULE_PATH.append("{root}/lib/cmake/OpenImageIO")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib/python3.9/site-packages")
                env.UE_PYTHONPATH.append("{root}/lib/python3.9/site-packages")
            elif python_ver.minor == 10:
                env.PYTHONPATH.append("{root}/lib/python3.10/site-packages")
                env.UE_PYTHONPATH.append("{root}/lib/python3.10/site-packages")
            elif python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib/python3.11/site-packages")
                env.UE_PYTHONPATH.append("{root}/lib/python3.11/site-packages")


uuid = "repository.OpenImageIO"
build_system = "cmake"
