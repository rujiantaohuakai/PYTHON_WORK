class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """初始化一个调查问卷，并设定问题"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """显示调查问卷的问题"""
        print(self.question)
    
    def store_response(self, response):
        """存储单份调查答卷"""
        self.responses.append(response)
    
    def show_results(self):
        """显示调查结果"""
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")
    