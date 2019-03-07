
class MockStore:
    @staticmethod
    def write_dict(data: dict, object_key: str) -> dict:
        print(f'mock write:')
        print({'storage': 'mock', object_key: data})
        return {"mock store": True}
