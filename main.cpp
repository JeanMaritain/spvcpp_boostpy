#include <iostream>
#include <boost/python.hpp>
#include <boost/version.hpp>
#include <Elastos.ELA.SPV.Cpp/SDK/WalletCore/BIPs/Mnemonic.h>
#include <Elastos.ELA.SPV.Cpp/SDK/WalletCore/KeyStore/KeyStore.h>
#include <Elastos.ELA.SPV.Cpp/ThirdParty/json/nlohmann/json.hpp>

using namespace boost::python;
using namespace Elastos::ElaWallet;

char const* greet()
{
    std::cout << "Hello, World " << std::endl;
    return "greeting";

}

BOOST_PYTHON_MODULE(hello_ext)
{
    def("greet", greet);
};

const char *MnemonicCreate()
{
	Mnemonic mnemonic("./Data");
	std::string phrase = mnemonic.Create("english");
	std::cout << phrase << std::endl;

	// TODO 这里内存没释放 内存会泄漏
	return strdup(phrase.c_str());
}

BOOST_PYTHON_MODULE(mnemonic)
{
	def("create", MnemonicCreate);
};

// TODO 研究一下参数怎么传
bool KeystoreImport(const std::string &/* or const char * ??? */keystoreJson, const std::string &passwd)
{
	Keystore keystore;

	nlohmann::json j = nlohmann::json::parse(keystoreJson);

	return keystore.Import(j, passwd);
}

BOOST_PYTHON_MODULE(keystore)
{
	def("import", KeystoreImport);
};


//int main() {
//    std::cout << "Boost version: " << BOOST_VERSION << std::endl;
//
//    greet();
//
//    return 0;
//}