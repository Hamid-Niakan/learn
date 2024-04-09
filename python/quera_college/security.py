import re


class Security:
    pattern = r'[A-Z][a-z]*:www\.[a-z0-9\.]+/\w+'

    def secure(self, info):
        if self.is_social_account_info(info):
            accounts = re.findall(self.pattern, info)
            for account in accounts:
                splited = account.split('/')
                encrypted_account = f'{splited[0]}/{self.encrypt(splited[1])}'
                info = info.replace(account, encrypted_account)
            return info
        return info

    def is_social_account_info(self, param):
        return bool(re.search(self.pattern, param))

    def encrypt(self, s):
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        result = ''
        for char, count in chars.items():
            char_weight = ord(char) - 96
            for i in range(1, count + 1):
                result += str(char_weight * i)
        return result


security = Security()
print(security.secure('FirstName:Ali, LastName:Alavi, BirthDate:1990/02/02 Gender:male Instagram:www.instagram.com/aalavi Degree:Master Twitter:www.twiter.com/alaviii imdb:www.imdb.com/alavi'))
