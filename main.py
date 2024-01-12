from uuid import uuid4


class Collection:
    def __init__(self, name):
        self.__name = name
        self.__records = []  # array of

    @property
    def name(self):
        return self.__name

    def add(self, record: dict):
        self.__records.append({uuid4(): record})

    def update(self, key, value):
        for entry in self.__records:
            entry[key] = value

    def results(self):
        return self.__records

    def __repr__(self) -> str:
        for record in self.__records:
            return f"{record}"


class KeyValueStore:
    def __init__(self) -> None:
        self.collections = []

    def insert(self, collection: str, data: dict) -> None:
        for coll in self.collections:
            if coll.name == collection:
                return
        c = Collection(collection)
        c.add(data)
        self.collections.append(c)

    def update(self, collection: str, key, value) -> None:
        for item in self.collections:
            if item.name == collection:
                item.update(key, value)

    def display(self, collection: str) -> None:
        for item in self.collections:
            if item.name == collection:
                print(item.results)

    def fetch_collections(self):
        return [item.name for item in self.collections]


db = KeyValueStore()
db.insert("users", {"name": "Dapo", "state_of_origin": "Lagos", "gender": "Male"})
db.insert("users", {"name": "Taiwo", "state_of_origin": "Ondo", "gender": "Female"})
db.display("users")
print(db.fetch_collections())
# db.update("users", {"name": "Taiwo", "state_of_origin": "Ondo", "gender": "Female"})
