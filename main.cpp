#include <iostream>
#include <boost/python.hpp>
#include <boost/version.hpp>

char const* greet()
{
    std::cout << "Hello, World " << std::endl;
    return "greeting";

}

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
};



//int main() {
//    std::cout << "Boost version: " << BOOST_VERSION << std::endl;
//
//    greet();
//
//    return 0;
//}