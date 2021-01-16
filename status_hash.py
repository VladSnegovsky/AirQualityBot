# From: https://www.convertstring.com/ru/Hash/MD5
# MD5 Hash Generator

class Hash:
    class Rec:
        def __init__(self, _message, _hash):
            self.message = _message
            self.hash = _hash

        def __str__(self):
            return "message: %s   hash: %s" % (self.message, self.hash)

    def __init__(self):
        self.list = []
        self.copy_list = []

    def add_record(self, message, hash):
        self.list.append(Hash.Rec(message, hash))

    def out(self):
        print('\n'.join(str(item) for item in self.list))


hash_class = Hash()
hash_class.add_record("Select new location",  "B84BAD6271E582DA65D6D72F302305E8")
hash_class.add_record("Select from list",     "AB0D918A39A3B28FE15C61F79B28632F")
hash_class.add_record("Country",              "59716C97497EB9694541F7C3D37B1A4D")
hash_class.add_record("Add new location",     "85D20237D10004B5F0F249397AA7DEAB")
hash_class.add_record("Get notification",     "24A578342C2B0E54774F0516A1884688")
hash_class.add_record("Main",                 "A02C83A7DBD96295BEAEFB72C2BEE2DE")
hash_class.add_record("Enter location name",  "A1BDF03330A2F37677ACDB9D097A3530")
hash_class.add_record("My Locations",         "DEC168AA910B8E7FD267D35E61BCFF27")
hash_class.add_record("Location Settings",    "EA65AEBED40AD8077CC90BBF999ABF5C")
hash_class.add_record("Edit Name",            "3CD57C1C49290D3B94BE13534F23A34E")
hash_class.add_record("Edit Step",            "9DFFC52C311BEECC195B7F5BB0CCFA12")
hash_class.add_record("Change language",      "8F241C62A9523B05BF0B6B16A09D856D")
hash_class.add_record("Choose language",      "A8D69CDFAD4C19ED22BF693B8871064E")
hash_class.add_record("Instructions",         "49CC8E6220245B65CD7D20FC6CCC74F5")


# shows all messages with hash
def show_all_hashes():
    hash_class.out()


# returns hash
def get_hash(message):
    find = False
    for item in hash_class.list:
        if item.message == message:
            find = True
            return item.hash
    if not find:
        return "ERROR"