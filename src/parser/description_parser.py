

class DescriptionData:
    def __init__(self,accommodation):
        self.data = accommodation

    def beyond_id(self):
        return self.data['id']

    def avantio_id(self):
        return self.data['managed_accounts'][0]['channel_id']