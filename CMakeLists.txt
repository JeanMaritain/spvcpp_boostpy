cmake_minimum_required(VERSION 3.10)

execute_process(
        COMMAND python3.7-config --ldflags
        COMMAND tr -d "\n"
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        OUTPUT_VARIABLE PYTHON_LDFLAGS
)
set(CMAKE_VERBOSE_MAKEFILE ON)
set(CMAKE_CXX_STANDARD 11)
set(BUILD_SHARED_LIBS ON)
set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS} ${PYTHON_LDFLAGS})

set(PYTHON3_HEADER_DIR "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/include/python3.7m/")
# set(PYTHON2_HEADER_DIR "/usr/include/python2.7")
# solve fatal error: 'pyconfig.h' file not found


project(spv_boost_py)
add_subdirectory(Elastos.ELA.SPV.Cpp)

include_directories(
        ${PYTHON3_HEADER_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_BINARY_DIR}

        ${CMAKE_CURRENT_SOURCE_DIR}/Elastos.ELA.SPV.Cpp
        ${CMAKE_CURRENT_BINARY_DIR}/Elastos.ELA.SPV.Cpp
        ${ThirdParty_INC_DIRS}
)


find_package(Boost 1.69.0 COMPONENTS system filesystem python37 REQUIRED)
    if (Boost_FOUND)
        # boost found in system lib
        include_directories(${Boost_INCLUDE_DIRS})
        add_library(spv_boost_py SHARED main.cpp Elastos.ELA.SPV.Cpp/SDK/Common/Log.cpp)

        message("[msg][Boost_LIBRARIES] ${Boost_LIBRARIES}")
        message("[msg][Boost_INCLUDE_DIRS] ${Boost_INCLUDE_DIRS}")

        target_link_libraries(spv_boost_py ${Boost_LIBRARIES} ${OpenSSL_LIBRARIES} walletcore)
        set_target_properties(spv_boost_py PROPERTIES POSITION_INDEPENDENT_CODE ON PREFIX "" SUFFIX ".so")

    endif ()



