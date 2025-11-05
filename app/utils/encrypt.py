import bcrypt


class Encrypt:
    """
    密码加密工具类
    """

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        对密码进行哈希加密
        :param password: 明文密码
        :return: 哈希加密后的密码
        """
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password_hash(password: str, password_hash: str) -> bool:
        """
        验证密码是否正确
        :param password: 明文密码
        :param password_hash: 哈希密码
        :return: 验证结果
        """
        password_bytes = password.encode("utf-8")

        password_hash_bytes = password_hash.encode("utf-8")

        return bcrypt.checkpw(password_bytes, password_hash_bytes)