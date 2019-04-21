# python3
# - tool ---------------------------------------------------------------------
import os

def chk_bin(bin_relative_dir, bin_name):
    def chk_hash(path):
        cmd_shasum_res = (lambda output_lines: output_lines[0].split()[0])
        cmd_shasum_file = (lambda output_lines: output_lines[0].split()[1])

        hash_res = os.popen('shasum -a 256 {}'.format(path)).readlines()
        print("{} {}".format(
            cmd_shasum_res(hash_res),
            cmd_shasum_file(hash_res))
        )
        return cmd_shasum_res(hash_res),

    def chk_copy(source, target):
        os.system("cp {} {}".format(source, target))
        print('\n{} copied to {}'.format(source, target))
        os.system('shasum -a 256 {}'.format(target))

    bin_output_path = os.path.join(os.path.expanduser('~'), bin_relative_dir, bin_name)
    bin_output_hash = chk_hash(bin_output_path)

    bin_in_test_path = os.path.join(os.getcwd(), bin_name)

    if os.path.exists(bin_in_test_path):
        bin_in_test_hash = chk_hash(bin_in_test_path)

        if not bin_output_hash == bin_in_test_hash:
            chk_copy(bin_output_path, bin_in_test_path)

    else:
        chk_copy(bin_output_path, bin_in_test_path)


print_type = lambda v: print('value: {}\n type: {}'.format(v, type(v)))

# - prepare lib ---------------------------------------------------------------------


LIB_RELATIVE_DIR = "CLionProjects/spvcpp_boostpy/cmake-build-debug"
LIB_NAME = "spv_boost_py"
LIB_SUFFIX = ".so"

chk_bin(bin_relative_dir=LIB_RELATIVE_DIR, bin_name=LIB_NAME+LIB_SUFFIX)

try:
    import foo
    print(dir(foo))
except:
    print('so import error')

# - test ---------------------------------------------------------------------

test_ks_import = (lambda : foo.ks_import)()
test_ks_import_export = (lambda : foo.ks_import_export)()

def test_simple_func():
    a = foo.greet()
    print(a)

    b = foo.mn_create()
    print(b)

class TestComplex(object):

    ks_a = 'aaaa'
    ks_b = 'bbbb'

    def test_ks_wrap(self):
        r = foo.ks_wrap(foo=self.ks_a, bar=self.ks_b)
        print_type(r)

    ks = '{"adata":"","cipher":"aes","ct":"cdvCw8PXoKgFz6W/uwsndXFXHJ7bEl1jt3ehKk/d1n1Lb2L7pU+0PN5Tvt6UhmNuJSndgMNi5HYMwsF9qw3WFVtJLDZBkvUChb5mlLreL2kcV/J37I8gW+474SjEdSF2xqeClk37CbOszQ4Ly9PXCu+y7PVVNvqzNnEIbIfEOhAnsMmyhxBDPwP4YspKvylklJJTkEn1K+B6hWpccyC9Uyjlz80qj4uaEDU3iJxbOytRgUnm+iN1TRRMGbtA9f+BUdzl2URdDvKFBOl+y9Nt3IyPamrTtaS4NzSWO+f7xuAewK9NdMiSQiWe79hiU/h/0arIwxLC5vSKF0TJ8wg9jf9LfB9Q1ycVgPYXXMFGDXLiihseFAyUyIRhChHbELLpWEKjvnSc56QCRoaHtfEpI19d2twf1gwtCvkW3NuIEP8cYYeJFYl3HweG9DeOqzXN+RTNa48gDWnj7QbKKT1x1VB4G07cSm9CEcxExoIWm5bXtKG5GpxT1NKlXLc9+V9s0Oyr8I3odGLJoHzp7zFUdGEG5L0+gXg9pQL2XXoDy0GT3GGTR+XpgEFjFFfkp8+A9DdefW1YdQXqigGVS9izcbSWm3X744QV2hqxepBARvphbE6nJ+zAJoeqdECuvHmAgW6pZLHkI65UerR9cPpM9U7Hmvlw6sU1rWYv1JGZchxGTBvvWNI1CgIutzYyabtCU0eo1+Uk42Wz4DB1BWSVi2Gjz7wqjVsQH2EY5wqV9D38uzFmSOqqqSVUKp1fwrkbNolzAewIc/1wP7VJzgdgp24J3+9Zrs5dOP6VP/ibgFlEcV5laoPBOR1sAS/JskCQCy4CLCVhm0DIjxNDiXmU/7fDp+hT9QmG/qK4G4xmvp/Rg1pSRIUvbLnJ9B0Z4oUKuJoWTEk3UT17fs3cqYT0hVEIsjc075iknGaiLdC4/znPj29XBgxLQWfd2sYEDh/B4I4F8t0Al2AndmXlnTwJukH9Cn+pJNpt9exBnsG688N3xXi0Ggi3DavLrHP59WSh47JFY4cWYAuiZLoKPVOGJfIxN/azXoE0cfDPZ904y9gRN54uTqm2fR1BnKPfQEiEUpsQB2rdFJSIrkAz/qKR9M+mNB9wanQupjNI5o2b1q4y1RD0ObkFxux80hhmIQNrF787eorhgt96AVXXoWAlTdZPQbrIXrFY3RBpUgkVRxwTP80D5YynWeXP4lxPnCTEj7bLQtjf/1FOw/rTSeuR5ZTpAnQ5GtjL3v4X5aR/yuEqO58eEpFZSzKsQ3MbMY7yjFk6mKdRA5m264eJ2/crxW8YIePiJrvxR3RevuOB3iGhHd3YgFoFXbcCgocLntw4VNO3mx65KecnUg0A3tRE+kgLJvdc7+RTVVXNLMlcX7BpvM7fBjKCwylpOxunXCMejHs+PIjWOA==","iter":10000,"iv":"mlnr1CuySYgQs1hhKfwFQQ==","ks":128,"mode":"ccm","salt":"lbX/Qo+lWm0=","ts":64,"v":1}'
    ks_5000 = '{"adata":"","cipher":"aes","ct":"OQbwpbKaINLnqI869yHg27VbVQcHDUARMSNN+N2uICxuCVQJZJQWdOxF9ni80CtOsTw98uyRd2UHTr1UU1nLSJZvkAjvSktKvFsCRimLgyMrjc/bvPMd6XTXys57FLim4+f2VMoUFAwgGcLRK1TnBF5W0xCQveWLN8b9R3PdV0nU3QONFJEqfysb27kxNWaMjSW8DYmogxDL9AxO+VDqnD36pFPiFAsyZJYzaRKkMT9EpKWVM/PqZ7h1ZOz1/0nadV3KY6hdx3kne37O5bABK98JYAi82dyVnucQa5GnbGU/b1EjmIDB1OuasMjfz2sQJmr6Q7BfFtdzHzQTXYyMGwc45HGwRxOlyGW9D3pp0xKmKqouh7jmKkwikRt/hMmRknFjtIA6SnEbh4YFEhCx0wj9bYgzewrcZAN/t0Dhj7E5HHb/wMctfNKDovNVphoXPEXWeB4b4GgsI1ovUU3nmW+9MJhorcZTRw4viTEBmUBbskTSrnOEGO0URUkPprBzm6gyK8HIZzpugCescwqEJm+CNQQs7eYpdo9KSihP876qrqpd+dLLabjetyJXusLhbdpRf/8QzdBFZa413XBFf8AiF8YL/zCVYT+8KUbdTFTWTpjCVF+8FIqwPTyzdR9LQshvES4j+UzUadAu/ohMwsaoJXm/6/uTHJApm2/NSKaS2pCZnofyl+i9dxKoOEGeeJq7j7oXz8vfo8qXMmLpwyvZ+ybt3sP5c8aAk6E4fngKP2M4+TIU/etX8EsybryHXcyUicxX1KgZogNlBu3Pm1imUl/ClsJHsPdWtMWkxTYVbwg09jS1mOo1ihIYNGipYi+N1KMCeGoRTDF6MQHRuukw0tMwOFcdEV0gTNr47fwdDpJ0LRbCGS7fqkTFqE47Vbae/0YH5K0uB+Ug7mCWcJlB6N3zo4tRpf53SRRdJv21ytV5ExAzyJgidCVlMO79KbA4EZ7qUG8vq89yebdgRzFNsWgXKlQAO3oxntARvyiF+4I9sEjZphoeTyl6gMOP+Z+LnbSssmTJQHHAbLZK5b734tVvK+v1BKej5iMnnS46RECxBvlkIpvorP2fN+WonjR9CC+caf3CeIz7gDm5ULlrbVrFL4UO+4Z1vPywigMtdo9mtdzsSc5xd4xCxf++iLI2fyQ+G03bvtyy9XCdesPxkm8YQPlyN6JbESHjwy+X6oC3pcCpIinsOEfzFefA3gJXW2+MHyyHG/BEq6wau6Q7O9tCTlDn8H4HIHMLJPcyaf85yXeZUecM8aztwLGVwSB4itPFkjT24f4AOlfZXrB0Xk4AykOEyJgFk2DSCATULwd6gyWhrttoCjY7XgqISP7t5OVy2KErzC0SBGgxM2IGP8Dc9Ojt0XyCttIIzJBqQg==","iter":10000,"iv":"co/Agybqknk1KBuvvuy5CA==","ks":128,"mode":"ccm","salt":"0OkfSnJnHaA=","ts":64,"v":1}'
    ks_1 = '{"adata":"","cipher":"aes","ct":"oGgn5ZaWJuVuX6oEm5fE+OgIRtOYvzm7xWz6F33uPCnOYtnr5ZvFSqRvSURhdCHNH9Imc2APyfungMMQEC8v1KBHA5DVP4BHOfmWhO1LJkEyXYbDQDTZ9qfKYiKbEu0x2mh7QIltwym+RcVd0fZ7D7WALUpcMOPLBlQhK6uLk/1lDoVhxZ7BxS97rahtWT9NSsb4Ek+IBCMXBnu3B+BcFzeeZktYuHI+K75WMsa0IssTIdd6jP9PXJknqwWus++fboREPKauQvY3zOVpklKOCw9DfYDWPLD0Np47gKMdvktoSL3s+HxktGPo1EmncNh6MnM+st2H8AgEjlvZ4jVgaNp43CKnH33ZcrKHmtIMlBnEHBiuUUMEnrPWjsSd612Y252zdwNoZQXQuwFMi9iCZKInwhXhfCwcO3WGnqBCF2zGpEjjd7sKiDWFlOzqDPj74cfhcw4BtdvJAbX4eSdQwURr5j5ymzQDUTdcoIOR3/b/+cwYrlQJ9GM3FIlbLwwbxbBPLWE4hAbkw7B9Vt9MDPEgube850RfNo2eDpKKzmkfQRK1SZUED5viqvEcaCJPu0IDq1WxahVlly1imiaA41aQL/H0/BEpkcv/2oNDhjCy/QtZrAOdjfkcKFJoPvraLLgF8cMy7lmaUvRcduq3ZCVfgEv3Hn9Sbrov6tGp5gsXK5a751l76uPKWK41MsPrgMZkqxTWWSl5btHAUIQxa0TVGR3EOwa7ijR9VhFy1OupWpWypJsXx5kbnJASDodrS/xlCXtKaPBL1vnVfrSgg4/68X8dOaVWBxndgSY9Usp+G+Jgmj51xTTGcdhyS/OXb/dvUYpgE65zMrtnkV4+cypyckFb2VT/+nKZatT2MS7fRb07NCw/O3w3cGyswdaQny9c3fH6zUTABYARd955XPcChU+PUwRdZfBVh3/0RaMCDsb+5yMwbzjCgEuGXTuANatsO5ElnnHZq42MTtGECOU01Hd8SCYqGT0yhNqMFa4XPOcSwKFvTmlvH6OQrDUe20I+Js6f58dFvuX4U14t9NAvboIYxULfDjzWNBZUmcjSPHOGEtQzimtRV0e3oBtN7gAZYKdAUyGYsjFcfc7/O0JcSY5UJd6CV6hT/7gGS+CQnGduj8B9tOXHaJyhSwOMpS1L2dlGBdfypjSJSaUw41IQ6QGOv+p2XARg6AiGbUJd6HgW7QIkTz+gOwlMqYPl/1oRZ/hQEeKy1tmq8IToBAQorSOPBcIjZlIdyfzPQ8/1DUwOslpfk60iCGvYiRh3Sr6Q0V85t6oqxc+/OjrxOUI4iGxFwmx9jfdDDRpzxyM9ZIYxiCIMHUHwbU/ILy7o1LV7Tjdncum196sQ5H0emUIj4cSRlIY6OuyaCbotjaASXHyarUIljp/A9ylrHaaGPGNmH7CrHuA=","iter":10000,"iv":"YJdhZbmASLPwwpq5U03ksQ==","ks":128,"mode":"ccm","salt":"7AKHPDjVCns=","ts":64,"v":1}'


    def test_ks_import_wrongpassword(self):
        r = test_ks_import(self.ks_1, 'asdfasdfa')
        print_type(r)

    def test_ks_import_non_keystore(self):
        r = test_ks_import('jfjfjfjfjfjfjfjfjf', 'asdfasdfa')
        print_type(r)

    def test_ks_import_unknown_keystore(self): # maybe old keystore
        r = test_ks_import(self.ks, 'asdfasdf')
        print_type(r)

    def test_ks_import_fine_keystore_wrong_password(self): # maybe old keystore
        r = test_ks_import(self.ks_5000, 'asdfasdf')
        print_type(r)

    def test_ks_import_fine_keystore_fine_password(self): # maybe old keystore
        r = test_ks_import(self.ks_1, 'asdfasdf')
        print_type(r)


# test_simple_func()

# TestComplex().test_ks_wrap()

# TestComplex().test_ks_import_non_keystore()

# TestComplex().test_ks_import_unknown_keystore()

# TestComplex().test_ks_import_fine_keystore_wrong_password()

# TestComplex().test_ks_import_fine_keystore_fine_password()



