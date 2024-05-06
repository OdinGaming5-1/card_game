class config:
    __conf = {
    "user_character_folder": "img/Free Knight 120x80/",
    "enemy_character_folder": "img/Huntress 150x150/",
    "magicalcards":"cards/attack_magical.json",
    "physicalcards":"cards/attack_physical.json"
    }
    # __setters = ["username", "password"]

    @staticmethod
    def config(name):
        return config.__conf[name]

    # @staticmethod
    # def set(name, value):
    #     if name in config.__setters:
    #         config.__conf[name] = value
    #     else:
    #         raise NameError("Name not accepted in set() method")
