#include <iostream>
#include <boost/python.hpp>
#include <boost/version.hpp>
#include <boost/python/args.hpp>
#include <boost/python/def.hpp>
#include <pyconfig.h>

#include "Elastos.ELA.SPV.Cpp/SDK/WalletCore/BIPs/Mnemonic.h"
#include "Elastos.ELA.SPV.Cpp/SDK/WalletCore/KeyStore/KeyStore.h"
#include "Elastos.ELA.SPV.Cpp/ThirdParty/json/nlohmann/json.hpp"
#include <Elastos.ELA.SPV.Cpp/SDK/Common/Log.h>

using namespace boost::python;
using namespace Elastos::ElaWallet;


char const* greet()
{
    std::cout << "Hello, World " << std::endl;
    return "greeting";
}


void foobar(const std::string &foo, const std::string &bar)
{
    std::cout << foo + bar << std::endl;
}


const char *MnemonicCreate()
{
	Mnemonic mnemonic("./Data");
	std::string phrase = mnemonic.Create("english");
	// TODO 这里内存没释放 内存会泄漏
	return strdup(phrase.c_str());
}


bool KeystoreImport(const std::string &keystoreJson, const std::string &passwd)
{
    KeyStore keystore;
	nlohmann::json j = nlohmann::json::parse(keystoreJson);
	return keystore.Import(j, passwd);
}


const char *KeystoreImportExport(const std::string &keystoreJson, const std::string &passwd)
{
    KeyStore keystore;
    nlohmann::json j = nlohmann::json::parse(keystoreJson);

    if (!keystore.Import(j, passwd)) {
        Log::error("import fail");
        return nullptr;
    }
    nlohmann::json result;
    result = keystore.Export(passwd, true);
    std::cout << result << std::endl;
    return strdup(result.dump().c_str());
}


BOOST_PYTHON_MODULE(spv_boost_py)
{
    def("greet", greet);
    def("foobar", foobar, args("foo", "bar"), "function with arguments");

    def("mn_create", MnemonicCreate);
    def("ks_import", KeystoreImport, args("KeystoreJson", "passwd"));
    def("ks_import_export", KeystoreImportExport, args("KeystoreJson", "passwd"));

};
