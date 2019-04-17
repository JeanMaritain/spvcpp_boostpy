#cmake_minimum_required(VERSION 3.13)
#project(spvcpp_boostpy)
#
#set(CMAKE_CXX_STANDARD 11)
#
#add_executable(spvcpp_boostpy main.cpp)


cmake_minimum_required(VERSION 3.13)

execute_process(
        COMMAND python3.7-config --ldflags
        # --cflags
        COMMAND tr -d "\n"
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        OUTPUT_VARIABLE PYTHON_LDFLAGS
)

# solve
# Undefined symbols for architecture x86_64:
# "_PyUnicode_Type", referenced from:
# boost::python::to_python_value<char const* const&>::get_pytype() const in main.cpp.o
# "__Py_NoneStruct", referenced from:
# boost::python::api::object::object() in main.cpp.o
# ld: symbol(s) not found for architecture x86_64


set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} ${PYTHON_LDFLAGS})

project(hello_ext)

#set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} ${PYTHON_LDFLAGS})


set(CMAKE_VERBOSE_MAKEFILE ON)

set(CMAKE_CXX_STANDARD 11)

set(BUILD_SHARED_LIBS ON)

include_directories("/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/include/python3.7m/")
# solve fatal error: 'pyconfig.h' file not found

find_package(Boost 1.69.0 COMPONENTS system filesystem python37 REQUIRED)
    if (Boost_FOUND)
        # boost found in system lib
        include_directories(${Boost_INCLUDE_DIRS})
        # add_executable(spvcpp_boostpy main.cpp )
            add_library(hello_ext SHARED main.cpp)

            message("${Boost_LIBRARIES}")
            message("${Boost_INCLUDE_DIRS}")



        target_link_libraries(hello_ext ${Boost_LIBRARIES})

        set_target_properties(hello_ext PROPERTIES POSITION_INDEPENDENT_CODE ON)

    endif ()

set_target_properties(hello_ext PROPERTIES PREFIX "")
