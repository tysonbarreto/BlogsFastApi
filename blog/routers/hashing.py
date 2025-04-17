from passlib.context import CryptContext



pass_ctxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

hash = pass_ctxt.hash
verify = pass_ctxt.verify


if __name__=='__main__':
    __all__=["hash","verify"]