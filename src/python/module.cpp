/*
 * Python interfaces for Smoldyn simulator.
 * Author: Dilawar Singh <dilawar.s.rajput@gmail.com>
 */

#include <algorithm>
#include <exception>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

using namespace pybind11::literals; // for _a

/**
 * @brief Definition of Python module _smoldyn.
 *
 * @param _smoldyn (name of the module)
 * @param m
 */
PYBIND11_MODULE(nfsim, m)
{
    // py::options options;
    // options.disable_function_signatures();

    m.doc() = R"pbdoc(
        Low level Python interface for the smoldyn simulator. This module is not
        meant for direct user interaction. The user api defined in smoldyn/smoldyn.py
        uses this module to create an user friendly API.
    )pbdoc";

    m.attr("__version__") = NFSIM_VERSION; // Version is set by CMAKE
}
