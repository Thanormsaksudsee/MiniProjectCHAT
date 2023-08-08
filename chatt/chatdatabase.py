class chatRecord():
    def __init__(self):
        self.data = []
    
    def addMessage(self, message):
        self.data.append(message)
    
    def getMessage(self, messageID):
        if len(self.data) == 0:
            return 'No message yet!'
        elif messageID == 0:
            return '\n'.join(self.data)
        elif messageID != 0:
            temp = self.data[messageID:]
            return '\n'.join(temp)
        else:
            return "\n"
